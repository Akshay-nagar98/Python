from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	if request.method=="POST":
		url="http://localhost:8001/api/books"
		querystring = {
			'title':request.POST['title'],
			'author':request.POST['author'],
			'isbn':request.POST['isbn'],
			'publisher':request.POST['publisher'],
		}
		response = requests.post(url,json=querystring)
		print(response.text)
		msg="Data Inserted Successfully"
		return render(request,'index.html',{'msg':msg})
	else:
		return render(request,'index.html')