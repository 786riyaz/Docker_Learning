FROM python

WORKDIR /app

COPY API_Calling.py .

# Install required Python packages
RUN pip install requests

CMD ["python", "API_Calling.py"]