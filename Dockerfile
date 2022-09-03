FROM ubuntu:latest 

ADD app.py /
WORKDIR /

RUN apt-get update 
RUN apt-get install -y python3-pip

COPY . .
RUN pip install -r requirements.txt 

RUN cd app

EXPOSE 5000

CMD ["flask", "--app", "app", "run"]