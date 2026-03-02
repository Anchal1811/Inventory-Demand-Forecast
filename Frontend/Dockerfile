# Use a lightweight Python image
FROM python:3.10-slim


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory

WORKDIR /app

# This copies the project file and any lock file that exists without crashing
COPY pyproject.toml uv.lock* ./

RUN uv sync


COPY . .

# Open the port for Streamlit
EXPOSE 8501

# Use 'uv run' to automatically enter the virtual environment created by 'uv sync'
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]