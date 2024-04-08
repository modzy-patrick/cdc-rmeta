# build final container

FROM python:3.9.1-alpine3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r cdc-rmeta/src/requirements.txt

    
# CMD ["python"]