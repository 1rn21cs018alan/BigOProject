import cv2 as cv

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
