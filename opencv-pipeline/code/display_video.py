import cv2

# 1. Open the video file (replace "sample.mp4" with your video filename)
cap = cv2.VideoCapture(0)

# 2. Check if the video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# 3. Read and display frames in a loop
while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        print("End of video or cannot read frame.")
        break

    cv2.imshow("Video", frame)  # Display the frame

    # 4. Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 5. Release resources
cap.release()
cv2.destroyAllWindows()
