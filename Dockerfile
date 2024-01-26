# Use a base image with Python and other dependencies
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY script/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Include the .git directory (in case it's not copied from the previous command)
COPY .git .git

# Copy and set permissions for the entry-point and git commit scripts
COPY docker_entrypoint.sh get_git_commit.sh /
RUN chmod +x /docker_entrypoint.sh /get_git_commit.sh

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the entrypoint script
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["python3", "/app/script/1_main.py"]
