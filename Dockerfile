# Use an official Python runtime as a parent image
FROM python:3.12

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl

# Install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install npm dependencies and run build
# RUN npm install && npm run build

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=myblog.settings

# Run migrations and the Django development server
CMD ["sh", "-c", "- python manage.py migrate &&  python manage.py runserver 0.0.0.0:8000"]