# start by pulling the python image
FROM python:latest

WORKDIR /app
# copy the requirements file into the image
COPY ./requirements.txt /app
COPY ./app/* /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# copy every content from the local file to the image


# configure the container to run in an executed manner
ENTRYPOINT [ "python3", "-m" ]

CMD [ "flask","--app", "app", "run", "--host=0.0.0.0"]