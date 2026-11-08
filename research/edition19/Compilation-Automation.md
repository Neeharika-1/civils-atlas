# Public compilations · daily reading automation

Added at the user's request on 7 November 2026. The user explicitly accepts PIB digests and newspaper compilations as coverage fallbacks and supplied First Principles IAS.

## Live local access test

All **six** compilation streams returned relevant links, producing **61 unique newly indexed URLs** after deduplication. These are reading links, not 61 newly authored or independently verified notes.

| Stream | Relevant entries returned | Use |
|---|---:|---|
| First Principles IAS topic archive | 22 | Subject-wise revision; default September 2026 |
| Legacy IAS daily current affairs RSS | 7 | Newspaper-based daily reading and related digests |
| Insights IAS RSS | 2 | Matching current-affairs/PIB/editorial/compilation entries |
| ForumIAS 9 PM monthly tag archive | 10 | Historical newspaper compilations; inspect edition dates |
| Legacy IAS daily PIB summaries | 1 | PIB-digest discovery |
| Legacy IAS monthly PIB compilations | 20 | Historical monthly PIB reading |

The entries sum to 62, with one overlapping URL, hence 61 unique new URLs. Feed counts are dated observations, not guaranteed future counts or coverage-completeness percentages.

First Principles IAS currently displays June–September 2026 coverage and September as its default/latest visible edition. Its HTML discovery returned 22 topic leads from the default page, not verified comprehensive extraction of all four months. It is not labelled as a November daily feed. The ForumIAS tag archive is historical, not a claim that the latest monthly issue is present. The initially guessed Legacy category route returned 404; it was replaced with the actual public daily/monthly navigation links extracted from its homepage.

## Implementation

- `data/compilation-registry.json`: six supplementary providers, distinct from the 18 original obligations.
- `scripts/update_compilations.py`: shared robots/TLS-respecting collector, relevant RSS filtering, URL deduplication and explicit secondary provenance. Uses public metadata only, no source full-text republication.
- `data/compilation-health.json`: separate per-provider results, actual counts and timestamp.
- `research/Compilation-Reading-Desk.md`: automatically regenerated linked reading list.
- Daily home: dedicated compilation desk with provider links, archive-date cautions and buttons to filter collected articles by source.
- Both builders embed the new data. The daily workflow invokes collection before rebuilding/publishing the dashboard and retains compilation diagnostics.

An alternate digest fills a reading/coverage gap; it does not mean the underlying newspaper or original PIB endpoint was accessed. Original obligations remain visible. Article/edition dates differ from discovery timestamps, and none of these links is automatically promoted into the researched-note library. Core facts used in future original notes require appropriate corroboration and clear evidence limits.

## Deployment status

The original Edition 19 website was confirmed live earlier. This compilation-enabled replacement is **locally implemented/tested**, not yet confirmed on GitHub. Replace the existing `.github/workflows/daily.yml` with the newly supplied self-contained file. No Pages-setting change, separate ZIP upload, account token, Codespace or publisher subscription is needed for the tested public routes.

Once successfully installed and published, the existing 06:30 IST scheduled workflow will also collect these compilations. GitHub scheduling and publishers can change or fail; a first scheduled run still requires actual observation. No flawless-service, complete daily-source coverage or unattended verified-note-authoring guarantee is made.
