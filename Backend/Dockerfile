FROM python:3.10-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# This copies the project file and any lock file that exists without crashing
COPY pyproject.toml uv.lock* ./

# 2. Install dependencies during BUILD (this is the "heavy" part)
# --frozen ensures it matches your lockfile exactly
RUN uv sync

# 3. Copy the rest of your backend code
COPY . .

# 4. Use 'uv run' to start the app instantly
# Change 'main:app' if your entry file or FastAPI variable is named differently
# We tell uvicorn to look inside the 'api' folder for the 'main' file
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]