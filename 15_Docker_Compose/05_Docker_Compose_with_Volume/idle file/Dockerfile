FROM python:3.11-slim

WORKDIR /app

# Copy application file(s)
COPY connect_database.py .

# Install required Python package(s)
RUN pip install --no-cache-dir mysql-connector-python

# Create a newProducts.txt if it doesn't exist (so volume mapping works smoothly)
RUN touch /app/newProducts.txt

CMD ["python", "connect_database.py"]
