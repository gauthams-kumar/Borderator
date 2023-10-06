"""
BORDERATOR
by Gautham Kumar
"""
version = str(4.4)

from PIL import Image
import os
import sys
import tkinter

"""
TO DO
[x] improve how this thing looks
[x] allow user to choose border colour and set white as default
[x] get square outputs to work
[x] allow borders at original aspect ratio i.e. even borders
[x] batch process based on folder selection
[] allow button click only when everything's filled out
"""
os.chdir(sys.path[0])

window = tkinter.Tk()
window.title(f"Borderator {version}")
window.iconbitmap("Resources/borderator.ico")
window.resizable(False, False)
print(f"This is Borderator {version}")

def runMode():
    inputPath = fpEntry.get().replace('"', '')

    validFiletypes = ".jpg", ".jpeg",".png", ".tiff"

    if os.path.isdir(inputPath):
        for root, dirs, files in os.walk(inputPath):
            for file in files:
                if file.endswith(validFiletypes) and "#BR" not in file:
                    imageRoot = os.path.join(root, file)
                    imagePath = os.path.abspath(imageRoot)
                    print(f"\nAbsolute filepath: {imagePath}")
                    borderate(imagePath)
        print(f"\nBatch borderation complete!")
    elif inputPath.endswith(validFiletypes):
        borderate(os.path.abspath(inputPath))
        print(f"\nBorderation complete!")
    else:
        print(f"\nNo valid images found at/within path")


def borderate(imageFile):
    print(f"Generating bordered image...")

    # establish original characteristics
    originalImage = Image.open(imageFile)
    originalName = os.path.splitext(os.path.basename(imageFile))[0]
    originalDimensions = originalImage.size
    originalSides = {"short": min(originalDimensions), "long": max(originalDimensions)}

    # retrieve desired margin colour, percent added, aspect ratio
    marginColour = marginColourEntry.get()
    marginPercent = float(marginEntry.get())
    aspectX = float(ar1Entry.get())
    aspectY = float(ar2Entry.get())

    # calculate desired aspect ratio
    aspect = aspectX, aspectY
    aspectRatio = max(aspect) / min(aspect) if 0 not in aspect else 1
    usingOriginalAR = True if 0 in aspect else False

    # calculate percent margin in pixels, then minimum necessary image size
    margin = originalSides["short"] * (marginPercent * 0.02)
    marginPlusShort = margin + originalSides["short"]
    marginPlusLong = margin + originalSides["long"]

    # orientation flag
    orientation = "landscape" if originalDimensions[0] > originalDimensions[1] else "portrait"
    if usingOriginalAR:
        print("    0:0 - Giving you a regular border")
        if orientation == "landscape":
            finalDimensions = (round(marginPlusLong), round(marginPlusShort))
        else:
            finalDimensions = (round(marginPlusShort), round(marginPlusLong))
    else:
        # decide which side should have the minimum margin
        preliminaryLong = marginPlusShort * aspectRatio
        if marginPlusLong < preliminaryLong:
            # the margin should be narrowest on the short side
            finalShort = round(marginPlusShort)
            finalLong = round(finalShort * aspectRatio)
        else:
            # the margin should be narrowest on the long side
            finalLong = round(marginPlusLong)
            finalShort = round(finalLong / aspectRatio)
        # pair dimensinos up for orientation
        if orientation == "landscape":
            finalDimensions = (finalLong, finalShort)
        else:
            finalDimensions = (finalShort, finalLong)

    print(f"    Output dimensions (px): {finalDimensions[1]} * {finalDimensions[0]}")

    # OUTPUT
    borderedImage = Image.new("RGB", finalDimensions, marginColour)
    pasteX = int((finalDimensions[0] - originalDimensions[0]) / 2)
    pasteY = int((finalDimensions[1] - originalDimensions[1]) / 2)
    borderedImage.paste(originalImage, (pasteX, pasteY))

    saveDir = os.path.dirname(imageFile) + "\\bordered"
    saveName = f"{originalName} #BR({round(marginPercent)}%; {round(max(aspect))}-{round(min(aspect))})"
    saveName += filetypeEntry.get()

    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
        print(f"    created '\\bordered' directory")

    fullSavePath = saveDir + "\\" + saveName
    borderedImage.save(fullSavePath, format="JPEG", quality=100, subsampling=0)

    successMessage = f"    Exported '{saveName}' with a {marginPercent}% {marginColour} border"
    if finalDimensions[0] == finalDimensions[1]:
        successMessage += " at aspect ratio 1:1, square"
    elif usingOriginalAR:
        successMessage += " at the original aspect ratio"
    elif orientation == "landscape":
        successMessage += f" at aspect ratio {max(aspect)}:{min(aspect)}"
    else:
        successMessage += f" at aspect ratio {min(aspect)}:{max(aspect)}"
    print(successMessage)


# GUI ELEMENTS
logoImage = tkinter.PhotoImage(file="Resources/logo.png").zoom(1, 1)
logoLabel = tkinter.Label(window, image=logoImage)

# short dimension
fpLabel = tkinter.Label(window, text="Target file/folder path")
fpEntry = tkinter.Entry(window)

# margin entry
marginLabel = tkinter.Label(window, text="Minimum margin (%)")
marginEntry = tkinter.Entry(window)
marginEntry.insert(0, '5')

# margin colour
marginColourLabel = tkinter.Label(window, text="Border colour")
marginColourEntry = tkinter.Entry(window)
marginColourEntry.insert(0, 'white')

# aspect ratio
arLabel = tkinter.Label(window, text="Output aspect ratio")
ar1Entry = tkinter.Entry(window, width=5, justify="center")
aspectSeparatorLabel = tkinter.Label(window, text=":")
ar2Entry = tkinter.Entry(window, width=5, justify="center")
ar1Entry.insert(0, '1')
ar2Entry.insert(0, '1')

# filetype
filetypeLabel = tkinter.Label(window, text="Output filetype")
filetypeEntry= tkinter.Entry(window, relief="flat")
filetypeEntry.insert(0, '.jpg')

# button
borderateImage = tkinter.PhotoImage(file="Resources/button.png").zoom(1, 1)
borderateButton = tkinter.Button(window, text="BORDERATE", command=runMode, bg="deep pink",
                            activebackground="black", image=borderateImage, relief="flat", borderwidth=8)

# instructions
inst0 = tkinter.Label(window, text="Specify either a target file or folder")
inst1 = tkinter.Label(
    window, text="Margin colour in hex or Tkinter name")
inst2 = tkinter.Label(window, text="Enter 0:0 for a regular border")

# spacers
spacer0 = tkinter.Label(window, text="")
spacer1 = tkinter.Label(window, text="")

# GUI GRID
window.configure(bg='#202020')

for child in window.winfo_children():
    child.grid_configure(padx=(10,10), pady=(0,10))
    if 'Label' in str(child.winfo_class):
        child.configure(bg='#202020', fg="white")
    elif 'Entry' in str(child.winfo_class):
        #child.grid_configure(padx=(10,10))
        child.configure(bg='#101010', fg="white", highlightthickness=1, highlightbackground = "#535353", highlightcolor= "#939393", borderwidth=8, relief="flat", insertbackground='deep pink')


logoLabel.grid(column=0, row=1, columnspan=2, pady=(20,20))

fpLabel.grid(column=0, row=2, sticky=tkinter.E)
fpEntry.grid(column=1, row=2)

marginLabel.grid(column=0, row=3, sticky=tkinter.E)
marginEntry.grid(column=1, row=3)

marginColourLabel.grid(column=0, row=4, sticky=tkinter.E)
marginColourEntry.grid(column=1, row=4)

arLabel.grid(column=0, row=5, sticky=tkinter.E)
ar1Entry.grid(column=1, row=5, sticky=tkinter.W)
aspectSeparatorLabel.grid(column=1, row=5)
ar2Entry.grid(column=1, row=5, sticky=tkinter.E)

filetypeLabel.grid(column=0, row=6, sticky=tkinter.E)
filetypeEntry.grid(column=1, row=6)

spacer0.grid(column=0, row=7, pady=(0,0))
inst0.config(fg='gray')
inst1.config(fg='gray')
inst2.config(fg='gray')
inst0.grid(column=0, row=8, columnspan=2, sticky='nesw', pady=(0,0),)
inst1.grid(column=0, row=9, columnspan=2, sticky='nesw', pady=(0,0))
inst2.grid(column=0, row=10, columnspan=2, sticky='nesw', pady=(0,0))

spacer1.grid(column=0, row=11, pady=(0,0))

borderateButton.grid(column=0, row=12, columnspan=2, sticky='nesw', pady=(0,10))

# MAINLOOP FOREVER
window.mainloop()

"""
Borderator
Copyright (C) 2021 Gautham Kumar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""