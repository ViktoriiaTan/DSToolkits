# Milestone 5 Report

## Task 2,3

To accomplish the task at hand, we created three Docker containers, each responsible for a specific component of the system. Here is a description of how we configured the system:  

- **PostgreSQL database container:** This container was set up to persistently store images and predictions.  
- **Flask application container:** Within this container, we hosted a REST API responsible for various tasks, including image uploads, image processing through a pre-trained neural network for prediction, and displaying the results. The configuration included the following steps:  
1. Loading a pre-trained neural network model during initialization.  
2. Initializing the database to store data.  
3. Setting up a route (/) to display an HTML page for image uploads.
4. Handling POST requests with images at the /predict endpoint. This involved saving the uploaded image, processing it using the neural network model for prediction, and storing both the image and its prediction in the database.
5. Providing predictions in either JSON format or displaying them on an HTML page based on the client's request.
6. Running the application on port 5000 for network accessibility.

- **Test client container:** This container was specifically designed to send a sample MNIST image to the Flask app for prediction. It simulated real-world scenarios where clients don't have direct access to another system's database but need to prepare and test images automatically. The test client waited for the Flask app to become available and then sent a sample image to the prediction endpoint.
   
- **pgAdmin:** To check our PostgreSQL database and display the predictions from Flask web application on pgAdmin interface.

The requirement file was updated to include pillow, psycopg and flask packages with fixed versions.

|   Package  | Version |                             SHA256                             |
|------------|---------|----------------------------------------------------------------|
|Pillow      |0.1.0    |61f1a9d247317fa08a308daaa8ee7b3f760ab1809ca2da14ecc88ae4257d6172|
|psycopg     |2-2.9.9  |d1454bde93fb1e224166811694d600e746430c006fbb031ea06ecc2ea41bf156|
|Flask       |3.0.1    |55d03fea4c4e9fd0ad75dc2e7e2b6757b80c152c032ea1d1de487461d8140efc|

To facilitate smooth communication and orchestration among these containers, we updated the *docker-compose.yml* file with the necessary configurations, ensuring proper networking and dependency settings.

Additionally, we developed a frontend that included upload and *result.html* templates, allowing users to select files for prediction. Two HTML templates were created: *upload.html* for the file upload form and *result.html* for displaying predictions and uploaded images. These templates were placed in the templates directory.  

Flask app effectively managed file uploads through the */predict* route, saving uploaded files and processing them accordingly. After processing images and generating predictions, the script rendered the result.html template, displaying predictions alongside the uploaded images. This process worked seamlessly when tested with sample uploads from the MNIST dataset.  
However, an issue arosed when we attempted to upload new image to the Flask app from frontend upload page and these image was not recognized as part of the request. But unfortunately, we didn't have enough time to solve this problem. We are continuing to work towards resolving this issue.   

**Challenges and solutions:**  

**Problem 1:** The test client script in its Docker container initiated execution immediately upon container startup. However, at this stage, the Flask app was not fully operational, leading to failed attempts to send images for prediction.  
**Solution:** We introduced a retry mechanism within the test client script. This modification allowed the script to periodically attempt communication with the Flask app, waiting until the Flask service was available and ready to process requests effectively.

**Problem 2:** Initially, the test client failed to reach the Flask app's prediction API due to an incorrect URL (*localhost:5000/predict*) in the test client script.  
**Solution:** We corrected the URL in the test client script to *flask_app:5000/predict*, aligning it with the service name defined in *docker-compose.yml*. This adjustment ensured that the test client correctly addressed the Flask container within the Docker network environment.
