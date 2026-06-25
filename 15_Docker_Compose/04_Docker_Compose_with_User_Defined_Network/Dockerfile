FROM python

WORKDIR /app

COPY connect_database.py .

# Install required Python packages
RUN pip install mysql-connector-python

CMD ["python", "connect_database.py"]