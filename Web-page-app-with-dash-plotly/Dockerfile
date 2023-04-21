FROM python:3.9.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /backend
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN apt-get update
# RUN apt-get install -y libpq-dev  # Not needed for psycopg2-binary
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org --no-cache-dir --timeout 1900 -r requirements.txt
RUN find /usr/local/ \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -delete

COPY . /app

EXPOSE 8050

CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]

