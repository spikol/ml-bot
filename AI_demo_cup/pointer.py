from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import glob
import os

# Load the model
model = load_model('/Users/xavier/Documents/Fable/My Fable Projects/AI_demo/keras_model.h5')

# Load labels
with open ('/Users/xavier/Documents/Fable/My Fable Projects/AI_demo/labels.txt', 'r') as f:
    class_labels = f.read().split('\n')

while True:
    if api.isPressed('spacebar'):
        
        api.setFaceEmotion(emotion='Neutral')
        api.setPos(0, 0, 'AMT')
        api.setSpeed(100, 100, 'AMT')
        list_of_files = glob.glob('/Users/xavier/Documents/Fable/My Fable Pictures/*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        os.remove(latest_file)

        # import the picture 
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        api.takePicture(temp=False, ignoreStorageLimit=False)
        api.wait(1)
        list_of_files = glob.glob('/Users/xavier/Documents/Fable/My Fable Pictures/*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        
        image = Image.open(latest_file)
        
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        
        
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        
        # run the inference
        prediction = model.predict(data)
        index = np.argmax(prediction)
        name  = class_labels[index]
        
        print(name)
        #print(index)
        print(prediction)
        
        
        # the pointer
        # Describe this function...
        
        if index == 1:
            api.playSound("woof.wav", 'Face')
            api.setFaceFocus(focusX=0.5, focusY=0.5, focusZ=-0.5, eyeToChange='both')
            api.setPos(45, -45, 'AMT')
            api.setSpeed(100, 100, 'AMT')
        
        # Describe this function...
        
        if index == 0:
            api.playSound("fart1.wav", 'Face')
            api.setFaceAnimation(animation='Happy')
            api.setFaceFocus(focusX=0.5, focusY=-0.5, focusZ=-0.5, eyeToChange='both')
            api.setPos(-45, -45, 'AMT')
            api.setSpeed(100, 100, 'AMT')



