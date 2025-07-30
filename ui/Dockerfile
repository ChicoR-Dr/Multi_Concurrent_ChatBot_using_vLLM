# Use an official Python runtime as a parent image
FROM python:3.12.7

# This is fine — WORKDIR /app creates /app inside container
WORKDIR /app

# Since the build context is ./ui, this copies the contents of the `ui` folder into /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

# Run uvicorn app from inside /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]

