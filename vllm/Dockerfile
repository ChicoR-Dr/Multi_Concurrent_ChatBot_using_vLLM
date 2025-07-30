# Use an official Python runtime as a parent image
FROM python:3.12.7

# 1. Create working directory inside container
WORKDIR /app

# 2. Copy everything from `vllm/` folder into container's `/app`
COPY . /app

# 3. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. Make the shell script executable
RUN chmod +x run_vllm.sh

# 5. Expose port (vLLM API runs on port 8000 by default)
EXPOSE 8000

# 6. Launch the server using the shell script
CMD ["./run_vllm.sh"]

