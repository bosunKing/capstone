import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_contour=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        center_x = x + w//2
        center_y = y + h//2
        print("center: ( %s, %s )"%(center_x, center_y)) 
        print("Face Contour Coords:", face_contour)
        cv2.drawContours(frame, [np.array(face_contour)], 0, (0, 0, 255), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # 눈 영역의 컨투어 좌표를 얻습니다.
           # eye_contour = [(x + ex, y + ey), (x + ex + ew, y + ey), (x + ex + ew, y + ey + eh), (x + ex, y + ey + eh)]
            #print("Eye Contour Coords:", eye_contour)
            #cv2.drawContours(roi_color, [np.array(eye_contour)], 0, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()