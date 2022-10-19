from re import L
import cv2
import numpy as np
from scipy import ndimage


#------------------------------------------------------------------------------------------------------------------------------------

def sobel_(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(3,3),0)
    
    sobelxy = cv2.Sobel(blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
    sobel_edges = cv2.convertScaleAbs(sobelxy)
    
    return sobel_edges

#------------------------------------------------------------------------------------------------------------------------------------

def prewit_(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(3,3),0)
    
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(blur_img, -1, kernelx)
    img_prewitty = cv2.filter2D(blur_img, -1, kernely)
    
    img_prewitt = np.add(img_prewittx,img_prewitty)
    
    return img_prewitt

#------------------------------------------------------------------------------------------------------------------------------------

def canny_(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(3,3),0)
    
    med_val = np.median(blur_img) 
    lower = int(max(0 ,0.7*med_val))
    upper = int(min(255,1.3*med_val))
    
    edges = cv2.Canny(blur_img, threshold1=lower,threshold2=upper)
    
    return edges

#------------------------------------------------------------------------------------------------------------------------------------

def kirsch_(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    kernelG1 = np.array([[ 5,  5,  5],
                         [-3,  0, -3],
                         [-3, -3, -3]], dtype=np.float32)
    
    kernelG2 = np.array([[ 5,  5, -3],
                         [ 5,  0, -3],
                         [-3, -3, -3]], dtype=np.float32)
    
    kernelG3 = np.array([[ 5, -3, -3],
                         [ 5,  0, -3],
                         [ 5, -3, -3]], dtype=np.float32)
    
    kernelG4 = np.array([[-3, -3, -3],
                         [ 5,  0, -3],
                         [ 5,  5, -3]], dtype=np.float32)
    
    kernelG5 = np.array([[-3, -3, -3],
                         [-3,  0, -3],
                         [ 5,  5,  5]], dtype=np.float32)
    
    kernelG6 = np.array([[-3, -3, -3],
                         [-3,  0,  5],
                         [-3,  5,  5]], dtype=np.float32)
    
    kernelG7 = np.array([[-3, -3,  5],
                         [-3,  0,  5],
                         [-3, -3,  5]], dtype=np.float32)
    
    kernelG8 = np.array([[-3,  5,  5],
                         [-3,  0,  5],
                         [-3, -3, -3]], dtype=np.float32)

    g1 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g2 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG2), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g3 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG3), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g4 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG4), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g5 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG5), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g6 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG6), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g7 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG7), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g8 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG8), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    magn = cv2.max(
        g1, cv2.max(
            g2, cv2.max(
                g3, cv2.max(
                    g4, cv2.max(
                        g5, cv2.max(
                            g6, cv2.max(
                                g7, g8
                            )
                        )
                    )
                )
            )
        )
    )
    return magn

#------------------------------------------------------------------------------------------------------------------------------------

def laplacian_(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(3,3),0)
    
    laplacian = cv2.Laplacian(blur_img,5,cv2.CV_64F)
    filtered_image = cv2.convertScaleAbs(laplacian)
    return filtered_image

#------------------------------------------------------------------------------------------------------------------------------------

def robert_(path):
    img =cv2.imread(path)
    img = cv2.imread(path)

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype('float64')
    
    gray/=255.0
    
    roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
    roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )
    
    vertical = ndimage.convolve(gray, roberts_cross_v )
    horizontal = ndimage.convolve( gray, roberts_cross_h )
  
    edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img*=255
    
    return edged_img

#------------------------------------------------------------------------------------------------------------------------------------

def scharr_(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(3,3),0)
    
    kernelx = np.array([[3,10,3],
                        [0,0,0],
                        [-3,-10,-3]])
    kernely = np.array([[3,0,-3],
                        [10,0,-10],
                        [3,0,-3]])
    
    img_scharrx = cv2.filter2D(blur_img, -1, kernelx)
    img_scharry = cv2.filter2D(blur_img, -1, kernely)
    
    img_scharr = np.add(img_scharrx,img_scharry)
    
    return img_scharr
    
#------------------------------------------------------------------------------------------------------------------------------------

def combine_(img2, flag_sobel,flag_prewit, flag_canny, flag_kirsch, flag_laplacian, flag_robert, flag_scharr):
    
    img = cv2.imread(img2)
    sobel_mask = np.zeros(img.shape[0:2])
    prewit_mask = np.zeros(img.shape[0:2])
    canny_mask = np.zeros(img.shape[0:2])
    kirsch_mask = np.zeros(img.shape[0:2])
    robert_mask = np.zeros(img.shape[0:2])
    laplacian_mask = np.zeros(img.shape[0:2])
    scharr_mask = np.zeros(img.shape[0:2])
    
    if(flag_sobel):
        sobel_mask = sobel_(img2)
    
    if(flag_prewit):
        prewit_mask = prewit_(img2)
        
    if(flag_canny):
        canny_mask = canny_(img2)
        
    if(flag_kirsch):
        kirsch_mask = kirsch_(img2)
        
    if(flag_laplacian):
        laplacian_mask = laplacian_(img2)
        
    if(flag_robert):
        robert_mask = robert_(img2)
        
    if(flag_scharr):
        scharr_mask = scharr_(img2)
        
    combine_mask = sobel_mask + prewit_mask + canny_mask + kirsch_mask + laplacian_mask + robert_mask + scharr_mask
    
    return combine_mask
