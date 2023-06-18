FROM python:3.10-alpine

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.5.0

RUN python -m pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
RUN apk add --no-cache python3-dev gcc cargo musl-dev linux-headers g++
RUN apk add --no-cache libpq-dev
WORKDIR /app
COPY . .
RUN poetry install
RUN apk del python3-dev gcc cargo musl-dev linux-headers g++
RUN apk add --no-cache firefox
RUN echo "Success builded!"
CMD poetry shell
CMD poetry run tickers_extract
CMD poetry run tickers_load
