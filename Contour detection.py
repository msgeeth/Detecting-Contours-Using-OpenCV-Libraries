import cv2

image = cv2.imread(r'C:\Users\Lenovo\Desktop\sample.jpg')
#covert in into grayscale 
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# APPLY BINARY THRESHOLDING
ret, thresh = cv2.threshold(img_gray, 150, 225, cv2.THRESH_BINARY)

# Show the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thresh.jpg', thresh)
cv2.destroyAllWindows()

# Detect contours on the binary image
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# Create a copy of the original image for drawing contours
image_copy = image.copy()  # This line creates the image_copy variable

# Draw contours on the copy
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(112, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# Show the result with contours
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
