▎Image Enhancement Tool

This project is a simple tool for image enhancement written using OpenCV and NumPy. This tool allows you to improve images with a white background and without noise.

▎Features

• Convert image to grayscale

• Thresholding the image to separate objects from the background

• Create a final image with a white background

▎Requirements

To run this code, you need the following libraries:

• OpenCV

• NumPy

You can install these libraries using pip:
```bash
pip install opencv-python numpy
```

▎How to Use

1. Save the code in a Python file (for example, image_enhancer.py).

2. In the terminal, navigate to the directory where you saved the file.

3. Run the code:
   
```bash
      python image_enhancer.py
```   

5. You will be prompted to enter the path of the input image, the name of the output image, and the threshold number.

6. The enhanced image will be saved at the specified path.

▎Example
```
Enter your photo: path/to/your/image.jpg
Enter name of your scanned photo: enhanced_image
Enter the number of thresh (Suggested number 80): 80
```

In this example, the input image is located at path/to/your/image.jpg, and the output image will be saved as enhanced_image.jpg.

▎Notes

• It is recommended to choose the threshold number between 0 and 255. The suggested value is 80.

• Make sure that the input image exists and is loadable.

---

Thank you for using this tool! If you have any questions or feedback, please feel free to raise them in the Issues section on GitHub.
