import cv2
import numpy as np
from time import sleep
import db_connection


def run_counter():
    db = db_connection.mycursor

    latitude_min = 80
    altitude_min = 80

    offset = 6

    line_pos = 250

    delay = 60

    detections = []
    cars = 0

    def get_center(x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx, cy

    def get_video_name():
        db.execute("SELECT VideoName FROM videos ORDER BY id DESC LIMIT 1")
        name = db.fetchone()
        name = str(name).replace("(", "").replace(")", "").replace(",", "").replace("\'", "")
        return name

    cap = cv2.VideoCapture('videos/' + get_video_name() + '.mp4')
    object_detector = cv2.createBackgroundSubtractorMOG2(varThreshold=40)
    videoname = get_video_name()

    while True:
        ret, frame1 = cap.read()
        if ret:
            tempo = float(1 / delay)
            sleep(tempo)
            grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(grey, (3, 3), 5)
            img_sub = object_detector.apply(blur)
            dilate = cv2.dilate(img_sub, np.ones((5, 5)))
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            dilatation = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
            dilatation = cv2.morphologyEx(dilatation, cv2.MORPH_CLOSE, kernel)
            contours, h = cv2.findContours(dilatation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.line(frame1, (0, line_pos), (1920, line_pos), (255, 127, 0), 3)
            for (i, c) in enumerate(contours):
                (x, y, w, h) = cv2.boundingRect(c)
                valid_contours = (w >= latitude_min) and (h >= altitude_min)
                if not valid_contours:
                    continue

                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                center = get_center(x, y, w, h)
                detections.append(center)
                cv2.circle(frame1, center, 4, (0, 0, 255), -1)

                for (x, y) in detections:
                    if y < (line_pos + offset) and y > (line_pos - offset):
                        cars += 1
                        db.execute("INSERT INTO car_single_count (Car_Sequence_No, Video_Name) VALUES(%s,'%s')" % (cars, videoname))
                        cv2.line(frame1, (25, line_pos), (1200, line_pos), (0, 127, 255), 3)
                        detections.remove((x, y))
                        print("car is detected : " + str(cars))

            cv2.putText(frame1, "VEHICLE COUNT : " + str(cars), (150, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.imshow("Video Original", frame1)
            cv2.imshow("Detector", dilatation)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cv2.destroyAllWindows()
    cap.release()

    db.execute("INSERT INTO car_count (CarCount) VALUES (%s)" % cars)
