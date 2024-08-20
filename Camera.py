import cv2
import numpy as np

class Camera:
    def __init__(self):
        # Initialize the variables
        self.cap = cv2.VideoCapture(0)
        self.orange_image = None
        self.prevCircle = None
        self.dist = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2

    def capture_orange_color_video( self , cap ):
        # Capture the frame
        ret, frame = cap.read()

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the orange color in HSV
        lower_orange = np.array([11, 120, 70])
        upper_orange = np.array([32, 255, 255])

        # Create a mask for the orange color
        orange_mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)

        # Apply the mask to the original frame to extract the orange color
        self.orange_image = cv2.bitwise_and(frame, frame, mask=orange_mask)

        ##########################
        grayFrame = cv2.cvtColor(self.orange_image, cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.GaussianBlur(grayFrame, (17, 17), 0)

        circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.4, 100,
                                param1=100, param2=30, minRadius=5, maxRadius=400)

        if circles is not None:

            circles = np.uint16(np.around(circles))
            chosen = None

            for i in circles[0, :]:
                if chosen is None: chosen = i
                if self.prevCircle is not None:
                    if self.dist(chosen[0], chosen[1], self.prevCircle[0], self.prevCircle[1]) <= self.dist(i[0], i[1], self.prevCircle[0], self.prevCircle[1]):
                        chosen = i
            cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
            cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (0, 100, 100), 3)

        ##########################
        # Display the original and orange images
        # video_writer.write(frame)
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Orange Frame", self.orange_image)

        # Press `q` to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return


    def release(self):
        # Release the resources
        self.cap.release()
        cv2.destroyAllWindows()

