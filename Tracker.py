import cv2 as cv
import numpy as np
def findOffset(gray,x,y):
    w,h=int(gray.shape[1]/3),int(gray.shape[0]/3)
    x=int(x)
    y=int(y)
    # roi=np.zeros((h*3,w*3),dtype=np.uint8)
    w=min(w,h)
    h=w
    track=(int(x),int(y),w,h)
    # here, term criteria tells when an iterative algorith should stop
    # for EPS, it means accuracy and for count, it is no of maximum iterations per function call
    term=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,1,15)
    canny=cv.Canny(gray,130,130)
    cv.imshow("Canny",canny)
    _,hist1=cv.meanShift(canny,track,term)
    # roi[x:x+w,y:y+h]=canny[x:x+w,y:y+h]
    # cv.imshow("ROI",roi)
    # _,hist1=cv.meanShift(roi,track,term)
    x=hist1[0]
    y=hist1[1]
    return x,y