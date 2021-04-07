from python:3.8-buster
RUN adduser --quiet --disabled-password --shell /bin/sh api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir -p /home/api/
COPY ./app /home/api/app
COPY manage.py requirements.txt run.sh /home/api/
RUN chown -R api:api /home/api
WORKDIR /home/api/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ./requirements.txt
WORKDIR /home/api/
USER api
RUN chmod 750 ./run.sh
ENTRYPOINT ./run.sh
