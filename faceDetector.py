import cv2

from camera import face_detector, video_capture, image_gray, detections

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    ret, frame = video_capture.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GREY)

    detections = face_detector.detectMultiScale(image_gray)

    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKety(1) & 0XFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()