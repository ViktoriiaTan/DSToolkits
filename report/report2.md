# Milestone 2 Report

## Task 1

In the milestone1 we created a .gitignore file in the root directory. 
It is essential for excluding non-essential or sensitive files (like passwords, API keys) from the version control system, ensuring a clean and secure codebase.  
For milestone 2, we updated our .gitignore by including myenv, data, pycache and other folders.  
* The exclusion of "myenv" helps prevent the buildup of individual environment configurations and dependencies, ensuring a separate and tailored development setup for each developer.  
* Excluding the "data" folder via .gitignore helps keep it efficient by avoiding large files, sensitive information, and irrelevant data.  
* Ignoring "pycache" directories avoids versioning Python bytecode files, which are machine and interpreter-specific, thus reducing repository noise and potential merge conflicts.  

We managed our .gitignore file by creating a special branch called gitignore-updates specifically for changes to .gitignore. Everyone could update this branch as needed and then merge these updates into their own work branches. When these feature branches are ready to merge into the main branch, they already include the latest .gitignore updates.  
This approach keeps our main branch organized and ensures that everyone works with the most current .gitignore settings.

## Task 2

**What is a Hash function? What are some of the use cases?**

A hash function is a special type of function in computing for implementing security. It takes input (which can be anything from a string of text to a file) and converts it into a fixed-size string of characters. This output, typically a sequence of numbers and letters (hash value/ hash code).  
Hash function is widely used:  
- Cryptocurrency (to secure transactions)  
- Password verification for authentication (websites hash and store passwords. During login, they compare the hash of the entered password with the stored hash for security)  
- Data and file integrity check (check the integrity of data or files. Checking the hash of an uploaded file against its original ensures that it hasn’t been modified)  
- Digital signature (maintain the integrity of digital signatures. Data is hashed and encrypted for signing, and this process is reversed for verification)  

**What is a Python module, package and script? How do they differ from one another?**

* A module is a .py file containing Python code, including functions, classes, and variables. It is designed for reuse in other Python programs. Modules help in keeping the code structured and modular. They can be easily imported into other Python scripts. Python's community has a vast range of modules for various purposes, some being part of the standard library, while others can be installed via package managers like pip.  
* A package is a collection of related modules. It's essentially a directory structure with a special file __init__.py that allows Python to treat the directories as containing packages. This allows for logical organization of modules. For instance, the NumPy package includes modules for numerical operations, array handling, and mathematical functions, all designed to work together for numerical computing and data analysis.  
* A Python script is a file with executable Python code, typically saved with a .py extension. Scripts can be run directly by a Python interpreter and may include a mix of functions, classes, and standalone code. Scripts are often used for specific tasks or small programs and are the simplest form of Python code execution.  

**How would you explain a Docker container and volume to a child?**

A Docker container is like a set of Lego. 
Each Lego piece, a building block represents a piece of the program: code, tools,  all files needed for running. 
Just as the Lego pieces themselves, Docker containers are also modular: if you need to, you could build any shape you can come up with: you have all the building blocks needed. Compatibility is also not an issue, all pieces can be connected and disconnected, reused when needed. You may also change (update) a block (container) without the compatibility being affected. There may be multiple pieces of the same block available too.
The blocks, just as the containers exist whether or not they are a part of an application or structure. The pieces are also portable, you can assemble them wherever you need them. 
A specific set of Lego, for example one that can build a starship or a police station, will come in a separate box. All the necessary pieces are found in the box to build the structure on the picture on the box. We do our best to not to mix up these boxes, but the Docker container will never have a problem with that: always keeps the necessary pieces for the set contained.

Now imagine that you have a magic Lego box with a secret compartment that keeps track of important information, records or items, tools and rare pieces, mini figures that get safely stored away in the secret compartment. That is similar to the Docker volume. 

You can build whatever you like in this magic box, but you have to remember one thing: once you close the box, all your creations will disappear, except for the items in the secret compartment.

**What is your preference concerning the use of Python virtualenv and Docker? When would you use one or the other?**

Virtualenv generally is the better choice for more lightweight or local projects, where a simpler environment capable of running a Python application is sufficient to separately run the necessary dependencies. Similarly to Docker containers, these virtual environments are capable of running confined, separate dependencies, however, this structure is created for running Python applications and they are not as robust as Docker containers.

Docker is a more complex system, capable of handling applications outside of Python too. It is best to use for more robust projects, where the program would be rolled out on multiple systems. It can handle multiple dependencies, including system-level ones, as well as different steps of the procedure, completely isolated. It is best to use for more demanding (non-local) deployment. 

**What is the Docker build context?**

The Docker build context is a set of files and directories that are sent to the Docker daemon when building a Docker image. When running a build, Docker CLI sends the contents of the specified directory (or the current directory by default) to the Docker daemon as the context. It's important to keep the build context minimal to speed up the build process.

**How can you assess the quality of a python package on PyPI?**

We can assess the quality of a Python package on PyPI by first searching for and installing packages based on relevance, updates, and Python version compatibility; this is followed by reviewing the package's details on PyPI for legitimacy and project relevance. Additionally, we can explore the package's GitHub repository for community engagement indicators like stars, forks, and pull requests, and use Libraries.io for detailed statistics like dependencies, release history, and SourceRank score. And it's important to verify that the package's licence is suitable for our intended use, particularly for commercial or shared projects.  

## Task 3

The "mnist_ convnet" script incorporates essential elements for a basic machine learning workflow with Keras and TensorFlow.  
It loads the MNIST dataset using `keras.datasets.mnist.load_data()` and defines a Sequential model with convolutional and dense layers. The model is compiled with the Adam optimizer and categorical crossentropy loss function. Training is conducted using `model.fit()` with a specific batch size and number of epochs.  
In order  to save the trained model to a .h5 file, we added `model.save(model.h5)` after training the model (module_ io), to load a model from a .h5 file, we added keras.models.load_ model(model.h5) in module_io.  
Also this model can make predictions on new data. By applying the `model.predict(x_test)` method, it generates class probabilities for each of the ten digit classes. These probabilities indicate the likelihood of each test image belonging to a particular digit class.

## Task 4

We've restructured our code into separate modules like module_ io, data_ prepar, model_ architect, train, and eval_predict to organise the code logically. This makes our code easier to read, update, and reuse.  
Smaller, focused files are simpler to manage than one large script. Modules can be used again in different parts of the project. Smaller pieces of code are simpler to test and debug.  
For example, isolating the model_architect  allows for easy experimentation with different model configurations.  

Structure of the code:

Main script main.py runs the whole process: loads data, processes it, builds and trains the model, saves it and makes predictions.  

Modules:
* Data handling (module_io.py): loads the MNIST data and handles saving/loading models.  
* Data preprocessing (data_prepar.py): prepares the data for the model (like scaling images).  
* Model building (model_architect.py): contains the structure of the neural network.  
* Model training (train.py): code to train the model.  
* Evaluation and prediction (eval_predict.py): used for testing the model and making predictions.  


## Task 5

We created a requirements.txt file for our code during milestone1. We identified all the necessary packages our project relies on, including their specific versions there.  
There are SHA256 hash digests (from PyPI) for each of them:

|  Package  | Version |                         Hash                                          |
|:----------|:--------|:----------------------------------------------------------------------|
|pip        | 22.0.2  |sha256:27b4b70c34ec35f77947f777070d8331adbb1e444842e98e7150c288dc0caea4|
|numpy      | 1.23.5  |sha256:1b1766d6f397c18153d40015ddfc79ddb715cabadc04d2d228d4e5a8bc4ded1a|
|tensorflow | 2.14.0  |sha256:c3870063433aebbd1b8da65ed4dcb09495f9239397f8cb5a8822025b6bb65e04|

We set up a virtual environment named "myenv" in our project directory using Python's venv module for isolation. After activating this environment `source myenv/bin/activate`, we installed our dependencies with `pip install -r requirements.txt`. Once installation was complete, we deactivated the environment with the `deactivate` command.

## Task 6

Initially, we tried using the Tensorflow image from Docker Hub, but it was unable to handle the requirements file. 
Then we changed to the Python image. 
We chose the image that uses Python version 3.10, checked the requirements for compatibility and built the container.
We also added a Dockerignore file.

## References:

1. https://resources.infosecinstitute.com/topics/cryptography/introduction-to-hash-functions/
2. https://pypi.org/project/
3. https://realpython.com/run-python-scripts/
4. https://www.linkedin.com/pulse/quality-over-quantity-all-python-packages-created-jessica
5. https://peps.python.org/pep-0008/#variable-annotations
6. https://hub.docker.com/
