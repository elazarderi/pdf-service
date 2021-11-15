FROM amazonlinux:latest
RUN yum -y install python3-pip && yum clean all
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN yum -y --nogpgcheck localinstall /usr/src/app/wkhtmltox-0.12.6.rpm

RUN pip3 install -r requirements.txt
EXPOSE 3001
ENTRYPOINT ["python3","./index.py"]