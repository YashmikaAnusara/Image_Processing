import cv2

# Show the Image
# img = cv2.imread("image/Pic.jpg");
# print(img)
# cv2.imshow("Test", img)
# cv2.waitKey(0);

# Video Input
# vi = cv2.VideoCapture(0)
# while True:
#     success, vi2 = vi.read();
#     cv2.imshow("video",vi2)
#     if cv2.waitKey(1)& 0xFF==ord('s'):
#         break

# Face Detection with camera
# face_para = cv2.CascadeClassifier('Body_Parameters/haarcascade_frontalface_default.xml')
# print("Read Face Parameter...")
# cam = cv2.VideoCapture(0)
# print("Detecting Camera...")
# while True:
#     success, cam_out = cam.read()
#     print("Read the camera...")
#     gray = cv2.cvtColor(cam_out, cv2.COLOR_BGR2GRAY)
#     print("Convert the RGB to Grayscale...")
#     face = face_para.detectMultiScale(gray, 1.1, 4)
#     print("Detecting grayscale image face parameter...")
#     for (x, y, w, h) in face:
#         cv2.rectangle(cam_out, (x, y), (x + w, y + h), (79, 168, 72), 4)
#         cv2.imshow('end_cam', cam_out)
#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             break
# cam.release()

# Face Detection with image
# face_para = cv2.CascadeClassifier('Body_Parameters/haarcascade_frontalface_default.xml')
# image = cv2.imread('image/pic1.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# face = face_para.detectMultiScale(gray, 1.1, 4)
# for (x, y, w, h) in face:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (79, 168, 72),4)
# cv2.imshow('img', image)
# cv2.waitKey()
