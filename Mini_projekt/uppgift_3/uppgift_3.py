# Writhing a word file bibliotek
from docx import Document
from docx.enum.text import WD_COLOR_INDEX
# Reading an excel file using Python bibliotek
import xlrd   
# importerar ch definerar tid
import datetime
dt = datetime.date.today()
# Give the location of the file 
loc = ("C://Users//s8gorgar//Desktop//prog//Python//Mini_projekt//uppgift_3//Bedömning_prog.xlsx")  # kan ändras beroende på positionen 
# För att välja vilken ska tas fram
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
sheet1 = wb.sheet_by_index(1)  
sheet2 = wb.sheet_by_index(2)  
sheet3 = wb.sheet_by_index(3)  
# variabler för klass,ämne och lärare
klass = sheet3.cell_value(2, 1)
larare = sheet3.cell_value(0, 1)
amne = sheet3.cell_value(1, 1)
# documenten funktion till variabel
document = Document()  
f = []  # array för alla elev numer
# elevens namn
elev = input("Ange elevens namn: ")
# for loop för att ta alla elever 
elever = []
for i in range(1, 30):     
    elever.append(sheet.cell_value(i,0))
# rubrik
document.add_heading(amne, 0)
# skriver ut klass och elevens namn
document.add_heading('Klass: '+ klass + "     " +  'Elev: '+ elev) 
# headers
document.add_heading('Centralt innehåll', level = 1)
# skriver i header
scetion = document.sections[0]
header = scetion.header
paragraph = header.paragraphs[0]
paragraph.text = larare + "          " + str(dt)
# information om ämnesbedömning
p1 = document.add_paragraph('')
p2 = document.add_paragraph('')
p3 = document.add_paragraph('')
p4 = document.add_paragraph('')
p5 = document.add_paragraph('')
p6 = document.add_paragraph('')
p7 = document.add_paragraph('')
p8 = document.add_paragraph('')
# elevens position från listan  med alla elever
i = elever.index(elev) + 1
# skriver under central inehållet 
if  sheet.cell_value(i, 1) == "Genomfört":  # om man har genomfört delen då blir den fet stil 
    p1.add_run('Grundläggande programmering i ett eller flera programspråk varav minst ett av språken är textbaserat.').bold = True
else:   # annars blir den vanlig text
    p1.add_run('Grundläggande programmering i ett eller flera programspråk varav minst ett av språken är textbaserat.')
if  sheet.cell_value(i, 2) == "Genomfört":    
    p2.add_run('Programmering och dess olika användningsområden ur ett socialt perspektiv inklusive genus, kultur och socioekonomisk bakgrund.').bold = True
else:
    p2.add_run('Programmering och dess olika användningsområden ur ett socialt perspektiv inklusive genus, kultur och socioekonomisk bakgrund.')
if  sheet.cell_value(i, 3) == "Genomfört":   
    p3.add_run('Programmeringens möjligheter och begränsningar utifrån datorns funktionssätt.').bold = True
else:
    p3.add_run('Programmeringens möjligheter och begränsningar utifrån datorns funktionssätt.')
if  sheet.cell_value(i, 4) == "Genomfört":    
    p4.add_run('Grundläggande kontrollstrukturer, konstruktioner och datatyper.').bold = True
else:
    p4.add_run('Grundläggande kontrollstrukturer, konstruktioner och datatyper.')
if  sheet.cell_value(i, 5) == "Genomfört":   
    p5.add_run('Arbetsmetoder för förebyggande av programmeringsfel, testning, felsökning och rättning av kod.').bold = True
else:
    p5.add_run('Arbetsmetoder för förebyggande av programmeringsfel, testning, felsökning och rättning av kod.')
if  sheet.cell_value(i, 6) == "Genomfört":    
    p6.add_run('Grundläggande datastrukturer och algoritmer.').bold = True
else:
    p6.add_run('Grundläggande datastrukturer och algoritmer.')
if  sheet.cell_value(i, 7) == "Genomfört":    
    p7.add_run('Gränssnitt för interaktion mellan program och användare.').bold = True
else:
    p7.add_run('Gränssnitt för interaktion mellan program och användare.')
if  sheet.cell_value(i, 8) == "Genomfört":   
    p8.add_run('Normer och värden inom programmering, till exempel läsbarhet, dokumentation, testbarhet, rena gränssnitt och nyttan av standard.').bold = True
else:
    p8.add_run('Normer och värden inom programmering, till exempel läsbarhet, dokumentation, testbarhet, rena gränssnitt och nyttan av standard.')
# kunskapskrav
document.add_heading('Kunskapskrav')
# skapar tabell
table = document.add_table(rows=11, cols=4)
hdr_cells = table.rows[0].cells # säter variabel för första raden i tabellet
ftr_cells = table.columns[0].cells  # säter variabel för första kolumnen i tabellet
ftr1_cells = table.columns[1].cells
ftr2_cells = table.columns[2].cells
ftr3_cells = table.columns[3].cells
hdr_cells[0].text = 'Rubrik'    # sätter konstanta värde på några ställe
hdr_cells[1].text = 'E'
hdr_cells[2].text = 'C'
hdr_cells[3].text = 'A'
for i in range(0,10):   # vad ska finnas i alla 4 kolumner
    ftr_cells[i].text = sheet2.cell_value(i, 0)
    ftr1_cells[i].text = sheet2.cell_value(i, 1)
    ftr2_cells[i].text = sheet2.cell_value(i, 2)
    ftr3_cells[i].text = sheet2.cell_value(i, 3)
# arrayer för betyg
A = []
C = []
E = []
for i in range(1,10):   # sätter in värde i arrayer
    ID = elever.index(elev) + 1
    if sheet1.cell_value(ID, i).startswith("A"):
        A.append(i)
    elif sheet1.cell_value(ID, i).startswith("C"):
        C.append(i)
    elif sheet1.cell_value(ID, i).startswith("E"):
        E.append(i)
# gör så att rätt kunskap nivå blir färgad
for s in range(1,len(A)+1): # för A nivå
    a = []  # array för att få det som står i tabelen
    a.append(table.cell(A[s-1],3))
    paragraphs = a[0].paragraphs    # paragraph som tar värdet från arrayen
    for paragraph in paragraphs:
        for run in paragraph.runs:  # gör run objekt
            font = run.font 
            font.bold = True    # gör texten fet
            font.highlight_color = 4    # väljer highlight färgen
for s in range (1,len(C)+1):    # för C nivå
    c = []
    c.append(table.cell(C[s-1],2))
    paragraphs = c[0].paragraphs
    for paragraph in paragraphs:
        for run in paragraph.runs:
            font = run.font
            font.bold = True
            font.highlight_color = 4    
for s in range (1,len(E)+1):    # för E nivå
    e = []
    e.append(table.cell(E[s-1],1))
    paragraphs = e[0].paragraphs
    for paragraph in paragraphs:
        for run in paragraph.runs:
            font = run.font
            font.bold = True
            font.highlight_color = 4     
# skapar documentet om elevens namn finns på listan
if elev in elever:                    
    document.save(elev + ".docx")
else:   # annars skriver ut fel
    print("Fel namn.")