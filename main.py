import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    # stem is a method that returns the file name
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-") #Unpack the values

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{date}")


    pdf.output(f"PDFs/{filename}.pdf")

    # print(df)
