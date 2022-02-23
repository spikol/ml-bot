from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import glob
import os

# Load the model
model = load_model('C:\\Users\\dieuw\\Documents\\Fable\\My Fable Projects\\AI_demo\\keras_model.h5')

# Load labels
with open ('C:\\Users\\dieuw\\Documents\\Fable\\My Fable Projects\\AI_demo\\labels.txt', 'r') as f:
    class_labels = f.read().split('\n')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
#image = Image.open('Cup3.jpeg')

api.takePicture(temp=False, ignoreStorageLimit=False)
api.wait(1)
list_of_files = glob.glob('C:\\Users\\dieuw\\Documents\\Fable\\My Fable Pictures\\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

image = Image.open(latest_file)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
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

if index == 1:
    api.playNote('C4');
    api.spinWheelByMetric('A', 90, 'degrees', '9ZM', 50, abs=False)

if index == 0:
    api.playNote('C4');
    api.spinWheelByMetric('A', -90, 'degrees', '9ZM', 50, abs=False)

