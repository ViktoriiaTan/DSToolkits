# Convolutional neural network on the MNIST dataset

This project focuses on setting up and running a Convolutional Neural Network to recognize handwritten digits using the MNIST dataset. This project extends the functionality of the existing handwritten digit classifier by integrating it into a Flask web application. The system includes a REST API that allows users to submit images containing handwritten digits for classification using the trained CNN. Additionally, the Flask app is dockerized, and the database is utilized to store predictions and associated image data.

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

1. To easily start the entire system, use the following command: `docker-compose up`
2. Once the Docker containers are up and running, you can access the front-end by opening a web browser and navigating to [http://localhost:5000](http://localhost:).
3. Using the upload for on the website, select an image containing handwritten digits from your local computer. Follow the on-screen instructions to submit the image.
4. After uploading the image, the neural network will process it, and the prediction for the handwritten digits will be displayed on the web page. Additionally, the uploaded image is shown on the page.
5. The prediction is saved into the database. You can inspect the database based on your configuration.


------------------------------------------------------------------------------------  

**Local environment (optional):**

1. Create Virtual Environment (optional but recommended):  

`python3 -m venv myenv`    and activate:  

**For macOS and Linux:** `source myenv/bin/activate`  

**For Windows:** `.\myenv\Scripts\activate`  

2. Install the necessary packages listed in requirements.txt:     `pip install -r requirements.txt`  

3. Run the script:    `python3 1_main.py`  

4. Deactivate Virtual Environment when done:   `deactivate`



-------------------------------------------------------------------------------------
# Contributors
Viktoriia Tantsiura
Mercédesz Lehoczky
