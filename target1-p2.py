import cv2 as cv

img=cv.imread('Capture.png')

#cv.imshow('Cat',img)
vidfilename="Seoul - 21985.mp4"
count =0
filename="IMG"
filecount=1
path="extract"
frameskip=(int)(input("Enter how many frames to skip after each pick\n"))
frameskip+=1
capture = cv.VideoCapture(vidfilename)
while(True):

    isTrue, frame=capture.read()
    count+=1
    if(count%frameskip==0):
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imwrite(filename,frame)

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
