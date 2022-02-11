import json

from fpdf import FPDF

with open("data.json","r") as f:
    mira=json.loads(f.read())


pdf = FPDF()
pdf.add_page()

pdf.set_auto_page_break
pdf.image('picture.jpg', x=160, y=9, w=38, h=38, type= '', link='')
pdf.set_font("Arial", "B", size= 17)
pdf.cell(200, 2, txt =mira ["data"][0]["FullName"], ln=1)
pdf.cell(200, 9, txt =mira ["data"][0]["Email"], ln=1)
pdf.cell(200, 2, txt =mira ["data"][0]["Address"], ln=1)
pdf.set_font("Arial", "I", size= 14)
pdf.cell(200, 9, txt =mira ["data"][0]["ContactNumber"], ln=1)
pdf.set_font("Arial", "B", size= 14)
pdf.cell(200, 10,txt = "Educational Attainment", ln=1,align="C")
pdf.set_font("Arial", "", size= 14)
pdf.cell(200, 10, txt =mira ["data"][0]["ElementarySchool"], ln=1)
pdf.cell(200, 4, txt =mira ["data"][0]["HighSchool"], ln=1)
pdf.cell(200, 10, txt =mira ["data"][0]["SeniorHighSchool"], ln=1)
pdf.cell(200, 6, txt =mira ["data"][0]["College"], ln=1)
pdf.set_font("Arial", "B", size= 14)
pdf.cell(200, 10,txt = "Achievements", ln=1,align="C")
pdf.set_font("Arial", "", size= 14)
pdf.cell(200, 10, txt =mira ["data"][0]["Achievements1"], ln=1,align="C")
pdf.cell(200, 10, txt =mira ["data"][0]["Achievements2"], ln=1,align="C")
pdf.set_font("Arial", "B", size= 14)
pdf.cell(200, 10,txt = "Experiences", ln=1,align="C")
pdf.set_font("Arial", "", size= 14)
pdf.multi_cell(200, 10, txt =mira ["data"][0]["Experiences"], )
pdf.set_font("Arial", "B", size= 14)
pdf.cell(200, 10,txt = "Summary", ln=1,align="C")
pdf.set_font("Arial", "", size= 14)
pdf.multi_cell(200, 10, txt =mira ["data"][0]["Summary"], )
pdf.output("Gonzales_JohnLouie.pdf")
