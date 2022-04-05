# ml-bot
machine learning and robotics

This is a tutorial how to teach machine learing principles with Teachable machine, Tensorflow and fable by shape robotics.

### How To

Fable is Python 3.8 based software which builds on Blockly by Google. To use the models made by Teachable Machine or other machine learning models in Fable Python packages need to be added to the application. In this repository the files and packages are bundled or you can download them yourself using the method below.

List of packages and files to be installed:
!!! important that these packages are all for Python 3.8 !!!

- tensorflow 2.4.3
- numpy	1.19.2
- Pillow 7.2.0
- FER
- grpc
- The folder ```xml```
- The file ```timeit.py```

#### MacOS
Copy the packages and files into ```Fable.app/Contents/Resources/app.asar.unpacked/prod/app/server```
If there the files already exist in the directory keep the original files.

#### Windows:
1. Download the Windows 64-bit version of Fable 2.0.4 from the Shape Robotics sites
2. Download the Python 3.8 version of Miniconda3 Windows 64-bit from https://docs.conda.io/en/latest/miniconda.html
3. Select 'Add Miniconda3 to my path environment variable' in the installation process
3. Open Anaconda Prompt and create an environment for your Fable installation. By using ```conda create --name fable``` command.
4. Activate environment using ```conda activate fable```
5. Use pip install to install the packages shown above
6. Copy the installed packages from the Anaconda Fable environment into the program files of the Fable Blockly software.
7. The installed packages are folders and files and can be found in the ```Miniconda3\Lib\site-packages``` folder and are identified by comparing the date modified column with the time the package installation started.
8. The destination is ```C:\Program Files\Fable\resources\app.asar.unpacked\prod\app\server``` 
9. When presented with duplicate files select keep the files already present in the server folder
10. Copy the timeit.py file from the same folder
11. Copy the xml folder to the same folder
12. Copy the unittest folder from the parent folder ```Lib```
13. Now the Fable Blockly software is installed to be able to run the pointer code you can find in this repository.
14. Fix file names in Python code to own system names

Steps 2 through 12 can be skipped by copying the contents of the folder ```site-packages.zip``` to be found at https://drive.google.com/file/d/19VvNa9FofgUnf4KDiEXYMXadnasbV6P_/view?usp=sharing into ```C:\Program Files\Fable\resources\app.asar.unpacked\prod\app\server``` this will copy all the required packages for the Fable 2.0.4 software to use. When presented with duplicate files select to keep the old original files.
