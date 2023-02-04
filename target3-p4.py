import cv2 as cv
import numpy as np
import time
import copy

# trying to find motion also

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def finderr(dif):
    err=np.sum(dif**2)
    mse=err/(float)(dif.shape[1] * dif.shape[0])
    return mse

def main():
    # vidfilename="TestVid1.mp4"
    vidfilename="TestVid2.mp4"
    # vidfilename="Seoul - 21985.mp4"
    count =0
    filename="IMG"
    filecount=1
    path="extract"
    scale=float(input("Enter the rescale multiplier\n"))
    frameskip=(int)(input("Enter how many frames to skip after each pick\n"))
    frameskip+=1

    Kernelsize=7;  #to adjust amount of blur


    capture = cv.VideoCapture(vidfilename)
    # capture = cv.VideoCapture(0)


    error=0

    # length=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    # print(length)
    
    # speed=2
    # speed=(float)(input("Enter speed multiplier for live feed\n"))
    timegap=20

    thres=10
    x1,y1,w1,h1=(100,100,200,200)
    track=(x1,y1,w1,h1)
    term=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)
    # fps = capture.get(cv.CAP_PROP_FPS)
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
            
            filename1=path+"\\DIF"+str(filecount)+".png"
            filecount+=1
            cv.imshow('Current video',frame)
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            canny=cv.Canny(gray,80,255)
            _,hist1=cv.meanShift(canny,track,term)
            x1,y1,w1,h1=hist1
            track=hist1
            # print(gray.shape)
            # blur = cv.GaussianBlur(dif, (Kernelsize, Kernelsize), 0) 
            # _, thresh = cv.threshold(blur,thres, 255, cv.THRESH_BINARY) 
            
            hist=copy.deepcopy(frame)
            hist=cv.rectangle(hist,(x1,y1),(x1+w1,y1+h1),255,3)
            # error=finderr(dif)
            # print(error)
            # if(error>1):
            #     print("\n",error,"\t",filecount)
            #     cv.imwrite(filename1,dif)
            #     cv.imwrite(filename,frame)
            cv.imshow('blur video',canny)
            cv.imshow('tracking window',hist)
            prevframe=frame
            if( cv.waitKey(timegap) & 0xFF==ord('d')):
                break;
        
        
        #cv.imwrite(filename,frame)

    capture.release()

    cv.destroyAllWindows()

    cv.waitKey(0)


main()
