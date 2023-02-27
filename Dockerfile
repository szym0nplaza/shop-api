FROM python:3.11
WORKDIR /src
COPY ./requirements/ ./
RUN pip install -r base.txt
COPY . .
CMD [ "python", "src/main.py" ]