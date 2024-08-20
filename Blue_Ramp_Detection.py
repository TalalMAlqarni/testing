import cv2
import numpy as np
class BlueColorCamera:
    def __init__(self):
        # Initialize the variables
        self.cap = cv2.VideoCapture(0)

    def BlueRmap(self,cap):

        ret, frame = cap.read()


        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the orange color in HSV
        lower_black = np.array([100, 100, 0])
        upper_black = np.array([130, 255, 255])

        # Create a mask for the orange color
        black_mask = cv2.inRange(hsv_frame, lower_black, upper_black)

        # Apply the mask to the original frame to extract the orange color
        black_image = cv2.bitwise_and(frame, frame, mask=black_mask)
        

        cv2.imshow("Blue Frame",black_image)
        area_blue = np.sum(black_image)
        if (area_blue > 1800000):
            print("shoot")
            return True
        else:
            print("don't shoot")
            return False

    


    def release(self):
        # Release the resources
        self.cap.release()
        cv2.destroyAllWindows()

