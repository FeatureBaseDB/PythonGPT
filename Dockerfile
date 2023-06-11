# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python 3.10.x and pip
RUN apt-get update && apt-get install -y python3.10 python3-pip

# Set the working directory inside the container
WORKDIR /PythonGPT

# Copy all files and directories from the current directory to the working directory inside the container
COPY . .

# Install dependencies from requirements.txt using pip
RUN pip3 install -r requirements.txt

# Set the entry point for the container
CMD [ "python3", "doc_code.py" ]
