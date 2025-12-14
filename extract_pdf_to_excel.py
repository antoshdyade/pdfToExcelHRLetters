import pdfplumber
import pandas as pd
import os
import re

PDF_FOLDER = "pdfs"
OUTPUT_FILE = "LOI_Data.xlsx"

data = []

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
    return full_text


for file_name in os.listdir(PDF_FOLDER):
    if file_name.endswith(".pdf"):
        pdf_path = os.path.join(PDF_FOLDER, file_name)
        text = extract_text_from_pdf(pdf_path)

        name = re.search(r"Dear\s+(.*)", text)
        loi_date = re.search(r"Date:\s+(.*)", text)
        stipend = re.search(r"stipend of\s+([\d,]+)", text)
        reporting_date = re.search(r"Expected Reporting Date is:\s+(.*)", text)
        recruiter = re.search(r"Recruiter Name:\s+(.*)", text)
        mobile = re.search(r"Mobile Number:\s+(\d+)", text)
        id_number = re.search(r"Id Number:-\s*(\w+)", text)
        location = re.search(r"Your Location of Joining will be:\s+(.*)", text)

        # ✅ NEW: Client Company extraction
        client_company = re.search(
            r"client company\s+([A-Za-z0-9\s–\-]+)",
            text,
            re.IGNORECASE
        )

        data.append({
            "Candidate Name": name.group(1).strip() if name else "",
            "LOI Date": loi_date.group(1).strip() if loi_date else "",
            "Client Company": client_company.group(1).strip() if client_company else "",
            "Stipend": stipend.group(1) if stipend else "",
            "Reporting Date": reporting_date.group(1).strip() if reporting_date else "",
            "Joining Location": location.group(1).strip() if location else "",
            "Recruiter Name": recruiter.group(1).strip() if recruiter else "",
            "Recruiter Mobile": mobile.group(1) if mobile else "",
            "ID Number": id_number.group(1) if id_number else "",
            "PDF File": file_name
        })

df = pd.DataFrame(data)
df.to_excel(OUTPUT_FILE, index=False)

print("✅ Data extraction completed. Excel file created:", OUTPUT_FILE)
