FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

RUN mkdir /tests
COPY . /tests
WORKDIR /tests

RUN pip install -r others/requirements.txt && \
    playwright install --with-deps

CMD ["pytest", "tests/web"]
