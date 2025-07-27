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

# FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

# WORKDIR /app

# COPY pyproject.toml /app/
# COPY README.md /app/
# COPY uv.lock /app/

# RUN --mount=type=cache,target=/root/.cache/uv \
#     --mount=type=bind,source=uv.lock,target=uv.lock \
#     --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#     --mount=type=bind,source=README.md,target=README.md \
#     uv sync --frozen --no-dev --no-editable

# COPY cortex_agents.py .
# COPY cortex_agents_client.py .
# COPY requirements.txt .
# COPY .env .

# FROM python:3.12-slim-bookworm

# RUN pip install --no-cache-dir -r requirements.txt

# WORKDIR /app

# COPY --from=uv /app/.venv /app/.venv
# COPY --from=uv /app /app

# ENV PATH="/app/.venv/bin:$PATH"
# ENV PYTHONPATH=/app

# EXPOSE 8501
# CMD ["streamlit", "run", "cortex_agents_client.py", "--server.port=8501", "--server.address=0.0.0.0"]

