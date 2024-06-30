# Use an official Python runtime as a parent image
FROM python:alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary files into the container
COPY . .

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable (if needed)
# ENV NAME World

# Run main_score.py when the container launches
CMD ["python", "main_score.py"]
