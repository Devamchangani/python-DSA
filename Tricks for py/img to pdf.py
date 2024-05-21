from fpdf import FPDF
pdf = FPDF()


image = "" # Image path
pdf.add_page()
pdf.image(image,x,y,w,h)
pdf.output("file.pdf", "F")