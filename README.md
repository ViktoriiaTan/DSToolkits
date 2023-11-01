## Convolutional neural network on the MNIST datase

This project focuses on setting up and running a Convolutional Neural Network (mnist_convnet.py) to recognize handwritten digits using the MNIST dataset.

#### Instructions to run the script

- Ensure Python (version up to 3.11.6) is already installed on your system. 
To check the version installed, use the command:
`python3 –version`

If Python is not installed, follow the instructions below based on your operating system:
###### Ubuntu Linux:

`sudo apt update`
`sudo apt install python3`
`sudo apt install python3-pip`

###### MacOS:
You can download Python from [here](https://www.python.org/downloads/macos/). 
Pip is included automatically.
Open terminal and verify the installation:
`python3 --version`
`pip3 –version`

###### Windows:
You can download the appropriate version of Python for your system from the this [link](https://www.python.org/downloads/windows/).
Open the downloaded file to start the installation process. 
Ensure that you check the box that says "Add Python 3.x to PATH" before clicking "Install Now". 
Pip is included automatically. 
Open command prompt and verify the installation:
`python --version`
`pip –version`

- Make sure Git is installed on your system: `git --version`
If you don’t have Git installed, you can download it from [here](https://git-scm.com/downloads).  
For Ubuntu run: `sudo apt-get install git`

- Clone the repository from GitHub to your local machine:

`git clone https://github.com/ViktoriiaTan/DSToolkits.git`

- Change your directory to the location where the script mnist_convnet.py is located
`cd DSToolkits/script`

- Create Virtual Environment (optional but recommended)
`python3 -m venv myenv`
and activate:

###### For macOS and Linux: 
`source myenv/bin/activate`

###### For Windows:
`.\myenv\Scripts\activate`

- Install the necessary packages listed in requirements.txt.
`pip install -r requirements.txt`

- Run the script:
`python3 mnist_convnet.py`

- Deactivate Virtual Environment when done
`deactivate`
