import cv2
from util import get_limits
from PIL import Image
green = [0,255,0]

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerlimit,upperlimit = get_limits(color=green)

    mask = cv2.inRange(hsv_image,lowerlimit,upperlimit)

    mask_ = Image.fromarray(mask) #converting image format from np array to pillow image
    bbox = mask_.getbbox()

    print(bbox)

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)

    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()