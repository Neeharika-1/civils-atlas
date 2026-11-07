# Edition 14 QA scope

- Structural validator: 965 notes, 583 references, 570 question schemas PASS.
- Export checks: 19 monthly volumes, note IDs, question sections, eight Mains headings each, OOXML integrity and nonblank PDF pages PASS.
- Question-pagination check: all 570 questions have final option on their starting question page.
- App regression: all 19 months, year-aware practice/documents, bookmarks, search/priority/AP filters, 18 journeys, linked-note navigation, relative links, 23-month ledger and no JS errors PASS.
- July visual samples inspected: retrospective EC, NiVU, AP CPI and MCQ page. MCQ joined words were found, corrected explicitly, rebuilt, retested and the final MCQ page inspected again.
- Six local HTTP routes returned 200. Server binds to 0.0.0.0; daily scheduler remains inactive.
- These checks do NOT independently certify facts, current law, completeness, every PDF page's appearance or real-world implementation.
