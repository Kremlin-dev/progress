import fitz

src_pdf_filename = './InternshipLetter.pdf'
dst_pdf_filename = './InternshipLetter.pdf' 
img_filename = './download (2).png'

img_rect = fitz.Rect(50, 180, 200, 1050)

document = fitz.open(src_pdf_filename)

page = document[0]
page.insert_image(img_rect, filename=img_filename)

document.saveIncr()

document.close()
