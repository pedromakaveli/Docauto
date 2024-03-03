from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

document = Document("file.docx")
paragraph = document.paragraphs[0]
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

alunos = [
    'Put the names here'
]

for aluno in alunos:
    paragraph.text = aluno
    for run in paragraph.runs:
        run.font.name = 'Arial'
        run.font.size = Pt(20)
    document.save(aluno + '.docx')