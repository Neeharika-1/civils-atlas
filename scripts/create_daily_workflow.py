"""Build the single-file installer; payload is inspectable ZIP data, not a secret.
Run locally after reviewing the listed code/data. Never called by nightly Actions.
"""
import base64,hashlib,io,json,pathlib,textwrap,zipfile
R=pathlib.Path(__file__).resolve().parents[1]
FILES=['scripts/update_compilations.py','data/compilation-registry.json','research/edition19/Compilation-Automation.md','requirements.txt','template.html','README.md','START-HERE.md','SAVED-PROJECT-STATUS.md','DAILY-WEBSITE.md','DAILY-UPDATES-SETUP.md','scripts/build.py','scripts/build_site.py','scripts/update.py','scripts/daily-home.js','scripts/ingest_documents.py','scripts/merge_research.py','scripts/export_research_supplement.py','scripts/reconcile.py','scripts/validate.py','scripts/test_daily_upgrade.py','scripts/test_edition19.py','scripts/create_daily_workflow.py','data/source-registry.json','research/edition19/research-delta.json','research/edition19/Research-Log.md','research/edition19/Source-Recovery.md','research/Research-Status.md','volumes/Edition-19-Mains-Frameworks.md']
files={p:(R/p).read_bytes()for p in FILES};manifest={'edition':19,'files':{p:hashlib.sha256(b).hexdigest()for p,b in files.items()}}
files['embedded-upgrade-manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
out=io.BytesIO()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for p,b in sorted(files.items()):
  i=zipfile.ZipInfo(p,(2026,11,7,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o100644<<16;z.writestr(i,b)
payload=out.getvalue();sha=hashlib.sha256(payload).hexdigest();encoded=base64.b64encode(payload).decode()
installer='''import base64, hashlib, io, json, os, pathlib, stat, zipfile
root=pathlib.Path.cwd().resolve()
expected="__SHA__"
encoded="""
__PAYLOAD__
"""
raw=base64.b64decode(encoded)
if hashlib.sha256(raw).hexdigest()!=expected:raise SystemExit('Embedded upgrade checksum mismatch')
marker=root/'.edition19-dashboard-installed'
rebuild=not marker.exists()or marker.read_text().strip()!=expected
with zipfile.ZipFile(io.BytesIO(raw))as z:
    info=z.infolist()
    if len(info)>100 or sum(x.file_size for x in info)>8_000_000:raise SystemExit('Unexpected upgrade size')
    manifest=json.loads(z.read('embedded-upgrade-manifest.json'))
    if {x.filename for x in info}!={*manifest['files'],'embedded-upgrade-manifest.json'}:raise SystemExit('Unexpected upgrade member')
    for i in info:
        p=pathlib.PurePosixPath(i.filename)
        if p.is_absolute()or '..'in p.parts or '\\\\'in i.filename or stat.S_ISLNK(i.external_attr>>16):raise SystemExit('Unsafe upgrade path')
        target=(root/i.filename).resolve()
        if not target.is_relative_to(root):raise SystemExit('Upgrade path escapes workspace')
        data=z.read(i)
        if i.filename!='embedded-upgrade-manifest.json'and hashlib.sha256(data).hexdigest()!=manifest['files'][i.filename]:raise SystemExit('Member checksum mismatch')
    for name in manifest['files']:
        target=root/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(name))
print('Verified and installed Edition 19 code/research delta; no existing note JSON overwritten.')
with open(os.environ['GITHUB_OUTPUT'],'a')as f:f.write('rebuild='+str(rebuild).lower()+'\\n'+'patch_sha='+expected+'\\n')
'''.replace('__SHA__',sha).replace('__PAYLOAD__','\n'.join(textwrap.wrap(encoded,100)))
workflow='''# Edition 19: one-file update. Embedded ZIP is checksum-verified and contains
# reviewable scripts, template, guides and the sparse 14-note research delta.
# No separate ZIP upload, API key, access token or Codespace is required.
name: Daily source discovery
on:
  push:
    paths: ['.github/workflows/daily.yml']
  workflow_dispatch:
  schedule:
    - cron: '0 1 * * *' # 06:30 IST; GitHub scheduling can be delayed.
concurrency:
  group: civils-atlas-update
  cancel-in-progress: false
jobs:
  update:
    runs-on: ubuntu-latest
    timeout-minutes: 25
    permissions:
      contents: write
    outputs:
      publish_ready: ${{ steps.ready.outputs.value }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.repository.default_branch }}
      - name: Install the verified embedded upgrade
        id: install
        shell: python
        run: |
__INSTALLER__
      - uses: actions/setup-python@v6
        with:
          python-version: '3.12'
          cache: pip
      - name: Install dependencies and bounded OCR support
        run: |
          python -m pip install -r requirements.txt
          sudo apt-get update -qq
          sudo apt-get install -y -qq fonts-dejavu-core poppler-utils tesseract-ocr tesseract-ocr-eng
      - name: Merge researched additions and preserve existing note IDs
        run: |
          python scripts/merge_research.py
          python scripts/reconcile.py
          python scripts/validate.py
          python scripts/test_daily_upgrade.py
          python scripts/test_edition19.py
      - name: Discover permitted links and retain source failures
        run: |
          set +e
          python scripts/update.py
          code=$?
          set -e
          if [ "$code" -ne 0 ] && [ "$code" -ne 2 ]; then exit "$code"; fi
      - name: Collect public PIB and newspaper compilations
        run: python scripts/update_compilations.py
      - name: Extract eligible primary PDFs, with bounded OCR
        run: python scripts/ingest_documents.py
      - name: Rebuild all study documents when this upgrade changes
        if: steps.install.outputs.rebuild == 'true'
        run: |
          python scripts/export_research_supplement.py
          python scripts/build.py
      - name: Rebuild dashboard and verify the resulting data
        env:
          PATCH_SHA: ${{ steps.install.outputs.patch_sha }}
        run: |
          python scripts/build_site.py
          python scripts/validate.py
          printf '%s\\n' "$PATCH_SHA" > .edition19-dashboard-installed
      - name: Summarise actual source health
        shell: python
        run: |
          import json, os, pathlib
          d=json.loads(pathlib.Path('data/automation-status.json').read_text())
          p=json.loads(pathlib.Path('data/document-intake.json').read_text())
          with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f:
              f.write('## Daily sweep\\n')
              f.write(f"Sources returning links: **{d['sources_ok']}/{d['sources_tested']}**. Links are not verified notes.\\n\\n")
              f.write(f"AP Finance PDFs machine-extracted: **{p['extracted']}/{p['attempted']}**; pending: **{p['pending']}**. Extraction is not factual/legal verification.\\n\\n")
              f.write('### Unresolved sources\\n')
              for x in json.loads(pathlib.Path('data/update-log.json').read_text()):
                  if x['status']!='ok': f.write(f"- {x['source']}: {x.get('error',x['status'])}\\n")
              f.write('\\nNo automatic verified-note authorship or completed all-source audit is claimed.\\n')
      - name: Summarise compilation access
        shell: python
        run: |
          import json, os, pathlib
          c=json.loads(pathlib.Path('data/compilation-health.json').read_text())
          with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f:
              f.write(f"\\n## Secondary compilation desk\\n{c['working']}/{c['tested']} streams returned links; {c['new_links']} new URLs. Secondary links are not verified study notes.\\n")
      - name: Save the upgraded app, notes and diagnostic state
        run: |
          git config user.name 'civils-atlas-bot'
          git config user.email 'civils-atlas-bot@users.noreply.github.com'
          git add -A
          git diff --cached --quiet || git commit -m 'Edition 19 research and daily source/document sweep'
          git push
      - name: Prepare the public website
        shell: python
        run: |
          import pathlib, shutil
          root=pathlib.Path('.'); dest=root/'.pages';dest.mkdir(exist_ok=True)
          for name in ['data','volumes','research']:
              if (root/name).exists():shutil.copytree(root/name,dest/name,dirs_exist_ok=True)
          for p in [root/'index.html',root/'Study-Notes.docx',*root.glob('*.md')]:
              if p.exists():shutil.copy2(p,dest/p.name)
          (dest/'.nojekyll').touch()
      - name: Keep a diagnostic artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: daily-source-diagnostics
          path: |
            data/automation-status.json
            data/document-intake.json
            data/compilation-health.json
            data/update-log.json
            data/source-coverage.json
          retention-days: 14
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .pages
      - name: Allow diagnostic website publication
        id: ready
        run: echo 'value=true' >> "$GITHUB_OUTPUT"
      - name: Report total discovery outage after preserving publication artifacts
        shell: python
        run: |
          import json,pathlib
          d=json.loads(pathlib.Path('data/automation-status.json').read_text())
          if not d['sources_ok']:raise SystemExit('No source returned links: diagnostic website artifact retained; do not treat this as success.')
  publish:
    needs: update
    if: ${{ always() && needs.update.outputs.publish_ready == 'true' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    steps:
      - name: Publish the website
        id: deploy
        uses: actions/deploy-pages@v4
'''.replace('__INSTALLER__',textwrap.indent(installer.rstrip(),'          '))
path=R/'.github/workflows/daily.yml';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(workflow);(R.parent/'daily.yml').write_text(workflow)
print(json.dumps(dict(embedded_files=len(files),embedded_zip_bytes=len(payload),embedded_zip_sha256=sha,workflow_bytes=len(workflow.encode()),workflow_sha256=hashlib.sha256(workflow.encode()).hexdigest()),indent=2))
