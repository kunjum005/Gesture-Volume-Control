import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0) #isse webcam open hota h

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw = mp.solutions.drawing_utils #we have the method provided by mediapipe that actually help us to draw all these points bcox there are so many points, 21 points and b/w each points if you want to line it will be quite a lot of maths that would be involved. so they provided us a method it is in line no 9.

pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #it will convert image to RGB because "hands" object in line no 8 only uses RGB images.
    results = hands.process(imgRGB) #there is a method inside this object "hands" called process that will process the frame for us and give the results.
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks: #we get the information or extract the info of each hand.
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): #enumerate func loop ki value ke sath sath index value bhi deta h.
                #print(id,lm) #we get the id no and landmark from "handLms.landmark".landmark has x,y,z coordinates, we use x,y coordinates to find the location on the hand
                h, w, c= img.shape #it will give the height and width
                cx, cy= int(lm.x*w), int(lm.y*h) #cx,cy are the positions of the center and
                print(id,cx,cy)
                if id==0: #id=0 means first landmark
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  #it will draw a hand for us. to make connections through dot we use "mpHands.HAND_CONNECTIONS"

    cTime = time.time() #it will give current time
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (100,2,200),4)



    cv2.imshow("Image",img)
    cv2.waitKey(1)