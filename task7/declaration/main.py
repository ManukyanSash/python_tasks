import PyPDF2

def read_from_pdf(filename):
    pdfFileObj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdfFileObj)
    page_obj = pdf_reader.pages[3]
    page_text = page_obj.extract_text()
    page_obj = pdf_reader.pages[4]
    page_text += page_obj.extract_text()
    pdfFileObj.close()
    return page_text

def to_dict(text):
    state_to_name_dict = dict()
    text_list = text[540::].split('[Column')
    for text in text_list[1:]:
        state_to_name_dict[text.split(":")[0][4:]] = text.split(":")[1].replace("\n", "").strip().replace("  ", ",")             
    print(state_to_name_dict)
    
    
if __name__ == "__main__":
    text = read_from_pdf("US_Declaration.pdf")
    to_dict(text)