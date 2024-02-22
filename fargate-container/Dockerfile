# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install poppler-utils -y

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U "unstructured[pdf]" "unstructured-inference"
RUN python3 -m nltk.downloader punkt && \
    python3 -m nltk.downloader stopwords && \
    python3 -m nltk.downloader averaged_perceptron_tagger

# Additional libs needed for unstructured
RUN apt-get install ffmpeg libsm6 libxext6 -y

# With bigger model (onnx - default)
RUN python3 -c "from unstructured.partition.model_init import initialize; initialize()"

# # With lighter model (detectron2_onnx)
# RUN python3 -c "from unstructured.partition.model_init import initialize; import os; os.environ['UNSTRUCTURED_HI_RES_MODEL_NAME'] = 'detectron2_onnx'; initialize()"

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "preprocessing.py"]