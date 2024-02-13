from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blog.urls')),
    path('Doctors/', include('Doctors.urls')),
    path('Blood_Bank/', include('Blood_Bank.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
