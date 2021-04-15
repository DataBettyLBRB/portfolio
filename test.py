import PyPDF2

if __name__ == "__main__":
    path = 'static/resumes/Chitty_Developer_Resume_2021.pdf'

    pdf = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)

    print(pdfReader.numPages)