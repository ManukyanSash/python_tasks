import PyPDF2

def read_from_pdf(filename):
    pdfFileObj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdfFileObj)
    page_obj = pdf_reader.pages[1]
    page_text = page_obj.extract_text()
    pdfFileObj.close()
    return page_text

def write_into_txt(filename, text):
    text = text.replace("AUTHORS:", "First_Name Last_Name, Title, Extension, EmailAUTHORS:")
    with open(filename, 'w') as file:
        file.write(text)
        
if __name__ == "__main__":
    pdf_text = read_from_pdf("Business_Proposal.pdf")        
    write_into_txt("contacts.txt", pdf_text)