import cv2
import glob

images = glob.glob("./sample-images/*.jpg")
# print(type(images))
# print(images)

for image in images:
    img = cv2.imread(image,1)
    resized = cv2.resize(img, (1000,1000))

    cv2.imshow('image', resized)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    count = str(images.index(image))

    cv2.imwrite(("./resized/resized_" + count + ".jpg"),resized)
    
    
    



    



