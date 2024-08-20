import cv2
import Camera
import Black_Ramp_Detection
import Blue_Ramp_Detection
cap = cv2.VideoCapture(0)
# Create a new instance of the Camera class sss
cam = Camera.Camera()
Black = Black_Ramp_Detection.BlackColorCamera()
Blue = Blue_Ramp_Detection.BlueColorCamera()
# Call the capture_orange_color_video() method
while True:
    cam.capture_orange_color_video(cap)
    Black.capture_Black_color_video(cap)
    Blue.BlueRmap(cap)







    # Press `q` to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break