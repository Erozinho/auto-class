from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('images.png', w=72, h=174.5)
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Amity Blight", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt="Biografia", ln=1)

pdf.set_font(family='Times', size=14)
text1 = """Amity Blight é uma personagem fictícia da série animada "The Owl House", criada por Dana Terrace. A série, que estreou no Disney Channel em janeiro de 2020, rapidamente ganhou popularidade por sua representação diversificada de personagens e temas de inclusão.\n

Amity é apresentada como uma bruxa adolescente talentosa e uma estudante exemplar da Hexside School of Magic and Demonics, a escola de magia do mundo fictício da Ilha dos Demônios. Inicialmente, ela é retratada como uma antagonista para a protagonista, Luz Noceda, uma humana que acidentalmente se encontra no mundo mágico e deseja se tornar uma bruxa. Amity é conhecida por sua excelência acadêmica, cabelos tingidos de roxo, e atitude inicialmente arrogante e competitiva.

À medida que a série avança, Amity experimenta um desenvolvimento significativo de personagem. Sua relação com Luz evolui de rivalidade para amizade e eventualmente para um romance, marcando um dos aspectos mais celebrados da série por sua representação positiva de um relacionamento LGBTQ+. Amity é mostrada lutando com as expectativas de sua família conservadora, especialmente sua mãe, Odalia Blight, que exerce pressão sobre ela para se destacar e despreza aqueles que considera inferiores, incluindo Luz no início.\n"""
pdf.multi_cell(w=0, h=20, txt=text1)

pdf.output('PDF-TESTE.pdf')
