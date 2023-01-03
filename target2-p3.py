import cv2 as cv
import numpy as np
import time

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def finderr(dif):
    err=np.sum(dif**2)
    mse=err/(float)(dif.shape[1] * dif.shape[0])
    return mse


vidfilename="Seoul - 21985.mp4"
count =0
filename="IMG"
filecount=1
path="extract"
scale=float(input("Enter the rescale multiplier\n"))
frameskip=(int)(input("Enter how many frames to skip after each pick\n"))
frameskip+=1


capture = cv.VideoCapture(vidfilename)


error=0

length=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
print(length)


while(True):
    isTrue, frame=capture.read()
    count+=1
    if(isTrue==False):
        break
    
    if(count%frameskip==0):
        frame=rescale(frame,scale)
        if(count==frameskip):
            prevframe=frame
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imshow('Current video',frame)
        cv.imshow('previous video',prevframe)
        prevgray=cv.cvtColor(prevframe,cv.COLOR_BGR2GRAY)
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        dif=cv.subtract(prevgray,gray)
        error=finderr(dif)
        print("\n",error)
        cv.imshow('difference video',dif)
        prevframe=frame
        if( cv.waitKey(25) & 0xFF==ord('d')):
            break;
        
        
        #cv.imwrite(filename,frame)

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
