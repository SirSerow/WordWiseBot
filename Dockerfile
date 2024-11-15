# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot.py file from /components/bot/bot.py to /app/
COPY ./components/bot/bot.py .

# Expose the port (if needed)
EXPOSE 8080

# Set runtime command
CMD ["python", "bot.py"]
