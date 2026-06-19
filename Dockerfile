FROM python:3.10

WORKDIR /app

# system dependencies (safe for ML)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# expose port (Render uses 10000 usually)
EXPOSE 10000

# start app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
