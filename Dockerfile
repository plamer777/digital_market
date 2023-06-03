FROM python:3.10-slim
WORKDIR /digital_market
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
CMD gunicorn -b 0.0.0.0:8000 digital_market.wsgi --workers=2 --threads=2