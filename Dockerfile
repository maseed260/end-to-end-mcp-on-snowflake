# Use official slim Python 3.12 image for smaller footprint and security
FROM python:3.12-slim-bookworm

# Prevent Python from writing .pyc and enable stdout buffer flushing
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install basic system dependencies required by many data/science libraries
WORKDIR /app
COPY cortex_agents.py .
COPY cortex_agents_client.py .
COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your code into the container
COPY cortex_agents.py .
COPY cortex_agents_client.py .
COPY .env .

EXPOSE 8501
CMD ["streamlit", "run", "cortex_agents_client.py", "--server.port=8501", "--server.address=0.0.0.0"]

