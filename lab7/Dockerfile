FROM python:3.9

WORKDIR /code

# RUN apt update
# RUN apt install -y wget

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt


COPY ./source /code/app
EXPOSE 4080

CMD [ "/bin/bash", "/code/app/start.sh" ]
