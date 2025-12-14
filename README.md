# 📄 PDF to Excel Data Extractor (Python)

This project extracts structured data from **multiple PDF files** (such as Letter of Intent / Offer Letters)
and stores the extracted information into a **single Excel file** automatically.

It is useful when handling **large numbers of similar-format PDFs** and avoids manual data entry.

---

## 🚀 Features

- Extracts data from multiple PDFs at once
- Supports text-based PDF files
- Generates Excel (.xlsx) output
- Easy to customize and extend
- Lightweight and fast execution

---

## 📁 Project Structure
PDF_TO_EXCEL/
│
├── pdfs/
│   ├── file1.pdf
│   ├── file2.pdf
│   ├── AnyName.pdf
│   └── many_more_files.pdf
│
├── extract_pdf_to_excel.py


1️⃣ Install Python (if not installed)

Download from:
👉 https://www.python.org/downloads/
✔ Tick “Add Python to PATH” during installation.

2️⃣ Install Required Python Libraries
Open Command Prompt (Windows) or Terminal and run:

pip install pdfplumber pandas openpyxl

3️⃣ Run the script:

python extract_pdf_to_excel.py

📊 Output

After execution, you will get:

LOI_Data.xlsx

Excel sheet will contain rows like:

Candidate Name	LOI Date	Stipend	Reporting Date	ID Number	PDF File

