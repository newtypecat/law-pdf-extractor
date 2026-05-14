import pymupdf
import re
from pathlib import Path

PDF_PATH = r"C:\Users\ryu04\OneDrive\デスクトップ\地方税法.pdf"
OUTPUT_PATH = r"C:\Users\ryu04\地方税法_要点.txt"

doc = pymupdf.open(PDF_PATH)
total_pages = len(doc)
print(f"ページ数: {total_pages}")

# フォントサイズ別にテキストブロックを収集
headings = []   # 大きいフォントの見出し
body_lines = [] # 本文行

for page_num, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            line_text = ""
            max_size = 0
            for span in line.get("spans", []):
                line_text += span.get("text", "")
                max_size = max(max_size, span.get("size", 0))
            line_text = line_text.strip()
            if not line_text:
                continue
            body_lines.append((page_num + 1, max_size, line_text))

doc.close()

# フォントサイズの分布を確認して見出し閾値を決定
sizes = [s for _, s, _ in body_lines]
if sizes:
    size_max = max(sizes)
    size_avg = sum(sizes) / len(sizes)
    heading_threshold = size_avg * 1.15
else:
    heading_threshold = 10.0

print(f"フォントサイズ: 最大={size_max:.1f}, 平均={size_avg:.1f}, 見出し閾値={heading_threshold:.1f}")

# 見出しパターン（法律文書向け）
HEADING_PATTERNS = [
    re.compile(r"^第[一二三四五六七八九十百千\d]+章"),   # 第○章
    re.compile(r"^第[一二三四五六七八九十百千\d]+節"),   # 第○節
    re.compile(r"^第[一二三四五六七八九十百千\d]+款"),   # 第○款
    re.compile(r"^第[一二三四五六七八九十百千\d]+目"),   # 第○目
    re.compile(r"^第[一二三四五六七八九十百千\d]+条"),   # 第○条（見出し）
    re.compile(r"^附則"),
    re.compile(r"^別表"),
]

def is_heading(size, text):
    if size >= heading_threshold and len(text) < 80:
        return True
    for pat in HEADING_PATTERNS:
        if pat.match(text):
            return True
    return False

# 見出し・要点を抽出
key_points = []
seen = set()

for page_num, size, text in body_lines:
    if is_heading(size, text) and text not in seen:
        seen.add(text)
        # インデントレベルを判定
        if re.match(r"^第[一二三四五六七八九十百千\d]+章", text):
            indent = ""
            prefix = "■"
        elif re.match(r"^第[一二三四五六七八九十百千\d]+節", text):
            indent = "  "
            prefix = "◆"
        elif re.match(r"^第[一二三四五六七八九十百千\d]+款", text):
            indent = "    "
            prefix = "▶"
        elif re.match(r"^第[一二三四五六七八九十百千\d]+目", text):
            indent = "      "
            prefix = "・"
        elif re.match(r"^附則|^別表", text):
            indent = ""
            prefix = "■"
        else:
            indent = "  "
            prefix = "◆"
        key_points.append(f"{indent}{prefix} {text}  （p.{page_num}）")

print(f"抽出した要点: {len(key_points)} 件")

# テキストファイルに出力
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write("地方税法　要点（目次・構造）\n")
    f.write(f"総ページ数: {total_pages}\n")
    f.write("=" * 60 + "\n\n")
    for point in key_points:
        f.write(point + "\n")

print(f"\n出力完了: {OUTPUT_PATH}")
