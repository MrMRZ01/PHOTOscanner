import cv2
import numpy as np
import re

def enhance_image(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    if image is None:
        print("Error: Image not found or unable to load.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray_image, thresh_number, 255, cv2.THRESH_BINARY)


    mask = cv2.bitwise_not(thresh_image)


    white_background = np.ones_like(image) * 255


    final_image = np.where(mask[:, :, np.newaxis] == 255, image, white_background)


    cv2.imshow("Final Image", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    cv2.imwrite(output_image_path, final_image)


input_path = input("Enter your photo: ")
output_path = input("Enter name of your scanned photo: ")
thresh_number = int(input('Enter the number of thresh(Suggested number 80): '))
regex = r'.(jpg|jpeg|png)$'
if not re.search(regex, output_path):
    output_path += ".jpg"

enhance_image(input_path, output_path)
