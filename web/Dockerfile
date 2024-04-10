FROM python:3.9
WORKDIR /usr/src
COPY ./src/ ./
COPY ./app/ ./app/
COPY ./templates/ ./templates/
COPY ./test/ ./test/
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD [ "python", "./server.py" ]