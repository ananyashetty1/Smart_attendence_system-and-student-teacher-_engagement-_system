import csv
import cv2
import os
from cv2 import VideoCapture
from cv2 import waitKey


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if(is_number(Id) and name.isalpha()):
        # Try opening camera. On macOS prefer AVFoundation backend.
        cam = None
        try:
            cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
        except Exception:
            cam = cv2.VideoCapture(0)

        if not cam or not cam.isOpened():
            print("\nError: Could not open the camera.")
            print("- If you're on macOS, check System Settings → Privacy & Security → Camera and allow access for Terminal/Python.")
            print("- Make sure no other application (Zoom/Teams/Photo Booth) is using the camera.")
            return
        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            if not ret or img is None:
                print("\nError: Camera frame not received (ret=False or frame is None).")
                print("Check camera permissions and that no other app is using the camera.")
                break
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum = sampleNum+1

                cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
            
