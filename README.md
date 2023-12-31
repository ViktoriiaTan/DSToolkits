# Convolutional neural network on the MNIST dataset

This project focuses on setting up and running a Convolutional Neural Network (mnist_convnet.py) to recognize handwritten digits using the MNIST dataset.

## Instructions to run the script:

### Python installation

Ensure Python (version 3.9 - 3.11) is already installed on your system.   
To check the version installed, use the command:  
`python3 –version`  

If Python is not installed, follow the instructions below based on your operating system:  

**Ubuntu Linux:**
`sudo apt update`  
`sudo apt install python3`  
`sudo apt install python3-pip`  

**MacOS:**
You can download Python from [here](https://www.python.org/downloads/macos/).   
Open terminal and verify the installation:  
`python3 --version`  
`pip3 –version`  

**Windows:**
You can download the appropriate version of Python for your system from the this [link](https://www.python.org/downloads/windows/).  
Ensure that you check the box that says "Add Python 3.x to PATH" before clicking "Install Now".  
Open command prompt and verify the installation:  
`python --version`  
`pip –version`  

### Git installation

1. Make sure Git is installed on your system: `git --version`  
If you don’t have Git installed, you can download it from [here](https://git-scm.com/downloads).  

**For Ubuntu run:** `sudo apt-get install git`  

2. Clone the repository from GitHub to your local machine:  
`git clone https://github.com/ViktoriiaTan/DSToolkits.git`  

### Docker installation 

Ensure Docker is installed. Check with `docker --version`.  
If not installed, follow the instructions from [Docker's official website](https://docs.docker.com/engine/install/)  and [for the compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

### Setup and execution

**Dockerized environment (recommended):**

1. Navigate to the project directory:`cd DSToolkits`   
2. Build and run the Docker images: `docker compose run --build`  
------------------------------------------------------------------------------------
**Local environment (optional):**

1. Create Virtual Environment (optional but recommended):  

`python3 -m venv myenv`    and activate:  

**For macOS and Linux:** `source myenv/bin/activate`  

**For Windows:** `.\myenv\Scripts\activate`  

2. Install the necessary packages listed in requirements.txt:     `pip install -r requirements.txt`  

3. Run the script:    `python3 main.py`  

4. Deactivate Virtual Environment when done:   `deactivate`
