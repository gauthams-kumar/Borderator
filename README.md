# Borderator
A lightweight python application for predictable borders to images

### Abstract

It can be hard to add visually-consistent borders to images quickly. Most approaches will require manual calculation or processing images one by one.

*Borderator* rapidly adds borders to batches or individual images at a consistent, user-specified aspect ratio and thickness. It preserves original orientation and, if desired, aspect ratio for an even border. Regardless of original resolution and file type, output files using the same recipe will have a unified appearance.

### Usage
This script adds borders to images, allowing the user to:
* Target an original image or folder by its path
* Specify border attributes to be added:
    * Colour (either hex or Tkinter color)
    * Aspect ratio, including the original aspect ratio
    * Minimum margin thickness (in percent)
* Save new images as high-quality JPEG files in a  `/bordered` directory without any discernible loss in quality
* Maintain visual consistency between images processed using the same recipe