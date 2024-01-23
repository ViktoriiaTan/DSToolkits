# Use the official Python image as a base
FROM python:3.10

# Setting working directory inside the container
WORKDIR /app

# Install dependencies
COPY script/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Set the entrypoint script
COPY .git .git
COPY docker_entrypoint.sh get_git_commit.sh /
RUN chmod +x /docker_entrypoint.sh /get_git_commit.sh
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["python3", "/app/script/1_main.py"]

