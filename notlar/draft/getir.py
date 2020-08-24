def yaz(a, b):
	hepsi = []
	headline = []
	content = []
	number = []
	descriptions = []
	anahtar = []
	filtre1 = []
	filtre2	= []
	from ingilizce.models import Lesson
	eklenenler = Lesson.objects.all()[a-1:b]
	for i in eklenenler:
		headline.append(i.headline)
		content.append(i.content)
		number.append(i.number)
		descriptions.append(i.descriptions)
		anahtar.append(i.anahtar)
		filtre1.append(i.filtre1)
		filtre2.append(i.filtre2)
	hepsi.append(headline)
	hepsi.append(content)
	hepsi.append(number)
	hepsi.append(descriptions)
	hepsi.append(anahtar)
	hepsi.append(filtre1)
	hepsi.append(filtre2)
	
	hepsi = str(hepsi)
	
	with open("example.py", "w", encoding = "utf-8") as dosya:
		dosya.write(hepsi)
	
def degistir(a, b):
	from ingilizce.models import Lesson
	from example import hepsi
	tum = hepsi()
	c = 0
	for i in range(a, b+1):
		print(i)
		ders = Lesson.objects.get(number = i)
		ders.headline = tum[0][c]
		ders.content = tum[1][c]
		ders.number = tum[2][c]
		ders.descriptions = tum[3][c]
		ders.anahtar = tum[4][c]
		ders.filtre1 = tum[5][c]
		ders.filtre2 = tum[6][c]
		ders.save()
		c = c+1
		
	