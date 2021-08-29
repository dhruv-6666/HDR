from tkinter import *
import numpy
from tkinter import filedialog
from PIL import Image, ImageOps
import matplotlib.pyplot as plt 


import tensorflow as tf

def pre(event = None):
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    pix = numpy.array(image)
    
    plt.imshow(pix)
    plt.show()

    model = tf.keras.models.load_model("MODEL")
    pred = model.predict(pix.reshape(1,28,28,1))
    print("\n\nPrediction = " + str(pred.argmax()))
	



root = Tk()
root.title("Digit Recognizer")

frame = Frame(root, width = 640, height = 480, bg = 'white')
frame.pack()

butt = Button(frame, text = 'UPLOAD!!!!', command = pre)
butt.pack()


root.mainloop()