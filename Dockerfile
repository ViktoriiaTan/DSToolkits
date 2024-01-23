# Use the official Python image as a base
FROM python:3.10

# Setting working directory inside the container
WORKDIR /app

# Install dependencies
COPY script/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Include the .git directory(in case it's not copied from previous command)
COPY .git .git

# Copy and set permissions for entry-point and git commit scripts
COPY docker_entrypoint.sh get_git_commit.sh /
RUN chmod +x /docker_entrypoint.sh /get_git_commit.sh

# Set the entrypoint script
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["python3", "/app/script/1_main.py"]

