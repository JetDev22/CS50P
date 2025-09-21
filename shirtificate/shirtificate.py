from fpdf import FPDF

name = input("Name: ")
banner = f"{name} took CS50"
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=40)
pdf.text(50, 30, "CS50 Shirtificate")
pdf.image("shirtificate.png", x=0, y=50)
pdf.set_font("helvetica", style="B", size=25)
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 220, banner, align="C")
pdf.output("shirtificate.pdf")
