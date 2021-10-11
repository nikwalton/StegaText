# StegaText
A text editor to hide text via steganographic methods - CPTS 427 Class project


## Requirements
Python

### Packages used
PyQt5
Pillow

## installation
Instsall the packages listed in requriements.txt either in a python virtual environment or locally.

## Running
to run the application, once the python packages have been installed on your environemnt of choice run
```python3 App.py``` to run the GUI application

once the GUI application is running you will presented with a text box and some menu items at the top of the window.
You are then able to write text into the text box and save to a image file using File->Encode Image. Additionally you can decode text from an image and display it using File->Decode image.

Text will not self delete once you encode to an image file, so make sure to delete any text left in the text box before reading a encoded image's text.

Encoding to Audio, and using symmetric key encryption is not supported for Milestone 1, will be added for milestone 2.

