# Borderator
A lightweight python application for predictable borders to images

### Abstract
Without using a web service, there's no lightweight method to add  borders to photos on Windows whilst preserving original image fidelity. One approach is to add borders by expanding the canvas using image processing software, a slow and inconsistent process. As these borders must be specified manually in pixels, this method introduces variability in perceived border thickness and ouput aspect ratio (unless you lean on prior calulcations). This results in borders that vary from photo to photo, especially if the original images have different dimensions to begin with.

This version of Borderator, by contrast, prioritises the user's specification of aspect ratio and border thickness. From these data, the program determines the necessary image dimensions and automatically selects landscape and portrait output based on the source. The result is quick, consistent, and high-quality.

### Usage
This script adds  borders to images, allowing the user to:
* target an original image or folder by its path
* pop that original image in the centre of a new field with arbitrary:
    * colour
    * aspect ratio, including the original aspect ratio
    * short margin thickness i.e. proportional distance from the image edge
* save that new image as a high-quality JPEG file without any discernible loss in quality
* maintain visual consistency between images processed using the same recipe