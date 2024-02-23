import fitz

with fitz.open("PDF-TESTE.pdf") as pdf:
    for page in pdf:
        print(page.get_text())
