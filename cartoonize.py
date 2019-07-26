import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def cartoonifyImage(frame):
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     small= cv2.resize(frame,None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
    
     median = cv2.medianBlur(gray,7)
     dst=cv2.Laplacian(median, 5)
 
     retval, mask= cv2.threshold(dst, 10, 255, cv2.THRESH_BINARY_INV)
     
     
     repetitions = 11
     
     for i in range(repetitions):
         ksize=9
         sigmaColor=9
         sigmaSpacce=7
         temp = cv2.bilateralFilter(small,ksize,sigmaColor,sigmaSpacce)
         small = cv2.bilateralFilter(temp,ksize,sigmaColor,sigmaSpacce)
    
     bigImg=cv2.resize(small,None, fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
     mask= cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
     
     new_mask=mask.astype(np.uint8)
     
     dst = cv2.addWeighted(bigImg,0.8,new_mask,0.2,0)
     return dst
    
    
while(True):
    
    ret, frame = cap.read()
   
    result= cartoonifyImage(frame)
    
    cv2.imshow('frame',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()