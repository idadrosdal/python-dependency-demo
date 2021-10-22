FROM python:3.9

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

COPY app.py /
COPY pyproject.toml /
COPY poetry.lock /
RUN poetry install --no-dev

CMD [ "poetry", "run", "python", "app.py" ]
