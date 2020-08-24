from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from django.utils.html import escape
from bs4 import BeautifulSoup
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.units import inch
		
import reportlab
import os

from dersler.models import Baslik, Ders

def pdf_view(request):
	fs = FileSystemStorage(location= "dosyalar/", base_url = "dosya/")
	filename = 'django.pdf'
	if fs.exists(filename):
		with fs.open(filename) as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
			return response
	else:
		return HttpResponseNotFound('The requested pdf was not found in our server.')


		

#from django.contrib.auth.models import User

class MyPrint:
	def __init__(self, buffer, pagesize):
		self.buffer = buffer
		if pagesize == 'A4':
			self.pagesize = A4
		elif pagesize == 'Letter':
			self.pagesize = letter
			self.width, self.height = self.pagesize
	
	def print_users(self, pk):
		
		reportlab_directory = os.path.dirname(reportlab.__file__)
		font_folder = os.path.join(reportlab_directory, "fonts")

		custom_font_folder = os.path.join(font_folder, "Arial.ttf")
		custom_font_bold_folder = os.path.join(font_folder, "Arial-bold.ttf")
		custom_font_italic_folder = os.path.join(font_folder, "Arial-italic.ttf")

		custom_font = TTFont("arial", custom_font_folder)
		custom_font_bold = TTFont("arial-bold", custom_font_bold_folder)
		custom_font_italic = TTFont("arial-italic", custom_font_italic_folder)

		pdfmetrics.registerFont(custom_font)
		pdfmetrics.registerFont(custom_font_bold)
		pdfmetrics.registerFont(custom_font_italic)

		registerFontFamily('hepsi', normal = "arial", bold = "arial-bold", italic = "arial-italic")

		
		
			
		
		buffer = self.buffer
		doc = SimpleDocTemplate(buffer,
			rightMargin=20,
			leftMargin=20,
			topMargin=20,
			bottomMargin=20,
			pagesize=self.pagesize)
		
		
		# Our container for 'Flowable' objects
		elements = []

		# A large collection of style sheets pre-made for us
		styles = getSampleStyleSheet()
		styles.add(ParagraphStyle(name='baslik', fontName = "arial", fontSize = 18, leading = 25, textColor = colors.red))
		styles.add(ParagraphStyle(name='alt-baslik', fontName = "arial", fontSize = 16, leading = 25, textColor = colors.red))
		styles.add(ParagraphStyle(name='paragraf', fontName = "arial", fontSize = 14, leading = 15))
		styles.add(ParagraphStyle(name='paragraf-bold', fontName = "arial", fontSize = 14, leading = 15))
		styles.add(ParagraphStyle(name='deneme', fontName = "hepsi", fontSize = 14, leading = 15))

		# Draw things on the PDF. Here's where the PDF generation happens.
		# See the ReportLab documentation for the full list of functionality.
		liste = [] 

		baslik = get_object_or_404(Baslik, pk = pk)
		dersler = baslik.ders_set.all()
		elements.append(Paragraph(baslik.title, styles["baslik"]))
		elements.append(Paragraph(baslik.content + "<br></br><br></br>", styles['paragraf']))
		for ders in dersler:
			elements.append(Paragraph(ders.title, styles['alt-baslik']))
			soup = BeautifulSoup(ders.content)				
			#paragraflar = soup.find_all("p")
			element_listesi = soup.find_all(["p", "table"])
			
			for element in element_listesi:
				if element.name =="p":
					paragraf = str(element) + "<br></br>" +  "<br></br>"
					elements.append(Paragraph(paragraf, styles['paragraf']))
				
				if element.name =="table":
					liste = []
					tr = element.findAll("tr")
					print("")
					#print(tr)
					print("")
					for i in tr:
						data = i.findAll(["th", "td"])
						data = [i.text for i in data]
						print("")
						#print(data)
						print("")
						print()
						
						print("")
						
						liste.append(data)
						#print(liste)
						print("")
						
					tstyle = TableStyle([("GRID", (0, 0), (-1, -1), 0.2, colors.red),
											  ('ALIGN',(0,0),(-1,-1),'LEFT'),
											  ("FONT", (0, 0), (-1, -1), "arial", 12),
											  ('VALIGN', (0,0),(-1,-1), "TOP"),
											  #('SPAN',(-0,-0),(-1,-1)),
											  #("BOX", (0, 0), (-1, -1), 0.2, colors.red),
							])
					print("LİSteeeeeeeeeeeeeee")
					print(liste,)
					t = Table(liste, rowHeights=50, colWidths=50)
					t.setStyle(tstyle)
					#t._argW[3]=5*inch
					elements.append(t)
				#elements.append(Paragraph("!!!Tablomuz burada!!!", styles['paragraf']))
					

		doc.build(elements)

		# Get the value of the BytesIO buffer and write it to the response.
		pdf = buffer.getvalue()
		buffer.close()
		return pdf

from io import BytesIO

def print_users(request, pk):
	
	
	
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="My Users.pdf"'

	buffer = BytesIO()

	report = MyPrint(buffer, 'Letter')
	pdf = report.print_users(pk)

	response.write(pdf)
	return response


def pdf_create(request, pk):
	baslik = get_object_or_404(Baslik, pk=pk)
	
	from reportlab.lib.styles import ParagraphStyle
	from reportlab.pdfbase import pdfmetrics
	from reportlab.pdfbase.ttfonts import TTFont
	
	dersler = baslik.ders_set.all()
	
	Story = []
	
	
	
	pdfmetrics.registerFont(TTFont("Hebrew", "Arial.ttf"))
	
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="filename.pdf"'
	
	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response, pagesize = A4)
	p.setFont("Hebrew", 24)
	
	p.drawString(5, 800, baslik.title)
	
	p.setFont("Hebrew", 14)
	p.drawString(5, 780, baslik.content)
	
	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

