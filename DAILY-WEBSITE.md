# Civils Atlas · one daily website

## Install the latest self-contained workflow — no ZIP upload

The separately supplied **daily.yml** contains the small, checksum-verified code upgrade and Edition 19 research delta. You do not need Codespaces, a terminal, another project upload, a password or a token.

1. In your repository, choose **Settings → Pages → Build and deployment → Source → GitHub Actions**.
2. Open the existing **.github/workflows/** folder. Choose **Add file → Upload files**, upload the latest **daily.yml** with that exact filename, replacing the old file, and commit. If your browser saved it as `daily (1).yml`, rename it before uploading. Alternatively edit the existing workflow and replace its contents. Do not place it at the repository root or create a second workflow.

The original study project must already be imported, as verified for your repository. This update installs its embedded patch, merges only new research IDs (preserving existing edited note IDs), runs the collector and primary-document intake, builds all study exports once, then publishes the website. Later runs use the faster dashboard-only build and do not rewrite researched notes from unreviewed feeds.

Open **Actions → Daily source discovery**. Both **update** and **publish** should succeed. The publish step supplies the actual website URL; the expected address is `https://neeharika-1.github.io/civils-atlas/`. This is not a claim that the new deployment has already happened. If Pages is not enabled, revisit step 1. Branch protection or account policies may block a bot commit; inspect the specific failed step rather than repeatedly uploading the project.

The previous small ZIP+workflow installation instructions are superseded by this single-file method. Keep the repository public for this simple Pages setup; the study notes and discovery metadata will be public. No private documents, account credentials, publisher full text or API keys should be uploaded.

## Daily use

Bookmark the published website, not GitHub's raw HTML source view.

- **Daily home:** last sweep, source health, researched update, primary PDFs and unreviewed links.
- **New researched update:** 14 new notes, a PDF/Word supplement, 14 original MCQs and four Mains frameworks.
- **Read & revise:** search/source filters and personal “Mark read”. These links are not verified new study notes.
- **Latest researched notes / AP-linked notes / All study notes:** easy routes into the full library.
- **Every required source:** 18 tracked obligations remain visible even when inaccessible. Green means links returned, not a fully read or utilised publisher.
- **Personal source checks:** stored on this device only; reset by IST date. They do not constitute a centrally verified source audit.
- **Primary-document intake:** checks source hashes, extracts text, applies English OCR to eligible scans, and flags changed cited versions. Date candidates are not legal commencement dates.
- **Refresh saved dashboard:** reloads the published snapshot; it does not itself start collection. **Check daily run** opens Actions, where a manual run is possible.

Automatic discovery/intake/publication is scheduled daily at **06:30 IST**. GitHub can delay execution. A scheduled event must actually be observed before the dashboard claims one. You do not have to download the website again to see successfully published link/document updates.

## Evidence and limits

Research edition 19: **1,192 notes, 696 references, 690 monthly + 14 supplementary MCQs, 184 monthly + four supplementary Mains frameworks, 23 selected period volumes**. Ten new November notes bring the first-week selection to 35; four earlier AP-document notes backfill March–May. Source bodies, original analysis, drafts, deadlines and unverified implementation claims are distinguished.

Local access test: **6/18** streams returned links. Primary intake: **four AP Finance PDFs / 11 pages** extracted, including OCR on two scanned pages. Source gaps remain unresolved, not discarded. Hosted expanded access, Pages deployment and first scheduled run still require verification after you apply this file.

Daily PDF intake is deliberately restricted to indexed original AP Finance PDFs: up to 12 documents per run, 10 MiB per download, 50 pages per document and eight OCR pages. Pending items rotate; external storage mirrors and other publishers are not silently claimed as read. TLS and robots checks are retained. OCR can make errors. Metadata and hashes are published, not full source text.

A green pipeline means installation/build/save/deploy worked, not that every publisher was accessed or utilised. Gaps appear in the dashboard, Actions summary and artifacts. Total source-discovery outage is reported after publishing diagnostic state.

The 14 new study notes were researched by the assistant in this session. There is no unattended fact-checking researcher or automatic verified-note authoring. The workflow does not bypass paywalls, access denials, CAPTCHAs or robots policies. All 23 historical source audits remain open; this is not full January 2025–November 2026 coverage or a current-law certificate.
