from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


#from edges import edgy

urlpatterns = [
    path('admin/', admin.site.urls),
    path("edop/",include('edop.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
