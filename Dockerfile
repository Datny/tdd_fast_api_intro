FROM python:3.9.6-slim-buster

#set working directory
WORKDIR /usr/src/app

#set environment variables
    # Prevents python from writing pyc files to disc, same as python -B
ENV PYTHONDONTWRITEBYTECODE 1
    # Prevents python from buffering stdout amnd stderr, same as python -u
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get -y install netcat gcc && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# add entry point
COPY entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entry point
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
