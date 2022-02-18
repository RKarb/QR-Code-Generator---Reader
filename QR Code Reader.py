import cv2

n = cv2.QRCodeDetector()
val,_,_=n.detectAndDecode(cv2.imread("Hol'up, wait a minute.jpg"))
print("Decoded QRCode is: ",val)