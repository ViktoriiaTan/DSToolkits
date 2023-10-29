# Milestone 1 Report

## Task 1
**Is it a classification or regression problem?**

**What are the characteristics of the data set?**



## Task 4 
**Explain in detail which steps were necessary to run the code**

In our virtual machine, the python version needed to be clarified:
´sudo apt update´
´sudo apt install python3´
We decided to use python 3, as it is the currently recommended version.

pip was not installed either:
´sudo apt install python3-pip´
Requirements needed to be installed as well, which can be found in *requirements.txt*:
´pip install -r requirements.txt´


**Find out what versions are being used to run the code (python version and all dependencies)**

Our machine runs 
- python 3.10.12 
- pip 22.0.2
- numpy 1.23.5
- tensorflow 2.14.0

These were all added to *requirements.txt*.


**Are the versions dependent on the system the code is being run on? (try running it on different machines, by checking out the code onto these machines. Does it work out of the box?)** 




## Task 5

**What is the input to and the output from the neural network?**

The input is 60000 images and their labels (10 categories), as described in *Task 1*. Specifically, the images are 28x28 pixels in size, each pixel with a value representing greyscale, scaled. (input_shape, /255) The input array is shape is also defined (making sure each pixel has a greyscale value)
The output is labels for the 10000 test images, status messages and metrics of the model's performance (epochs, accuracy, loss).


**What is Keras? And how does it relate to Tensorflow?**

Keras is a deep learning API running on the machine learning platform Tensorflow, which offers simplicity for coders to create their machine learning scripts. Among other benefits, it is easy to implement, provides deployability and easy maintenance.

As mentioned, it is closely tied with TensorFlow, an "end-to-end" platform for various machine learning implementations. 


**How is the data loaded?**

MNIST is part of the datasets included in the Keras library. It is already divided into training and test data. 


**Which dependencies are imported?**

The libraries: 
- numpy package
- tensorflow.keras module
- tensorflow.keras.layers submodule
- tensorflow.keras.datasets.mnist submodule (dataset)


**What kind of neural network architecture are you dealing with?**


## References

1) https://keras.io/
2) https://www.tensorflow.org/
3) https://keras.io/api/datasets/
4) https://keras.io/api/datasets/mnist/#load_data-function

