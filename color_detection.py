'''
This code will detect the colors of rubicks cube (Red, Green, Blue, Orange, Yellow< white)
'''

import cv2
import numpy as np
from PIL import Image

# Function to make a bounding box on a detected color portion
def GetBoundingBox(boarder, color):
    global frame
    if boarder is not None:
        x1, y1, x2, y2 = boarder  #getting cordinates of detected color portion
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), [0,255,0], 5)
        cv2.putText(frame,  
                color,  
                (x1,y1),  
                cv2.FONT_HERSHEY_SIMPLEX, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4) 


cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    img_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Calebrated HSV values for Red
    lower_Red = np.array([164,195,169])
    upper_Red = np.array([172,226,195])
    mask_Red = cv2.inRange(img_HSV, lower_Red, upper_Red)
    mask_Red2 = Image.fromarray(mask_Red) 
    boarder_Red = mask_Red2.getbbox()
    GetBoundingBox(boarder_Red,color="RED")

    # Calebrated HSV values for Green
    lower_Greean = np.array([64,189,158])
    upper_Greean = np.array([70,235,185])
    mask_Green = cv2.inRange(img_HSV, lower_Greean, upper_Greean)
    mask_Green2 = Image.fromarray(mask_Green)
    boarder_Green = mask_Green2.getbbox()
    GetBoundingBox(boarder_Green,color="GREEN")

    # Calebrated HSV values for Blue
    lower_Blue = np.array([93,211,189])
    upper_Blue = np.array([98,255,222])
    mask_Blue = cv2.inRange(img_HSV, lower_Blue,upper_Blue)
    mask_Blue2 = Image.fromarray(mask_Blue)
    boarder_Blue = mask_Blue2.getbbox()
    GetBoundingBox(boarder_Blue,color="BLUE")

    # Calebrated HSV values for Orange
    lower_Orange = np.array([4,176,188])
    upper_Orange = np.array([6,213,229])
    mask_Orange = cv2.inRange(img_HSV, lower_Orange,upper_Orange)
    mask_Orange2 = Image.fromarray(mask_Orange)
    boarder_Orange = mask_Orange2.getbbox()
    GetBoundingBox(boarder_Orange,color="ORANGE")

    # Calebrated HSV values for Yellow
    lower_Yellow = np.array([29,186,159])
    upper_Yellow = np.array([38,228,188])
    mask_Yellow = cv2.inRange(img_HSV, lower_Yellow,upper_Yellow)
    mask_Yellow2 = Image.fromarray(mask_Yellow)
    boarder_Yellow = mask_Yellow2.getbbox()
    GetBoundingBox(boarder_Yellow,color="YELLOW")

    # Calebrated HSV values for White
    lower_White = np.array([99,23,172])
    upper_White  = np.array([113,54,198])
    mask_White  = cv2.inRange(img_HSV, lower_White,upper_White)
    mask_White2 = Image.fromarray(mask_White)
    boarder_White = mask_White2.getbbox()
    GetBoundingBox(boarder_White,color="WHITE")
    
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows() # Close all windows on the screen
 
