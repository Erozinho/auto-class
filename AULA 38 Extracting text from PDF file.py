import fitz

with fitz.open("PDF-TESTE.pdf") as pdf:
    page1 = pdf[0].get_text()
    print(page1)
    for page in pdf:
        pass
        # print(page.get_text())
