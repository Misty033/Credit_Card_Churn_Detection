# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y libgomp1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose ports for FastAPI and Streamlit
EXPOSE 8000 8501

# Default command overridden in docker-compose
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Note: The CMD command can be overridden in the docker-compose file
# to run Streamlit or FastAPI as needed.    