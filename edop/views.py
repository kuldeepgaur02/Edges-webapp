from pyexpat.errors import messages
from django.shortcuts import render 
from django.http import HttpResponse
from.models import Pictiure 
import cv2 
import numpy as np
import os
from .filter import *

def index(request):
    return render(request,'edop/index.html')
    
    
def sobel(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = sobel_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)
    return render(request,'edop/sobel.html')

def canny(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = canny_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/canny.html')

def prewitt(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = prewit_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/prewitt.html')

def Hirsch(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = kirsch_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/hirsch.html')
    
def laplacian(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = laplacian_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/laplacian.html')

def Scharr(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = scharr_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/schar.html')
def Robert(request):
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
        
        # return render(request,'edop/sobel.html')
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = robert_(path)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)

    return render(request,'edop/robert.html')
def Combination(request): 
    
    sobel=request.POST.get('sobel',0)
    print(sobel)
    canny=request.POST.get('canny',0)
    print(canny)
    kirsch=request.POST.get('Kirsch',0)
    print(kirsch)
    prewitt=request.POST.get('prewitt',0)
    print(prewitt)
    robert=request.POST.get('robert',0)
    print(robert)
    laplacian=request.POST.get('laplacian',0)
    print(laplacian)
    schar=request.POST.get('schar',0)
    print(schar)
    
    if request.method=="POST":
        im=Pictiure()
        
        if len(request.FILES) !=0:
            im.venue_image=request.FILES['filename']
        im.save()
    
        path = os.path.join(r"/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/media/",str(im.venue_image.name))
        imgout = combine_(path,sobel,prewitt,canny,kirsch,laplacian,robert,schar)
        cv2.imwrite('/Users/kuldeeprajgour/Documents/my DESKTOP WORK/project/django__/eddy/static/images/hello.jpeg',imgout)
    
    
    

    return render(request,'edop/combination.html')