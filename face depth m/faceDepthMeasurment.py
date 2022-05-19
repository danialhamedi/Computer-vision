import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
while True:
    ret, img = cap.read()
    img, face = detector.findFaceMesh(img, draw=True)
    if face:
        face = face[0]
        leftpoint = face[145]
        pointright = face[374]
        # cv2.circle(img, leftpoint, 5, (0, 255, 0), cv2.FILLED)
        # cv2.circle(img, pointright, 5, (0, 255, 0), cv2.FILLED)
        # cv2.line(img, leftpoint, pointright, (255, 255, 255), 5)
        w, _ = detector.findDistance(pointright, leftpoint)
        # this function is sensetive to face perspective
        # cv2.putText(img, str(w), (50, 450), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
        W = 6.3
        # d = 50
        # f = (w * d) / W
        # f will be 640
        f = 640
        distance = (W*f)/w
        cv2.putText(img, str(int(distance)), (face[10][0] - 50, face[10][1]), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
    cv2.imshow("img", img)
    cv2.waitKey(1)
