import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(3, 1280.)
cap.set(4, 720.)

cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, False)
cap.set(cv2.CAP_PROP_EXPOSURE, -6)

# Distances In inches
KNOWN_HEIGHT = 6
KNOWN_DISTANCE = 43
FOCAL_LENGTH = 590

IMAGE_WIDTH = 640
IMAGE_CENTER = IMAGE_WIDTH/2
H_FOV = 53
DPP = H_FOV/IMAGE_WIDTH
print(DPP)
MIN_AREA = 1000

while True:

    ret, frame = cap.read()
    cv2.imshow("Filtering", frame)


    if cv2.waitKey(1) == 27:
        break  # esc to quit
cv2.destroyAllWindows()