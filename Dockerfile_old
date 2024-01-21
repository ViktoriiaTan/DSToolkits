# Official Python image as a base
FROM python:3.10

# Setting working directory inside the container
WORKDIR /app

# Install netcat (nc)
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy and install requirements
COPY script/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application scripts
COPY . .

# Copy wait-for-it.sh into the image
COPY wait-for-it.sh app/wait-for-it.sh
RUN chmod +x app/wait-for-it.sh

CMD ["/app/wait-for-it.sh", "postgres:5432", "python3", "/app/script/1_main.py"]



