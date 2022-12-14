# start by pulling the python image
FROM python:latest

WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# copy the requirements file into the image
COPY ./requirements.txt requirements.txt
COPY ./api/* .



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy every content from the local file to the image


# configure the container to run in an executed manner
#ENTRYPOINT [ "python3", "-m" ]

CMD [ "flask", "run"]