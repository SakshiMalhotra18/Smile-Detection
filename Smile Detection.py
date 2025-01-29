import cv2
import os

# Load the face and smile detector models
face_detector_path = os.path.join(os.getcwd(), 'haarcascade_frontalface_default.xml')
smile_detector_path = os.path.join(os.getcwd(), 'haarcascade_smile.xml')

face_detector = cv2.CascadeClassifier(face_detector_path)
smile_detector = cv2.CascadeClassifier(smile_detector_path)

# Initialize webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read the current frame from the webcam
    successful_frame_read, frame = webcam.read()

    # If there is an error, abort
    if not successful_frame_read:
        break

    # Convert frame to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_detector.detectMultiScale(frame_grayscale, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50), 4)
        
        # Get the face region of interest (ROI)
        the_face = frame[y:y+h, x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        
        # Detect smiles within the face ROI
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
        
        for (x_, y_, w_, h_) in smiles:
            cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 4)
        
        if len(smiles) > 0:
            cv2.putText(frame, 'Smiling', (x, y + h + 40), fontScale=2, 
                        fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, color=(250, 250, 250))
    
    # Display the frame
    cv2.imshow('Smile Detector', frame)
    
    # Break loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()

print('Smile Detection Completed')
