#   SECJ3563-06 COMPUTATIONAL INTELLIGENCE    #
#                   PROJECT                   #
# ------------------GROUP 9------------------ #
# 1. Chong Jing Wen      A21EC0170            #
# 2. Kristy Yap Jing Wei A21EC0191            #
# 3. Ooi Joo Yee         A21EC0218            #
# 4. Wai Jia Wen         A21EC0139            #

import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv
from tkinter import NW, Image, filedialog
from PIL import ImageTk,Image
from tkinter import (Tk, ttk, Label, Button, Canvas, HORIZONTAL)
import matplotlib.pyplot as plt

class WasteClassification(Tk):

    def __init__(self):
        super().__init__()
        self.manipulationMenu()

    #----- GUI -----
    def manipulationMenu(self):
        # set title of window
        self.title('Waste Classification Application')
        # set the size of window
        self.geometry("600x600+50+50")
        self.setupMenu()
    
    def setupMenu(self):
        # set up the widgets
        # title
        title = Label(self, text="Waste Classification Application", font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(self, orient=HORIZONTAL)
        line.pack(fill='x')

        empty_line = Label(self, text=""); empty_line.pack() # an empty line

        ## display recycle image
        canvas = Canvas(self, width = 550, height = 300)
        canvas.pack()
        im = ImageTk.PhotoImage(Image.open("./images/recycle.webp"))
        canvas.create_image(0,0, anchor=NW, image=im)
        canvas.image = im

        empty_line = Label(self, text=""); empty_line.pack() # an empty line

        ## choose file to upload
        imageFile_label = Label(self, text="Please select an image file for waste classification.", font=('Helvetica', 14), bd=10)
        imageFile_label.pack(anchor='w')

        selectImage_button = Button(self, text="Select Image", font=('Helvetica', 11), width=10, command=self.openImageFile, fg='white', background='green', activebackground='lightgreen') # button to prompt image file upload
        selectImage_button.pack(anchor='w', padx=10)

    # open image file
    def openImageFile(self):
        self.filename = filedialog.askopenfilename(initialdir='./images', title='Select an image for waste classification')
        self.raw_img = cv.imread(self.filename)
        self.img = self.raw_img.copy()
        self.predict_func(self.img)

    # prediction
    def predict_func(self, img): 
        self.img = cv.resize(self.img, (224, 224))
        img_copy = self.img
        self.img = np.reshape(self.img, [-1, 224, 224, 3])
        result = np.argmax(model.predict(self.img))
        if result == 0: self.display("Recyclable", img_copy)
        elif result ==1: self.display("Organic", img_copy)

    # display image
    def display(self, result, image):
        fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), tight_layout=True, num = 'Classification Result')
        axs.imshow(image[:,:,::-1])
        axs.set_title(result)
        axs.axis("off")

        plt.show()

model = load_model('my_modelVGGNet.h5')

if  __name__  ==  "__main__":
    app = WasteClassification()
    app.mainloop()