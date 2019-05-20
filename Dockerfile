FROM ubuntu:latest
MAINTAINER Omar Ewedah "omar.ewedah@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libmysqlclient-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install flask-mysql
RUN pip install pymysql
RUN pip install flask-jsonpify
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]