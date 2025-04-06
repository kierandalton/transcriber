FROM python:3.9-slim

# Install system dependencies, including ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Create and activate a virtual environment
RUN uv venv

# Set execute permissions on activate script
RUN chmod +x /app/.venv/bin/activate

# Install dependencies into the virtual environment
RUN /app/.venv/bin/activate && uv pip install -r requirements.txt

# Copy your application code
COPY transcribe.py .

# Command to run your application
CMD ["/app/.venv/bin/python", "transcribe.py", "/audio/test_audio.m4a"]