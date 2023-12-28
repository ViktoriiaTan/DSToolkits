# Official Python image as a base
FROM python:3.10

# Setting working directory inside the container
WORKDIR /app

# Copy wait-for-it.sh
COPY wait-for-it.sh /app/

# Copy requirements.txt 
COPY script/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r  requirements.txt

# Copy the rest of the application
COPY script/ .

# Run the application
CMD ./wait-for-it.sh postgres:5432 -- python 1_main.py

