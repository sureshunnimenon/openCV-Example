import cv2
img = cv2.imread('galaxy.jpg',0)

print(type(img))
print(img)

# resize the image

resized_img = cv2.resize(img, (900,600))

# display image

cv2.imshow('image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# display the properties of image

print(img.shape, img.ndim)