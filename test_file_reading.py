# Initial notes:
# What about contouring? Could maybe be useful!
# Especially some of the methodology used here: https://www.baeldung.com/cs/computer-vision-contours

from PIL import Image

im_file = "Tunic Rune Samples/Easy (WoB).png"

im = Image.open(im_file)



print(im.size)

#im.show(title="test img")
#im.crop((200,200,1720,880)).show()


