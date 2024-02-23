from fpdf import FPDF
import pandas as pd

wb = pd.read_excel('auto-class\\data.xlsx')

for index, row, in wb.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)

    for column in wb.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=15, txt=f'{column.title()}')

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=15, txt=row[column], align='C', ln=1)

    pdf.output(f'{row['name']}.pdf')
