FROM python:3.8

COPY pyproject.toml .

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY mttools/ mttools/
COPY tests/ tests/

RUN poetry install
