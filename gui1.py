from tkinter import *
import numpy
import logging
logging.getLogger("tensorflow").setLevel(logging.WARNING)
from tkinter import filedialog
from PIL import Image, ImageOps, ImageDraw
import matplotlib.pyplot as plt 
import PIL


import tensorflow as tf

def save():
    filename = 'image.png'
    image.save(filename)
    image1 = Image.open(filename)
    image1 = ImageOps.grayscale(image1)
    image1 = ImageOps.invert(image1)
    image1 = image1.resize((28,28))
    pix = numpy.array(image1)

    
    
    plt.imshow(pix)
    plt.show()

    model = tf.keras.models.load_model("MODEL")
    pred = model.predict(pix.reshape(1,28,28,1))
    print("\n\nPrediction = " + str(pred.argmax()))


def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=30)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=30)
	



root = Tk()
root.title("Digit Recognizer")



cv = Canvas(root, width = 280, height = 280, bg = 'white')
# --- PIL
image = PIL.Image.new('RGB', (280, 280), 'white')
draw = ImageDraw.Draw(image)
# ---- 
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)



butt = Button(text = 'PREDICT!!', command = save)
butt.pack()


root.mainloop()