# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (important for Render)
EXPOSE 5000

# Run Flask app
CMD ["python", "app/main.py"]

