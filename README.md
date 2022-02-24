# ml-bot
machine learning and robotics

This is a tutorial how to teach machine learing principles with Teachable machine, Tensorflow and fable by shape robotics.

### How To

Fable Blockly is Python 3.8 based software in combination with Blockly by Google. To use the models made by teachable machine or other machine learning models in fable blocky python packages need to be added to the application. In this repository are all the python files or you can download them yourself.

list of packages:

!!! important that these packages are all for Python 3.8 !!!

- tensorflow 2.4.3
- numpy	1.19.2
- Pillow 7.2.0
- xml
- timeit.py

these packages should be places in the following directory:
```Fable.app/Contents/Resources/app.asar.unpacked/prod/app/server```
If there the files already exist in the directory keep the original files.

#### Windows:
- Download the Windows 64-bit version of Fable 2.0.4 from the Shape Robotics sites
- Download the Python 3.8 version of Miniconda3 Windows 64-bit from https://docs.conda.io/en/latest/miniconda.html
  - Select 'Add Miniconda3 to my path environment variable' in the installation process
- Open Anaconda Prompt and create an enviroment for your Fable installation. By using ```conda create --name fable``` command.
- Activate environment using ```conda activate fable```
- Use pip install to install the packages shown above
- Copy the installed packages from the Anaconda Fable enviroment into the program files of the Fable Blockly software.
  - The installed packages are folders and files and can be found in the ```Miniconda3\Lib\site-packages``` folder and are identified by comparing the date modified column with the time the package installation started.
  - The destination is ```C:\Program Files\Fable\resources\app.asar.unpacked\prod\app\server``` 
  - When presented with duplicate files select keep the files already present in the server folder
  - Copy the timeit.py file from the same folder
  - Copy the xml folder to the same folder
  - Copy the unittest folder from the parent folder ```Lib```
- Now the Fable Blockly software is installed to be able to run the pointer code you can find in this repository.
- Fix file names in Python code to own system names

Copy folder ```site-packages.zip``` to be found at https://drive.google.com/file/d/19VvNa9FofgUnf4KDiEXYMXadnasbV6P_/view?usp=sharing into ```C:\Program Files\Fable\resources\app.asar.unpacked\prod\app\server``` this will copy all the required packages for the Fable 2.0.4 software to use. When presented with duplicate files select to keep the old original files.
