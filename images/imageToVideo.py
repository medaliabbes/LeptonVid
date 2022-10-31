import cv2 
import glob

frameSize = (160, 120)

out = cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc(*'DIVX'),9, frameSize)
#IM_22-10-30_20_49_00_xx.bmp
#for filename in glob.glob('./*.bmp'):
for i in range(0,100):
    filename = 'IM_22-10-30_20_49_00_'
    try :
        if(i>=10):
            filename = filename+str(i)+'.bmp'
        else:
            filename = filename+'0'+str(i)+'.bmp'
        print(filename)
        img = cv2.imread(filename , -1)
        #img = cv2.resize(img ,((320, 320 )))
        #cv2.imshow("im" , img)
        #cv2.waitKey(0)
        #img = _2dto3d(img)
        out.write(img)
        print(img.shape)
    except Exception as e :
        print(e)

out.release()
