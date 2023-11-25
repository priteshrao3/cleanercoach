from django.shortcuts import render
from django.views import View
from .models import ServicePage, Project, Testomonial, GalleryImg, Video
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



# Create your views here.
class HomePage(View):
    template_name = ''
    def get(self, request):
        service = ServicePage.objects.all()
        project = Project.objects.all()
        testom = Testomonial.objects.all()
        galleryimg = GalleryImg.objects.all()
        return render(request, self.template_name, {'services':service, 'project':project, 'testom':testom, 'galleryimg':galleryimg})

    def post(self, request):
        username = 'Name: '
        useremail = 'Email: '
        userphone = 'Phone No.: '
        usermessage = 'Message: '

        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        send_mail(
            subject,
            username+name +'\n'+  useremail+email +'\n'+ userphone+phone +'\n'+ '\n'+ usermessage+message,
            settings.EMAIL_HOST_USER,
            ['devepritesh@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'Your message send successful..!')
        return render(request, self.template_name)





class Services(View):
    def get(self, request, servd):
        serv_title = servd.replace('-', ' ')
        service = ServicePage.objects.all()
        video = Video.objects.all()
        services=ServicePage.objects.get(Service_Title=serv_title)  
        return render(request, 'app/service-details.html', {'serv':services, 'services':service, 'video':video})
