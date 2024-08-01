FROM python:3.9-alpine3.13
LABEL maintainer="Nishant Jawla"

# Setting python unbuffered mode to avoid buffering issues in docker and print logs in real time
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
# Setting working directory to /app directory to avoid setting it in every RUN command, its the default directory where all the commands will be executed
WORKDIR /app
EXPOSE 8000

# We are using ARG to set the default value of the environment variable DEV to false, so that we can use this variable to install the requirements for development or production environment using the same Dockerfile
ARG DEV=false
# We can make them as multiple RUN commands but it will increase the size of the image as each RUN command will create a new layer in the image
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# We are creating a new user to run the application in the container, this is a best practice to avoid running the application as root user and avoid security issues in case the docker container is compromised
ENV PATH="/py/bin:$PATH"

# We are setting the path of the python binary to the path of the python binary in the virtual environment, so that the python binary in the virtual environment is used to run the application

# We are running the application as a non-root user
USER django-user