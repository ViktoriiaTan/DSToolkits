# Official Python image as a base
FROM python:3.10

# Setting working directory inside the container
WORKDIR /DSToolkits/script

# Copy requirements.txt 
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r  requirements.txt

# Copy the rest of the application
COPY . . 

# Run the application
CMD ["python", "./main.py"]
