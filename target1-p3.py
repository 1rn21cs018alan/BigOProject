import cv2 as cv


vidfilename="Seoul - 21985.mp4"
count =0
filename="IMG"
filecount=1
path="extract"
frameskip=(int)(input("Enter how many frames to skip after each pick\n"))
frameskip+=1

capture = cv.VideoCapture(vidfilename)

length=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
print(length)
while(True):

    isTrue, frame=capture.read()
    count+=1
    #if(count> length):
    if(isTrue==False):
        break;
        
    if(count%frameskip==0):
        filename=path+"\\IMG"+str(filecount)+".png"
        filecount+=1
        cv.imwrite(filename,frame)

capture.release()
