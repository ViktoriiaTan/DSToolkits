# Milestone 1 Report
 
## Task 1

The MNIST dataset is a widely-used collection of handwritten digits for training machine learning models in image classification.
It combines images from NIST's Special Databases 1 and 3: SD-1, featuring complex digits from high school students, and SD-3, with clearer digits from Census Bureau employees.

**Is it a classification or regression problem?**

The dataset presents a classification problem, specifically aimed at identifying and categorizing handwritten digits from 0 to 9 by analyzing patterns in the image pixel data.

**What are the characteristics of the data set?**

- Contains 60,000 training images and 10,000 testing images, each of which is a grayscale image of size 28x28 pixels.
- The pixel values are stored as unsigned bytes (0 to 255), where 0 - white background, 255 -black foreground.
- Data files are stored in a specific IDX file format, designed for vectors and multidimensional matrices.
- Metadata such as magic numbers and sizes in each dimension are also included.

## Task 4 
**Explain in detail which steps were necessary to run the code**

In our virtual machine, the python version needed to be clarified first:
`sudo apt update`  
`sudo apt install python3`  
We decided to use python 3, as it is the currently recommended version.

In our case, pip was not installed either:
`sudo apt install python3-pip`  

Dependencies needed to be installed as well, which can be found in *requirements.txt*:
`pip install -r requirements.txt`  


**Find out what versions are being used to run the code (python version and all dependencies)**

Our machine runs 
- python 3.10.12 
- pip 22.0.2
- numpy 1.23.5
- tensorflow 2.14.0

These were included in *requirements.txt*.


**Are the versions dependent on the system the code is being run on? (try running it on different machines, by checking out the code onto these machines. Does it work out of the box?)** 

We ran the code on different operating systems: Ubuntu, macOS, and Windows, and encountered some dependency issues. The code didn’t work "out of the box" across all systems.  
Libraries (in our case TensorFlow and NumPy), along with the Python version, needed to be compatible and well-matched for successful code execution.   
TensorFlow, for example, has problems with Python 3.12 compatibility, therefore the versions used had to be changed.  


## Task 5

This code represents a system pipeline for handwritten digit classification utilizing the MNIST dataset within the TensorFlow framework using the Keras API.

**What is the input to and the output from the neural network?**

The input is 60000 images and their labels (10 categories), as described in *Task 1*. Specifically, the images are 28x28 pixels in size, each pixel with a value representing greyscale, scaled. (input_shape, /255) The input array is shape is also defined (making sure each pixel has a greyscale value).
The output is labels for the 10000 test images, status messages and metrics of the model's performance (epochs, accuracy, loss).


**What is Keras? And how does it relate to Tensorflow?**

Keras is a deep learning API running on the machine learning platform Tensorflow, which offers simplicity for coders to create their machine learning scripts. Among other benefits, it is easy to implement, provides deployability and easy maintenance.

As mentioned, it is closely tied with TensorFlow, an "end-to-end" platform for various machine learning implementations. 


**How is the data loaded?**

MNIST is part of the datasets included in the Keras library. It is already divided into training and test data. 


**Which dependencies are imported?**

Dependencies such as Numpy and various TensorFlow modules are imported to enable numerical operations and neural network functionality.  
The libraries are: 
- numpy package
- tensorflow.keras module
- tensorflow.keras.layers submodule
- tensorflow.keras.datasets.mnist submodule (dataset)


**What kind of neural network architecture are you dealing with?**

A Convolutional Neural Network (CNN) model is constructed, comprising layers such as convolutional, pooling, and dense layers. This architecture is optimized for extracting hierarchical features from image data, essential for accurate classification tasks.

The model trains by going through the whole dataset 15 times (epochs). 
In each epoch, it processes 128 images at a time (batch size), updating its knowledge each time. It uses a specific method (categorical cross-entropy loss and Adam optimizer) to improve its predictions based on the training.

Finally, the model is tested to see how well it works on new data, measuring its accuracy and mistakes, showing if it’s ready for practical use in recognizing handwritten digits.


## References

1) https://keras.io/
2) https://www.tensorflow.org/
3) https://keras.io/api/datasets/
4) https://keras.io/api/datasets/mnist/#load_data-function
5) http://yann.lecun.com/exdb/mnist/
6) https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/
7) https://medium.com/data-science-365/acquire-understand-and-prepare-the-mnist-dataset-3d71a84e07e7
