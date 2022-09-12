# start by pulling the python image
FROM python:latest

WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# copy the requirements file into the image
COPY ./requirements.txt requirements.txt
COPY ./* .


#make your container https ready
#RUN apt-get install openssl -y
#RUN openssl req -x509 --newkey rsa:4096 --out cert.pem --keyout key.pem --days 365

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy every content from the local file to the image


# configure the container to run in an executed manner
#ENTRYPOINT [ "python3", "-m" ]
EXPOSE 8000
CMD ["gunicorn", "--certfile", "cert.pem", "--keyfile", "key.pem", "-b", "0.0.0.0:8000", "app:app"]