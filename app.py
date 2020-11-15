import cv2
 
img = cv2.imread('/opencv_app/open_cv.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
# gray scale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

#treshold

retval, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#cv2.imshow("Resized image", threshold)

cv2.imwrite("/opencv_app/open_cv_resized.jpg",resized)
cv2.imwrite("/opencv_app/open_cv_gray.jpg",gray)
cv2.imwrite("/opencv_app/open_cv_threshold.jpg",threshold)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
