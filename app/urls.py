from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage.as_view(template_name='app/index.html'), name='homepage'),
    path('about-us', views.HomePage.as_view(template_name='app/about.html'), name='about'),
    path('gallery', views.HomePage.as_view(template_name='app/gallery.html'), name='gallery'),
    path('franchise', views.HomePage.as_view(template_name='app/franchise.html'), name='franchise'),
    path('contact-us', views.HomePage.as_view(template_name='app/contact.html'), name='contact'),
    path('terms-and-conditions', views.HomePage.as_view(template_name='app/terms-and-conditions.html'), name='terms-and-conditions'),
    path('service/<servd>', views.Services.as_view(), name='service-details'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)