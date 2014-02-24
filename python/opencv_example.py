#SKumar
from cv2.cv import *
img = LoadImage(sys.argv[1])
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)