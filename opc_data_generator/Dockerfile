FROM python:3.11-slim

WORKDIR /opt/opc_mockup/datagenerator

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./opc_data_generator.py"]