# Build Docker Images
To build the Docker image for example for the the `booking-service`, you use the following commands:

### Step 1: Navigate to the service directory
```bash
cd backend/booking-service
```

### Step 2: Build the Docker image and tag it
```bash
docker build -t 44sven/sepro-group-7/booking-service:v1.0.0 .
```
Make sure to replace `booking-service` with the appropriate service name if you are building a different service. Replace `v1.0.0` with the desired version tag.

### Step 3: Log in to Docker Hub (interactive prompt)
```bash
docker login
```

### Step 4: Push the image to Docker Hub
```bash
docker push 44sven/sepro-group-7/booking-service:v1.0.0
```

Make sure to replace `booking-service` with the appropriate service name if you are building a different service. Replace `v1.0.0` with the version tag you used in Step 2.

# Run Docker Containers
To run the Docker container for the `booking-service`, you can use the following command:
```bash
docker run -p 8001:8000 --rm --name booking-service 44sven/sepro-group-7:booking-service
```
Or use the provided `docker-compose.yml` file in the root directory of the whole project to run all services together:
```bash
docker-compose up -d
```
To run a single service using Docker Compose, you can specify the service name:
```bash
docker-compose up -d booking-service
```
