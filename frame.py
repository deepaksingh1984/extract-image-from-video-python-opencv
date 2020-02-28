import cv2 
import os 

cam = cv2.VideoCapture("C:/Users/COM/Desktop/frame/online-tutor.mp4") 
framerate = int(cam.get(cv2.CAP_PROP_FPS))
framecount = 0
try: 
    if not os.path.exists('imaes'): 
        os.makedirs('images') 
except OSError: 
    print ('Error: Creating directory of data') 
  
currentframe = 1
  
while(True): 
    ret,frame = cam.read() 
    framecount += 1
    if framecount == (framerate * 30):
        framecount = 0
        name = './images/' + str(currentframe) + '.jpg'
        print ('Creating...' + name)  
        cv2.imwrite(name, frame)
        currentframe += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cam.release() 
cv2.destroyAllWindows() 