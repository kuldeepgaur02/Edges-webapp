from.import views
#from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",views.index,name="edgyhome"),
    path("Sobel/",views.sobel,name="Sobel"),
    path("Canny/",views.canny,name="Canny"),
    path("Prewitt/",views.prewitt,name="Prewitt"),
    path("Hirsch/",views.Hirsch,name="Hirsch"),
    path("Laplacian/",views.laplacian,name="Laplacian"),
    path("Scharr/",views.Scharr,name="Scharr"),
    path("Robert/",views.Robert,name="Robert"),
    path("Combination/",views.Combination,name="Combination"),
    
]
