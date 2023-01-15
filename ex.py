from tkinter import *
from PIL import Image

img = Image.open("images/login2.png")
img = img.convert("RGBA")
img.putalpha(128)
img.save("transparent_image.png")

root = Tk()

# Create a PhotoImage object for the image
image = PhotoImage(file="transparent_image.png")

# Create a label to display the image
label = Label(root, image=image)

# Pack the label
label.pack()

root.mainloop()

