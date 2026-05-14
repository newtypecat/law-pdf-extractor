# Local Tax Law PDF Analyzer

> Automated extraction and structuring of Japanese legal documents using Python and PyMuPDF — no external APIs or AI services required.

---

## Overview

This tool parses the **Japanese Local Tax Act (地方税法)** — a 797-page legal document — and automatically extracts its hierarchical structure (chapters, sections, subsections, and articles) into a clean, readable text file.

Built for legal professionals, government officers, and researchers who need to navigate large Japanese statutes quickly, this project demonstrates how document intelligence can be achieved through pure PDF analysis without relying on paid AI APIs.

**Key result:** 5,216 key points extracted from 797 pages in seconds.

---

## Features

- Extracts document structure based on font-size analysis and regex pattern matching
- Recognizes Japanese legal hierarchy: 章 (Chapter) → 節 (Section) → 款 (Subsection) → 目 (Article group)
- Outputs indented, symbol-prefixed bullet points with page number references
- Works entirely offline — no API keys, no internet connection required
- UTF-8 encoded output for full Japanese text support

---

## Technologies

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core scripting language |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | PDF parsing and font-size analysis |
| Regex (`re`) | Japanese legal heading pattern matching |

---

## Installation

```bash
pip install pymupdf
```

No other dependencies required.

---

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/local-tax-law-analyzer.git
cd local-tax-law-analyzer
```

2. Place your PDF file in the project directory and update the path in `summarize_pdf.py`:

```python
PDF_PATH = r"path/to/your/document.pdf"
OUTPUT_PATH = r"path/to/output.txt"
```

3. Run the script:

```bash
python summarize_pdf.py
```

4. Open the generated `.txt` file. Output format:

```
============================================================
地方税法　要点（目次・構造）
総ページ数: 797
============================================================

■ 第一章　総則  （p.1）
  ◆ 第一節　通則（第一条―第八条の五）  （p.1）
  ◆ 第二節　納税義務の承継（第九条―第九条の四）  （p.1）
    ▶ 第一款　更正、決定等の期間制限（第十七条の五・第十七条の六）  （p.1）
      ・ 第一目　課税標準及び税率（第三十二条―第三十八条）  （p.1）
```

---

## Results

| Metric | Value |
|---|---|
| Document | Japanese Local Tax Act (地方税法) |
| Total pages | 797 |
| Key points extracted | 5,216 |
| Processing time | < 30 seconds |
| External API calls | 0 |

---

## Use Cases

- **Legal research:** Quickly navigate large Japanese statutes without reading every page
- **Government digitization:** Convert legacy PDF documents into structured data
- **Compliance work:** Map tax regulations to specific articles for audit or advisory purposes
- **Document intelligence:** Foundation for further NLP or AI-based analysis pipelines

---

## About the Author

I am a Japan-based IT consultant with a background that bridges **public administration, tax law, and software development**.

### Professional Background

- **11 years** at a local government office in Japan, specializing in:
  - Municipal taxation (地方税務) — assessment, collection, and dispute resolution
  - Legal affairs and ordinance drafting
  - Administrative procedures and citizen services
  - Currently working as an **IT consultant**, applying domain knowledge in law and finance to build practical automation tools

### Why This Project

Having personally worked with the Local Tax Act for years in a professional capacity, I understand how time-consuming it is to locate specific provisions within a dense, multi-hundred-page statute. This tool was born out of that firsthand experience — built to solve a real problem I encountered in government work.

This combination of **deep domain expertise in Japanese tax law** and **hands-on software development** allows me to deliver solutions that are not just technically sound, but practically useful to real-world legal and compliance workflows.

---

## Potential Extensions

- [ ] Support for other Japanese statutes (National Tax Act, Civil Code, etc.)
- [ ] Export to JSON or CSV for database integration
- [ ] Keyword search across extracted structure
- [ ] Claude API integration for AI-powered summarization of individual articles

---

## License

MIT License — free to use, modify, and distribute.

---

*For freelance inquiries or collaboration, feel free to reach out via [Upwork](https://www.upwork.com).*
