import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    #  ret is True/False, If the frame is read correctly, it will be True
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    # 1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
    # 2.waitKey(1) will wait for keyPress for just 1 millisecond and it will continue to refresh and read frame from your webcam using cap.read().
    if cv2.waitKey(1) == ord('q'):
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()