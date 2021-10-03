from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Profile
import pdfkit
from django.template.loader import get_template, render_to_string
import io



# Create your views here.
def index(request):
    return render(request, 'pdf/resume.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")    
        image = request.POST.get("image")    
        email = request.POST.get("email")    
        phone = request.POST.get("phone")    
        address = request.POST.get("address")    
        competence = request.POST.get("competence")
        langue = request.POST.get("langue")
        interet = request.POST.get("interet")    
        objectif = request.POST.get("objectif")  
        experience = request.POST.get("experience")    
        education = request.POST.get("education")    
        projet = request.POST.get("projet")  

        profile = Profile(name=name, email=email,image=image, phone=phone, address=address, competance=competence, langue=langue, interet=interet, objectif=objectif, experience=experience, education=education, Projet=projet)
        profile.save()
        return HttpResponse('Vos donnes ')

    return render(request, 'pdf/form.html')    

def viewcv(request, id):
    profile = Profile.objects.get(pk=id)
    com = profile.competance.split(',')
    langue = profile.langue.split(',')
    interet = profile.interet.split(',')
    exp = profile.experience.split('.')   
    objectif = profile.objectif.split('.')   
    education = profile.education.split('.')   
    project = profile.Projet.split('.')   
    template = get_template('pdf/generer.html')
    html = template.render({'profile':profile, 'com':com, 'interet':interet, 'langue':langue, 'experience':exp, 'objectif':objectif, 'education': education, 'project':project })
    option ={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html,False, option)
    reponse = HttpResponse(pdf, content_tyte='application/pdf')
    reponse['Content-Disposition']="attachement"
    filename = 'resume.pdf'
    
    return reponse

        

