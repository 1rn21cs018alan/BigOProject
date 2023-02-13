import cv2 as cv
import numpy as np
import time
import copy

def findOffset(prev,curimg):
    w,h=int(prev.shape[1]/3),int(prev.shape[0]/3)
    size_x=int(prev.shape[1])
    size_y=int(prev.shape[0])
    chkboundx=int(w)
    chkboundy=int(h)
    offsetx=0
    offsety=0
    count=0

    totalx,totaly,totalcount=0,0,0
    # print(size_x,size_y)
    x=int(size_x/3)
    y=int(size_y/3)
    orb=cv.ORB_create(nfeatures=800)
    roi=prev[y:y+h,x:x+w]
    cur=curimg[y:y+h,x:x+w]
    #roi is "region of interest"
    roiKeyPoint,roiDesc=orb.detectAndCompute(roi,None)
    curKeyPoint,curDesc=orb.detectAndCompute(cur,None)
    if type(roiDesc)!=type(None) and type(curDesc)!=type(None):
        KPmatcher=cv.BFMatcher(cv.NORM_HAMMING)
        KPmatch=KPmatcher.match(roiDesc,curDesc)
        # print("_-_-_-_--_--_-_-_-_-_--_")
        # for each in (roiKeyPoint):            
        #     print(each.pt)
        # print("________")
        sortedmatch=sorted(KPmatch,key= lambda x:x.distance)
        count=0
        for each in sortedmatch[:20]:
            # print(each.trainIdx,each.queryIdx ,end=",")
            # print(roiKeyPoint[each.queryIdx].pt,curKeyPoint[each.trainIdx].pt)
            
            offset1=roiKeyPoint[each.queryIdx].pt[0]-curKeyPoint[each.trainIdx].pt[0]
            offset2=roiKeyPoint[each.queryIdx].pt[1]-curKeyPoint[each.trainIdx].pt[1]
            if(offset1<15) and (offsety<15):
                offsetx+=offset1
                offsety+=offset2
                count+=1
        if(count!=0):
            offsety/=count
            offsetx/=count 
            totalx+=offsetx
            totaly+=offsety
            totalcount+=1


        matchframe=np.zeros((h*3,w*3),dtype=np.uint8)
        matchframe=cv.drawMatches(roi,roiKeyPoint,cur,curKeyPoint,sortedmatch[:20],matchframe,flags=2)
        cv.imshow("matches center",matchframe)
    

    offsety=0
    offsetx=0       
    count=0
    roi=prev[0:y,0:x]
    cur=curimg[0:y,0:x]
    #roi is "region of interest"
    roiKeyPoint,roiDesc=orb.detectAndCompute(roi,None)
    curKeyPoint,curDesc=orb.detectAndCompute(cur,None)
    if type(roiDesc)!=type(None) and type(curDesc)!=type(None):
        KPmatcher=cv.BFMatcher(cv.NORM_HAMMING)
        KPmatch=KPmatcher.match(roiDesc,curDesc)
        sortedmatch=sorted(KPmatch,key= lambda x:x.distance)
        count=0
        for each in sortedmatch[:20]:
            
            offset1=roiKeyPoint[each.queryIdx].pt[0]-curKeyPoint[each.trainIdx].pt[0]
            offset2=roiKeyPoint[each.queryIdx].pt[1]-curKeyPoint[each.trainIdx].pt[1]
            if(offset1<15) and (offsety<15):
                offsetx+=offset1
                offsety+=offset2
                count+=1
        if(count!=0):
            offsety/=count
            offsetx/=count 
            totalx+=offsetx
            totaly+=offsety
            totalcount+=1       
            

        matchframe=np.zeros((h*3,w*3),dtype=np.uint8)
        matchframe=cv.drawMatches(roi,roiKeyPoint,cur,curKeyPoint,sortedmatch[:20],matchframe,flags=2)
        cv.imshow("matches top left",matchframe)
    

    offsety=0
    offsetx=0
    count=0       
    roi=prev[0:y,2*x:]
    cur=curimg[0:y,2*x:]
    #roi is "region of interest"
    roiKeyPoint,roiDesc=orb.detectAndCompute(roi,None)
    curKeyPoint,curDesc=orb.detectAndCompute(cur,None)
    if type(roiDesc)!=type(None) and type(curDesc)!=type(None):
        KPmatcher=cv.BFMatcher(cv.NORM_HAMMING)
        KPmatch=KPmatcher.match(roiDesc,curDesc)
        sortedmatch=sorted(KPmatch,key= lambda x:x.distance)
        count=0
        for each in sortedmatch[:20]:
            
            offset1=roiKeyPoint[each.queryIdx].pt[0]-curKeyPoint[each.trainIdx].pt[0]
            offset2=roiKeyPoint[each.queryIdx].pt[1]-curKeyPoint[each.trainIdx].pt[1]
            if(offset1<15) and (offsety<15):
                offsetx+=offset1
                offsety+=offset2
                count+=1
        if(count!=0):
            offsety/=count
            offsetx/=count        
            totalx+=offsetx
            totaly+=offsety
            totalcount+=1
            

        matchframe=np.zeros((h*3,w*3),dtype=np.uint8)
        matchframe=cv.drawMatches(roi,roiKeyPoint,cur,curKeyPoint,sortedmatch[:20],matchframe,flags=2)
        cv.imshow("matches top right",matchframe)
    

    offsety=0
    offsetx=0       
    count=0
    roi=prev[2*y:,0:x]
    cur=curimg[2*y:,0:x]
    #roi is "region of interest"
    roiKeyPoint,roiDesc=orb.detectAndCompute(roi,None)
    curKeyPoint,curDesc=orb.detectAndCompute(cur,None)
    if type(roiDesc)!=type(None) and type(curDesc)!=type(None):
        KPmatcher=cv.BFMatcher(cv.NORM_HAMMING)
        KPmatch=KPmatcher.match(roiDesc,curDesc)
        sortedmatch=sorted(KPmatch,key= lambda x:x.distance)
        count=0
        for each in sortedmatch[:20]:
            
            offset1=roiKeyPoint[each.queryIdx].pt[0]-curKeyPoint[each.trainIdx].pt[0]
            offset2=roiKeyPoint[each.queryIdx].pt[1]-curKeyPoint[each.trainIdx].pt[1]
            if(offset1<15) and (offsety<15):
                offsetx+=offset1
                offsety+=offset2
                count+=1
        if(count!=0):
            offsety/=count
            offsetx/=count        
            totalx+=offsetx
            totaly+=offsety
            totalcount+=1
            

        matchframe=np.zeros((h*3,w*3),dtype=np.uint8)
        matchframe=cv.drawMatches(roi,roiKeyPoint,cur,curKeyPoint,sortedmatch[:20],matchframe,flags=2)
        cv.imshow("matches down left",matchframe)
    

    offsety=0
    offsetx=0       
    count=0
    roi=prev[2*y:,2*x:]
    cur=curimg[2*y:,2*x:]
    #roi is "region of interest"
    roiKeyPoint,roiDesc=orb.detectAndCompute(roi,None)
    curKeyPoint,curDesc=orb.detectAndCompute(cur,None)
    if type(roiDesc)!=type(None) and type(curDesc)!=type(None):
        KPmatcher=cv.BFMatcher(cv.NORM_HAMMING)
        KPmatch=KPmatcher.match(roiDesc,curDesc)
        sortedmatch=sorted(KPmatch,key= lambda x:x.distance)
        count=0
        for each in sortedmatch[:20]:
            
            offset1=roiKeyPoint[each.queryIdx].pt[0]-curKeyPoint[each.trainIdx].pt[0]
            offset2=roiKeyPoint[each.queryIdx].pt[1]-curKeyPoint[each.trainIdx].pt[1]
            if(offset1<15) and (offsety<15):
                offsetx+=offset1
                offsety+=offset2
                count+=1
        if(count!=0):
            offsety/=count
            offsetx/=count  
            totalx+=offsetx
            totaly+=offsety
            totalcount+=1      
            
        matchframe=np.zeros((h*3,w*3),dtype=np.uint8)
        matchframe=cv.drawMatches(roi,roiKeyPoint,cur,curKeyPoint,sortedmatch[:20],matchframe,flags=2)
        cv.imshow("matches down right",matchframe)

        # cv.imshow("tracking region",roi)
        # cv.imshow("Ref region",cur)


    if(totalcount==0):
        return (0,0)
    offsetx=totalx/totalcount
    offsety=totaly/totalcount
        # print(offsetx,offsety)
    return (offsetx,offsety)

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
    pageBorder=0.8
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
    pageBorder=float(al[5])
    frameskip+=1
    filename=path+"\\IMG1.png"
    print("started",vidfilename,"-")
    if(choice==0):
        capture = cv.VideoCapture(vidfilename)
    else:
        capture = cv.VideoCapture(0)
    
    outOfBound=True
    # fps = capture.get(cv.CAP_PROP_FPS)
    isTrue, framefull=capture.read()
    while(True):
        isTrue, framefull=capture.read()
        count+=1
        if(isTrue==False):
            break
        prevframefull=framefull
        if(count%frameskip==0):
            if(choice==1):
                framefull=cv.flip(framefull,1)
            frame=rescale(framefull,scale)
            if(count==frameskip):
                prevframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                size_x=prevframe.shape[1]
                size_y=prevframe.shape[0]
                x1,y1=0,0
                print("paged")
                # cv.imwrite(filename1,dif)
                cv.imwrite(filename,framefull)
                
            filename=path+"\\IMG"+str(filecount)+".png"
            filename1=path+"\\DIF"+str(filecount)+".png"
            filecount+=1
            cv.imshow('Current video',frame)
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            dif=cv.subtract(prevframe,gray)
            
            # hist=copy.deepcopy(frame)
            # hist=cv.rectangle(hist,(int(size_y/3),int(size_y/3)),(int(2*size_x/3),int(2*size_y/3)),(255,0,255),3)
            error=finderr(dif)
            # print(error)
            if(error>1):
                (offset_x,offset_y)=findOffset(prevframe,gray)
                x1+=offset_x
                y1+=offset_y
                if(abs(x1)>pageBorder*size_x) or (abs(y1)>pageBorder*size_y):
                    # prevframe=gray
                    x1=0
                    y1=0
                    print("paged")
                    # cv.imwrite(filename1,dif)
                    cv.imwrite(filename,frame)
            else:
                continue

            #     cv.imwrite(filename1,dif)
            #     cv.imwrite(filename,frame)
            # cv.imshow('tracking window',hist)
            prevframe=gray
            if( cv.waitKey(timegap) & 0xFF==ord('d')):
                break
        
        
    cv.imwrite(filename,prevframefull)

    capture.release()

    cv.destroyAllWindows()

    cv.waitKey(0)


main()
