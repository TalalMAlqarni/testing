import cv2
import numpy as np
class BlackColorCamera:
    def __init__(self):
        # Initialize the variables
        self.cap = cv2.VideoCapture(0)
        self.black_image = None

    def capture_Black_color_video(self , cap):
       

            # Capture the frame
            ret, frame = cap.read()

            # Convert the frame to HSV color space
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define the lower and upper bounds of the black color in HSV
            lower_black = np.array([0, 0, 0])
            upper_black = np.array([60, 50, 100])

            # Create a mask for the black color
            black_mask = cv2.inRange(hsv_frame, lower_black, upper_black)

            # Apply the mask to the original frame to extract the black color
            black_image = cv2.bitwise_and(frame, frame, mask=black_mask)
            
            cv2.imshow("Black Frame",black_image)

    # def get_black_area(self):
    #     area_black = np.sum(self.black_image)
    #     return area_black

    # def is_black_present(self):
    #     area_black = self.get_black_area()
    #     if (area_black > 1800000):
    #         return True
    #     else:
    #         return False

    def release(self):
        # Release the resources
        self.cap.release()
        cv2.destroyAllWindows()


