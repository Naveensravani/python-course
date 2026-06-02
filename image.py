import cv2

# Load child image
image = cv2.imread("child.jpg")

if image is None:
    print("Child image not found!")
else:
    cv2.namedWindow("Child Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Child Image", 800, 500)

    cv2.imshow("Child Image", image)

    print("Image Dimensions:", image.shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()