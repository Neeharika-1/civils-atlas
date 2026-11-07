# Activate daily updates · GitHub Actions

**Prepared and locally tested; NOT yet deployed or activated for your account.** You chose GitHub Actions. A repository URL and account-side setup are still needed. This session has no supported GitHub connector and has not created a repository, pushed files, enabled Actions or observed a hosted scheduled run. Never share a password or access token in chat.

## What runs automatically

At **06:30 India time** (`0 1 * * *` UTC), the workflow attempts source-link discovery, deduplicates URLs, refreshes the unreviewed inbox, records source health/history and rebuilds the app/documents. It commits results back to the default branch. GitHub may delay or skip a scheduled run; this is not an exact-time guarantee.

**It does not independently read articles, write verified study notes, resolve omissions or create an editorially reviewed daily PDF.** Research and approval remain necessary. Existing note counts must not be presented as new content merely because the app was rebuilt. No paid AI service or API key is configured.

## 1. Create an empty repository

Create a repository named, for example, `civils-atlas` in your GitHub account. Public or private is your choice; GitHub Actions quotas and Pages eligibility depend on the account/plan. Do not initialise a second README if using the commands below. Send the repository URL so the deployment instructions can be matched to it.

## 2. Upload the package contents at the repository root

Extract the new package, then open its **Civils-Atlas** folder. The repository root must contain `index.html`, `data`, `scripts`, `volumes`, `research` and **`.github/workflows/daily.yml`**. Do not wrap them in an extra nested `Civils-Atlas` directory in the repository.

Using Git on your computer (replace the example URL with your actual repository):

```bash
cd /path/to/extracted/Civils-Atlas
git init
git branch -M main
git add .
git commit -m "Publish Civils Atlas study library and daily discovery"
git remote add origin https://github.com/YOUR-ACCOUNT/civils-atlas.git
git push -u origin main
```

Authenticate through GitHub’s normal browser/credential-manager flow. The `.gitignore` excludes dependencies, local QA files, environment secrets and ZIPs. It does not exclude `.github` workflows. If uploading through the web interface, ensure hidden `.github` files are included.

## 3. Allow Actions to save updates

In the repository, open **Settings → Actions → General**:
- Enable GitHub Actions as allowed by your account/organisation policy.
- Under **Workflow permissions**, allow **Read and write permissions**.
- Save. The workflow already requests `contents: write`; account policy and branch protection may still prevent direct pushes.

If the default branch requires pull requests or blocks the Actions bot, do not disable important safeguards casually. Use an authorised update branch/PR design instead; that adaptation has not been deployed here.

## 4. Run the first hosted test

Open **Actions → Daily source discovery → Run workflow** on the default branch. Review:
- The run’s job summary and downloadable `source-health` artifact.
- `data/automation-status.json`, `data/update-log.json`, `data/update-history.json`.
- A bot commit updating the inbox/app and logs.

A **manual** hosted run proves that dispatch worked, not that a daily schedule has already executed. The app says scheduling is observed only after an actual `schedule` event runs and writes `last_observed_scheduled_run`.

Local test on **7 November 2026**: **5/8 sources returned links**. The Hindu national/AP, PRS 2025/2026 and ISRO worked. PIB daily and ministry-review pages returned 403; Indian Express’s robots check returned 403 and was conservatively skipped. Results can differ from GitHub’s network. Access controls are not bypassed. Source failures are deliberately visible and cause a red run after queue/log persistence; a red source-health result does not mean every successful source was discarded.

If dependency, validation, build or push itself fails, inspect the failed step: a full rebuilt commit may not exist. Artifacts are attempted even on failure.

## 5. Verify daily scheduling

After the next eligible 06:30 IST window, check for a run whose event is **schedule**, inspect its commit and the status file. The system records scheduled execution separately from source success. A scheduled run may execute while individual collectors still fail.

Keep Actions failure notifications enabled in your GitHub notification settings. Scheduled workflows run from the default branch; inactive public repositories may have their schedules disabled by GitHub, and quotas/account policies can also affect execution. Check the Actions UI rather than assuming perpetual operation.

## 6. Optional: publish the study website

Repository updates alone do not automatically publish a website.
1. **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. **Settings → Secrets and variables → Actions → Variables**: create `PUBLISH_PAGES` with value `true`.
3. Run **Actions → Publish study website → Run workflow** once.
4. Open the URL shown in the deployment or repository Pages settings.

The Pages workflow also runs after daily discovery completes, including a partial-source failure, so the published app can show current source-health notices. It checks out the latest default branch, not an old pre-update commit. The Actions token’s own commits do not trigger ordinary push workflows; the explicit `workflow_run` trigger handles that case.

The published website contains the original study material, registered references and unreviewed source metadata. Check that you want these public before enabling Pages. Do not add private documents or credentials. Pages availability/visibility depends on your plan and repository settings.

## 7. Daily editorial use

Open **Update desk** in the app. Filter the queue, inspect sources and dates, check primary instruments and AP relevance, then write original referenced notes. Review duplicate events, legal commencement, targets versus outcomes and conflicting figures before publishing. Daily discovery is a research aid, not completeness or factual certification.

## Files
- `.github/workflows/daily.yml` — daily discovery, validation, rebuild, persistence and visible failures.
- `.github/workflows/pages.yml` — optional original-material website publication.
- `scripts/update.py` — conservative collector, deduplication, status and 365-run history.
- `scripts/reconcile.py` — count refresh preserving manually recorded evidence/audit disclosures.
- `scripts/test_daily.py` — five offline unit checks; not a hosted-run test.
- `research/edition-18-automation-checks.json` — actual local test scope/results.

**Current activation status: repository deployment and first hosted scheduled run still pending.**
