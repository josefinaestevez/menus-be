# Set python version
ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

# Set environment variables to avoid .pyc and unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working dir
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "config.wsgi"]