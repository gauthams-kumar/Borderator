<p align="center">
  <img width="100"  src="/Resources/borderator.png">
</p>

# Borderator
A lightweight python application for adding predictable borders to images.

### Abstract

It can be frustrating to add visually consistent borders to images quickly. Most approaches will require manual calculation or processing images one by one, and others will produce visual inconsistencies between images that were meant to look cohesive.

*Borderator* rapidly adds borders to batches or individual images at a reliable, user-specified aspect ratio and thickness. It preserves original orientation and, if desired, aspect ratio for an even border. Regardless of resolution, input file type, and output file type, bordered images from the same recipe will have a unified appearance without needing to open images or lean on prior calculations.

### Usage
This script adds borders to images, allowing the user to:
* Target an original image or folder by its path
* Specify border attributes to be added:
    * Colour (either hex or Tkinter color)
    * Aspect ratio, including the original aspect ratio
    * Minimum margin thickness (in percent)
* Specify output filetype
* Save new images as high-quality JPEG files in a  `/bordered` directory without any discernible loss in quality
* Maintain visual consistency between images processed using the same recipe