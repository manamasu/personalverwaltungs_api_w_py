# 1. build an image based on the Python official-image
FROM python:3.13-slim

# 2. Setup the working dir
WORKDIR /app

# 3. Installing System dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# # Copy our .env.docker and renaming it to .env
# COPY .env.docker .env

COPY . .

# 5. Expose the PORT which the app will run on
EXPOSE 8080

# 6. RUN APP
CMD [ "python", "./run.py"]