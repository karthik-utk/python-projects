import fitz  


def read_pdf(path):
    
    doc = fitz.open(path)
    pdf_content = ''

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        pdf_content += text
        

    doc.close()
    return pdf_content


text = read_pdf("example.pdf")
print(text)
print(len(text))