Tech Stack:
1)Backend:Python,Flask
2)Containerization:Docker

Structure
1)requirements.txt: list the necessary Python packages and the version required to run the Flask application
2)Dockerfile:defines the setup for a Docker container to host the Flask application

3)py_doc:
*sever.py: establishes a Flask server and defines routes to process recipts and retrieve points. It needs to import functions from validations.py and points.py to calculate points based on receipt.The file contains POST requests at /receipts/process to process new receipts. You can insert the input JSON files into Postman, the POST requests would generate the ID and points. The GET requests at /receipts/{id}/points would retrieve points associated with a given receipt ID.

*validations.py:contains functions to validate the receipt structure and its content. Make sure the data provided adheres to specified conditions.

*points.py:contains functions to calculate the points on different rules provided in a receipt.The function takes the dictionary as input and returns points based on the rules.

Setup and running instructions
1) Install Docker in your machine and Clone the project repository
   chose the file that store the document(example:interview)
   run the following command in the command Prompt
	pip freeze > requirements.txt
2) Build the Docker Image
   run the command to build the Docker image:
   	docker build -t interview-receipts-app .
3) Run Docker Container 
(Once the image is built, start the container) run the command:
4) Accessing the Application:
   run the command
   	docker run interview-receipts-app
   you can process receipts and retrieve points: http://localhost:8080/receipts/process
   and http://localhost:8080/receipts/{id}/points
5) Stop and Remove Docker Container (docker ps)
