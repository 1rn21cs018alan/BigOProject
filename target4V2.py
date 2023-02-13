import cv2 as cv
import numpy as np
import time
import copy
from Tracker import findOffset

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
    al=[]
    with open("values.txt",mode="r") as MyFile:
        for x in MyFile:
            al.append(x)
    scale=float(al[0])
    frameskip=int(al[1])
    timegap=int(al[2])
    vidfilename=str(al[3])
    vidfilename=vidfilename.strip()
    choice=int(al[4])
    frameskip+=1
    print("started",vidfilename,"-")
    if(choice==0):
        capture = cv.VideoCapture(vidfilename)
    else:
        capture = cv.VideoCapture(0)
    
    outOfBound=True
    term=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)
    # fps = capture.get(cv.CAP_PROP_FPS)
    isTrue, frame=capture.read()
    while(True):
        isTrue, frame=capture.read()
        count+=1
        if(isTrue==False):
            break
        
        if(count%frameskip==0):
            if(choice==1):
                frame=cv.flip(frame,1)
            frame=rescale(frame,scale)
            if(count==frameskip):
                prevframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            filename=path+"\\IMG"+str(filecount)+".png"
            if(outOfBound):
                boundy,boundx=frame.shape[0]/3,frame.shape[1]/3
                x1,y1=frame.shape[1]/3,frame.shape[0]/3
                outOfBound=False
            
            filename1=path+"\\DIF"+str(filecount)+".png"
            filecount+=1
            cv.imshow('Current video',frame)
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            dif=cv.subtract(prevframe,gray)
            blur = cv.GaussianBlur(gray,(5,5),0)
            _, thresh = cv.threshold(blur,10, 255, cv.THRESH_BINARY) 
            hist=copy.deepcopy(frame)
            hist=cv.rectangle(hist,(int(x1),int(y1)),(int(x1+min(boundx,boundy)),int(y1+min(boundx,boundy))),255,3)
            error=finderr(dif)
            # print(error)
            if(error>4):
                (x1,y1)=findOffset(blur,x1,y1)
                if abs(x1-boundx)>(0.9*boundx) or abs(y1-boundy)>(0.9*boundy):
                    outOfBound=True
                    print("paged")
                    print("\n",error,"\t",filecount)

            #     cv.imwrite(filename1,dif)
            #     cv.imwrite(filename,frame)
            cv.imshow('tracking window',hist)
            prevframe=gray
            if( cv.waitKey(timegap) & 0xFF==ord('d')):
                break
        
        
        #cv.imwrite(filename,frame)

    capture.release()

    cv.destroyAllWindows()

    cv.waitKey(0)


main()
