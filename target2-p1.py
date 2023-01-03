import cv2 as cv
import time

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)



vidfilename="Seoul - 21985.mp4"
count =0
filename="IMG"
filecount=1
path="extract"
scale=float(input("Enter the rescale multiplier\n"))
frameskip=(int)(input("Enter how many frames to skip after each pick\n"))
frameskip+=1


capture = cv.VideoCapture(vidfilename)


length=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
print(length)

#isTrue,prevframe=(cv.VideoCapture(vidfilename)).read()
#cv.imshow('first frame',prevframe)

time.sleep(2)
while(True):

    isTrue, frame=capture.read()
    count+=1
    if(isTrue==False):
        break
    
    if(count%frameskip==0):
        frame=rescale(frame,scale)
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imwrite(filename,frame)

capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
