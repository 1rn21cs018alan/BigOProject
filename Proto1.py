import cv2 as cv

img=cv.imread('Capture.png')

#cv.imshow('Cat',img)
filename="Seoul - 21985.mp4"
count =0
speed=2
speed=(int)(input("Enter speed\n"))
timegap=(int)(20/speed)
capture = cv.VideoCapture(filename)
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
path="C:\\Users\\Achu\\Desktop\\BigO Project\\extract"

capture = cv.VideoCapture(filename)
while(True):

    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    count+=1
    if cv.waitKey(timegap) & 0xFF==ord('d'): 
        break;
    if(count%100==0):
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imwrite(filename,frame)

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
