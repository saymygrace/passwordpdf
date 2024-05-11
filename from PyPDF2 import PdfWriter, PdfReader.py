from PyPDF2 import PdfWriter, PdfReader
import getpass

# PdfWriter sınıfından bir örnek oluşturun
pdfwriter = PdfWriter()

# PdfReader sınıfını kullanarak belirtilen PDF dosyasını okuyun
pdf = PdfReader("yourpdf.pdf")

# Okunan PDF dosyasının her bir sayfasını PdfWriter örneği üzerine ekleyin
for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])

# Kullanıcıdan bir şifre alın
password = getpass.getpass(prompt='Enter Password: ')

# PdfWriter nesnesini kullanarak PDF dosyasını verilen şifre ile şifreleyin
pdfwriter.encrypt(password)

# Son olarak, şifrelenmiş PDF dosyasını belirtilen dosya yoluna kaydedin
with open('ho.pdf', 'wb') as f:
    pdfwriter.write(f)
