FROM python:3.9

RUN pip install pipenv
COPY Pipfile /
COPY Pipfile.lock /
RUN pipenv install --deploy
COPY app.py /

CMD [ "pipenv", "run", "python", "app.py" ]
