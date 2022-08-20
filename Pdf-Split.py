from PyPDF4 import PdfFileReader, PdfFileWriter
input_pdf = PdfFileReader(r'C:\Users\eminu\OneDrive\Bilder\ControlCenter4\Scan\19_Ergebnis.pdf')
pages = [0,2,4,6,8]
output = PdfFileWriter()
for page_num in pages:
    output.addPage(input_pdf.getPage(page_num))
with open(r"C:\Users\eminu\OneDrive\Bilder\ControlCenter4\Scan\19_Ergebnis2.pdf", 'wb') as output_stream:
    output.write(output_stream)
    output_stream.close()
    print(f'New Pdf-file {output_stream.name} created')    
