from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('images.png', w=144, h=349)
pdf.set_font(family='Times', style='', size=24)
pdf.cell(w=0, h=50, txt="Amity Blight", align='C')

pdf.output('PDF-TESTE.pdf')
