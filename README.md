# Extract Image from m4 video using opencv python

Install openCV
```
  pip install opencv-python
```

create a python page i.e frame.py

```
#Import OpenCV module
import cv2 

#import OS module
import os 

# define vidoe path
vid = cv2.VideoCapture("C:/Users/COM/Desktop/video.mp4") 

# get Framerate
framerate = int(vid.get(cv2.CAP_PROP_FPS))
framecount = 0


try: 
    #Create a directory to strore generated images
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

```

# Done! 

just run the code:

```
python frame.py
```
