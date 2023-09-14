FROM python:3-slim

# Set the initial working directory to /app
WORKDIR /app

# Copy all files to /app
COPY . ./

# Install dependencies
RUN pip3 install -r requirements.txt

# Change the working directory to /app/src
WORKDIR /app/src

# Expose port 8080
EXPOSE 8080

# Set the entry point for the container
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0" ]