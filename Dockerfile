FROM python:3.9-slim

# Set the working directory
WORKDIR /app
COPY model.pkl /app/model.pkl
COPY requirements.txt /app/requirements.txt
COPY ml_service.py /app/ml_service.py

# Install the dependencies
RUN pip install -r requirements.txt

# Command to run on container start
CMD [ "python", "ml_service.py" ]
