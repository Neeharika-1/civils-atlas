# Daily setup · current method

Use **[DAILY-WEBSITE.md](DAILY-WEBSITE.md)**. It supersedes the previous Codespaces and separate-patch-ZIP instructions.

The latest `.github/workflows/daily.yml` is self-contained: it installs a checksum-verified embedded update, preserves old note objects, adds the Edition 19 research delta, collects permitted links, extracts/OCRs eligible primary PDFs, rebuilds and publishes Pages.

Only two account-side actions are needed: select **GitHub Actions** as the Pages source and replace the existing workflow file with the supplied latest `daily.yml`. Confirm the **update** and **publish** jobs, actual website URL and, later, a genuine **schedule** event. Never send credentials to this chat.

Daily time: **06:30 IST**, with possible GitHub delays. Link discovery, primary text extraction, editorial research, source utilisation and full-coverage audits are distinct checks. All-source automatic verified-note authoring is not achieved or promised.
