import cv2

# Load the face detector model
face_detector_path = r'C:\Users\saksh\Desktop\pythonProject\START AGAIN\haarcascade_frontalface_default.xml'
face_detector = cv2.CascadeClassifier(face_detector_path)


smile_detector_path = r'C:\Users\saksh\Desktop\pythonProject\START AGAIN\haarcascade_smile.xml'
smile_detector = cv2.CascadeClassifier(smile_detector_path)

# Initialize webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read the current frame from the webcam
    successful_frame_read, frame = webcam.read()

    # If there is an error, abort
    if not successful_frame_read:
        break

    # # Change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    # # Detect faces
    faces = face_detector.detectMultiScale(frame_grayscale)
    # smiles = smile_detector.detectMultiScale(frame_grayscale)


    # print(faces)


    #Run face detection within those faces

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50), 4)

        #Get the sub frame using numpy N-dimensional array slicing

        the_face = frame[y:y+h, x: x+w]

        # Change to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # Detect faces
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        for (x_, y_, w_, h_) in smiles:
            cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 4)
            # pass  # draw all the rectangles along the smile

    # Draw rectangles around detected faces
    for (x, y, w, h) in smiles:
        cv2.rectangle(the_face, (x, y), (x + w, y + h), (50, 50, 200), 4)


        if len(smiles)>0:
            cv2.putText(frame,'smiling',(x,y+h+40), fontScale=2, fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, color=(250,250,250))
    # Show the frame
    cv2.imshow('Smile Detector', frame)

    # waitkey
    cv2.waitKey(1)

# Release resources
webcam.release()
cv2.destroyAllWindows()

print('Code Completed')

