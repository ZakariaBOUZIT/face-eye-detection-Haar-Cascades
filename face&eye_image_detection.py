import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read the input image
img = cv2.imread('testimage.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.5, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    img=cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    img2=img[y:y+h,x:x+h]
    gray2=gray[y:y+h,x:x+h]
    # Detect eyes
    eyes = eye_cascade.detectMultiScale(gray2,1.5,4)
    # Draw rectangle around the eyes
    for (x2, y2, w2, h2) in eyes:
        cv2.rectangle(img2, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()


