# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .



# Expose port 8000
EXPOSE 8000

# Run Django app with gunicorn
CMD sh -c "python manage.py migrate --noinput && \
          python manage.py collectstatic --noinput && \
          echo 'from django.contrib.auth import get_user_model; User = get_user_model(); \
          User.objects.filter(username=\"admin\").exists() or \
          User.objects.create_superuser(\"admin\", \"admin@example.com\", \"adminpass\")' | python manage.py shell && \
          gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000"



