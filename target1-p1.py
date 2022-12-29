import cv2 as cv

img=cv.imread('Capture.png')

#cv.imshow('Cat',img)
vidfilename="Seoul - 21985.mp4"
count =0
speed=2
speed=(int)(input("Enter speed multiplier for live feed\n"))
timegap=(int)(20/speed)
filename="IMG"
filecount=1
path="extract"
frameskip=10
capture = cv.VideoCapture(vidfilename)
while(True):

    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    count+=1
    if cv.waitKey(timegap) & 0xFF==ord('d'): 
        break;
    if(count%frameskip==0):
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imwrite(filename,frame)

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
