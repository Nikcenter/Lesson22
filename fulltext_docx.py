from docx import Document

def get_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

text = get_text_from_docx('dogovir.docx')
print(text)
