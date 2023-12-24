# Milestone 3 Report

## Task 1

**Which services are being used for the application (described in the link above)? How do they relate to the host names in terms of computer networks?**  

The web service uses an image built from the Dockerfile in the current directory. This service is configured to expose port 5000 of the container, mapping it to port 8000 of the host machine​​.
The redis service, on the other hand, uses a public Redis image from Docker Hub. It's a standalone service and does not expose any ports explicitly in this example.
Each container for a service joins the default network created by Docker Compose and is reachable and discoverable by other containers on that network at a hostname identical to the container name​.

**What ports are being used (within the application and in the docker-compose file)?**  

In the Docker Compose file  the Flask application is configured with:
Container port: Port 5000 is where Flask operates inside the Docker container. 
Host port: Port 8000 on the host machine (our laptop) is mapped to the container's port. 
The syntax for port mapping in Docker Compose follows the HOST_ PORT:CONTAINER_PORT format. In this scenario, the mapping is defined as 8000:5000. This configuration facilitates external access to the service running inside the container.
 

**How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine?**  

When localhost:8000 is accessed via a web browser, Docker's network infrastructure redirects this request to port 5000 of the container, where the Flask application resides. This mechanism enables communication between the host machine and the application within the Docker container. The port mapping is essential as it connects the isolated environment of the Docker container with the external environment of the host machine. Without this mapping, the containerized services would remain inaccessible from outside the Docker ecosystem.

**What is localhost, why is it useful in the domain of web applications?**

In computer networking, "localhost" is the term for the user's own computer, connecting through the loopback interface. The IP address range for localhost is 127.0.0.0 to 127.255.255.255, with 127.0.0.1 being the most commonly used. This ensures any connections to localhost are directed back to the same device.

Role in web development:
* Acts as a virtual server for running and testing server-side code on the developer's machine.
* Facilitates local development and testing without internet exposure.
* Loopback to the user's own web server allows for secure and private development.

## Task 2

**a) What is PostgreSQL? Is it SQL or no-SQL (why?)**  

PostgreSQL is an SQL database, using SQL for data management and organizing data in linked tables. This is unlike NoSQL databases, which are designed for less structured data without a fixed table format. However, PostgreSQL also includes NoSQL-like features. A prime example is the ability to process data in JSON format, which is typically associated with semi-structured data, adding flexibility to a traditionally structured SQL environment.

**b)**
To complete this task, we started by setting up a custom Docker network called "mynetwork." This was important for making sure the PostgreSQL database and PGAdmin containers could talk to each other easily.  
Next, we used Docker to pull down the PostgreSQL version 14.0 image. Once we had the image, we ran a PostgreSQL container on "mynetwork." During this setup, we created a user named "student" with a password for the database.  
We also needed Python to work with PostgreSQL, so we installed the psycopg2 package. This package is a bridge between Python and PostgreSQL, letting our Python scripts interact with the database server.  
Then, we wrote a Python script called jokes.py. The script's job was to connect to PostgreSQL, make a new database named ms3_jokes, add a table called jokes, put a joke in it, and then get the joke back out to show it.  
For the database management part, we set up PGAdmin in another Docker container on the same network. This made managing the database easier.  
Finally, in PGAdmin, we did the following:  
Access: opened PGAdmin by going to http://localhost:5050 in our web browser.  
Login: logged in using the email  and password.  
Connection setup: In PGAdmin, we added a new server connection using the name mypostgres for the PostgreSQL container. We used the student user's credentials for this.  

**Challenges and solutions:**
We had  an issue connecting PGAdmin to PostgreSQL database. As we understood at the end this was because we were running both of them in separate Docker containers.  
The solution came from understanding Docker's networking capabilities. We placed both the PostgreSQL and PGAdmin containers on the same custom Docker network (mynetwork). This allowed PGAdmin to communicate with the PostgreSQL container using the container name (mypostgres) as the hostname. 

**c) If you stopped and deleted the Docker container running the database and restarted it. Would your joke still be in the database? Why or why not?**  

If we stop and delete our PostgreSQL container as it's currently set up, we'll lose all the data, including the joke. This is because we didn't use a Docker volume, and data stored inside a container is temporary and disappears with the container.  
However, if we use a Docker volume for our database, the situation changes. With a volume, our data remains safe even if we stop and delete the container. So, if we restart the container and connect it back to the same volume, our joke and all other data in the database will still be there.

## Task 3

**How do you need to represent/transform image data to save it to a relational database?**  

## Task 4

#### Additional: What is an SQL Injection Attack and how can you protect yourself?

### References:

1. https://www.postgresql.org/about/
2. https://www.freecodecamp.org/news/what-is-localhost/
3. https://www.postgresqltutorial.com/postgresql-python/connect/
4. https://www.postgresql.org/docs/12/datatype-binary.html#id-1.5.7.12.9
