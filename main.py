import time
import cv2


class Camera:

    def __init__(self, port):
        self.port = port

    def startFaceDetect(self):
        print("---- Welcome to Face Detector! ----\n")
        time.sleep(0.25)
        print("~System is using Camera with id : ", int(self.port))
        time.sleep(0.5)
        print("~ Please wait while we configure the system")
        time.sleep(1)
        print("~ Displaying video feed!")
        cap = cv2.VideoCapture(self.port)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=4)

            for (x, y, w, h) in faces:
                face_box_gray = gray[y:y + h, x:x + w]
                face_box_color = frame[y:y + h, x:x + w]
                cv2.imwrite("detected_face.jpg", face_box_gray)

                color = (0, 0, 255)
                stroke = 2
                end_coord_x = x + w
                end_coord_y = y + h
                cv2.rectangle(frame, (x, y), (end_coord_x, end_coord_y), color, stroke)

            cv2.imshow('Video Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("~Terminating Window")
                time.sleep(0.5)
                break


cam1 = Camera(0)
cam2 = Camera(1)


def main():

    time.sleep(0.5)
    cam1.startFaceDetect()
    print("---- Thank you for using this software! ----")


main()
