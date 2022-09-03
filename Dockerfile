FROM ubuntu:latest 


WORKDIR /

RUN apt-get update 
RUN apt-get install -y python3-pip

COPY . .
RUN pip install -r requirements.txt 



EXPOSE 5000

CMD ["cd", "app", "&&", "flask", "--app", "app", "run"]