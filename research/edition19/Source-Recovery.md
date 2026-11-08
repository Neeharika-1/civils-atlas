# Source recovery · 7 November 2026

## What was actually tested

The enhanced collector made **37 route attempts across all 18 required source streams**. The separate candidate probe checked 20 additional official-host routes. TLS validation and robots checks remained enabled; redirects still receive independent policy checks.

**Result: six streams returned links; one additional stream has an accessible interactive portal; eleven remain blocked/unresolved.** This is not 18/18 automatic working sources.

- Working discovery streams: The Hindu national and Andhra Pradesh feeds, PRS 2025 and 2026 review listings, ISRO, AP Finance.
- Supreme Court: the original route is inaccessible to the collector, but **https://scr.sci.gov.in/** responded as an interactive official portal. Recorded as **manual review required**, not successful judgment extraction or source utilisation.
- PIB daily/year reviews, Indian Express India/Explained, Vision daily/monthly, AP IPR, AP orders, APPSC, RBI and Gazette remain unresolved for unattended collection. Candidate domains/paths did not remove DNS, certificate, robots or service failures in this environment.

Evidence: `source-route-probes.json`, `source-recovery-sweep.json`, `source-recovery-policy-tests.log`. Public-index probes are recorded separately: Google News and Bing web-search robots policies disallowed the tested automated routes; the tested Bing News RSS route produced no matching items. None was installed as a false successful fallback.

## Improvements implemented

1. Retained all 18 obligations and installed additional independently checked official-host candidate routes. These are candidates, not guarantees of active/current pages.
2. Added a browser-only source-domain search for **every** source card. These links are never requested by the collector and never count as successful source access or verified reading.
3. Exposed candidate routes on each relevant source card, so the user can try their browser if GitHub-hosted collection fails.
4. Recorded the actual selected route and accessible-portal state even when document retrieval remains manual. Portal reachability does not turn the source green.
5. Fixed stale hidden month-navigation counts (November 35; AP backfill months updated).
6. Added tests that a reachable fallback portal remains manual and that a manual search link never promotes a failed source to success.

The APPSC alternate domain was identified through the commission's own FAQ at https://portal-psc.ap.gov.in/HomePages/Faqs. Vision's public legacy resource links were checked as candidate routes alongside its current archives. Search-result snippets were endpoint leads only, not evidence of article reading or legal facts.

## Installation and remaining limits

The previously deployed Edition 19 website is live. **This newer source-recovery replacement has not been deployed or tested on GitHub yet.** Replace the existing `.github/workflows/daily.yml` with the newly supplied file. The Pages setting does not need to be repeated.

The updated workflow embeds its own code, template and registry. It uses the same first-install rebuild/scheduled fast-update design. Updated installer/merge/dashboard checks are separate from the earlier full baseline workflow simulation; neither is a guarantee of publisher access from GitHub.

No proxy rotation, identity spoofing, CAPTCHA/paywall bypass, disabled TLS verification or robots bypass was installed. Public source availability is controlled by publishers and government services; universal automatic access cannot honestly be guaranteed. Where a source is inaccessible, use the original source in a normal browser if available, or supply legitimately obtained source files for a separate research update. A different publisher covering the event does not fulfil the inaccessible publisher's utilisation requirement.

## Robots-standard correction · subsequent test

Inspected RFC 9309 section 2.3.1.3 at https://www.rfc-editor.org/rfc/rfc9309.html#section-2.3.1.3. The earlier collector incorrectly treated a robots-resource 403 as equivalent to a Disallow rule. Corrected the shared handler: unavailable robots 4xx responses may permit an ordinary public-resource request; 401/429, server/network failures, explicit Disallow rules, actual resource denials and certificate errors still stop collection. No identity spoofing or denial bypass is attempted. Twelve policy/parser tests pass.

A full 18-source probe and subsequent collector run confirmed **no increase in automatic source access**: the affected PIB/Indian Express pages themselves return 403; RBI resources return 418; other unresolved services retain their network/certificate/server failures. The distinction fixes diagnostic correctness, not external availability. Six streams still return links; the Supreme Court alternate portal remains manual. The correction is local; deployed code has not been changed. No flawless/all-source outcome is claimed.
