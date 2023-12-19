import cv2

# Configurable Parameters
source = "hero-min.jpg"
destination = "hero-min-1.jpg"
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

dsize = (width, height)

output = cv2.resize(image, dsize)

cv2.imwrite(destination, output)
# cv2.waitKey(0)
