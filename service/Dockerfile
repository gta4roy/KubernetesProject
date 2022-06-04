#start by pulling the python image 
FROM python:3.8-alpine

#for Rasberry PI
#FROM arm32v7/python

#switch working directory 
WORKDIR /app

COPY .  /app

EXPOSE 7474

ENV HOSTNAME 0.0.0.0
ENV PORT 7474
ENV REDIS_PORT 6379
ENV REDIS_HOST 192.168.0.110
ENV REDIS_PASSWORD secret_password

RUN pip install flask 
RUN pip install redis 

ENTRYPOINT [ "python" ]

CMD [ "apiserver.py" ]


