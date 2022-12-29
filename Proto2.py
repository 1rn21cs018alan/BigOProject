import cv2 as cv
#import numpy 

#def imgcomp(img1,img2):
    



img=cv.imread('Capture.png')

#cv.imshow('Cat',img)

count =0
speed=2
speed=(int)(input("Enter speed\n"))
timegap=(int)(20/speed)
capture = cv.VideoCapture("vid1.mp4")
while(True):

    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    count+=1
    if(count==7619):
        break;
    if(count%speed<3):
        if cv.waitKey(timegap) & 0xFF==ord('d'): 
            break;
    
capture.release()

cv.destroyAllWindows()

cv.waitKey(0)

filename="IMG"
filecount=1
samecount=1
path="C:\\Users\\Achu\\Desktop\\BigO Project\\extract2"
flag1=0
capture = cv.VideoCapture("vid1.mp4")
while(True):

    isTrue, frame=capture.read()
    
    cv.imshow('Video',frame)
    count+=1
    if cv.waitKey(timegap) & 0xFF==ord('d'): 
        break;
    if(count%100==0):
        if(flag1==1):
            print("1\n")
            if (frame.all()==prevframe.all()):
                print("identical\n")
                filename=path+"\\sameA"+str(samecount)+".png"
                cv.imwrite(filename,frame)
                
                filename=path+"\\sameB"+str(samecount)+".png"
                samecount+=1
                cv.imwrite(filename,prevframe)
            else:
                filename=path+"\\IMG"+str(filecount)+".png"
                filecount+=1
                cv.imwrite(filename,frame)
        else:
            filename=path+"\\IMG"+str(filecount)+".png"
            filecount+=1
            cv.imwrite(filename,frame)
        flag1=1
        prevframe=frame
    

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
