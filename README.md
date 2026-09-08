# Playwright Python Automation framework (Page object model)

This framework is designed to be used as a boilerplate template to start automation testing quickly for any web application. The page object model is used to structure the test.

## Built With

- [Playwright Python](https://playwright.dev/python/)
- [PyTest](https://docs.pytest.org/en/latest/)
- [Docker](https://www.docker.com/)

## Installation

Prerequisites:
Python 3.10+

- Clone the repo.
- Navigate to the folder and install dependencies using:
```bash
pip install -r others/requirements.txt
```

- Install Playwright browsers
```bash
playwright install --with-deps
```

## Usage

- Run all the tests present in the "tests/web" directory:
```bash
pytest tests/web
```

## Docker 
- Directly use docker compose file:
```bash
docker-compose -f others/docker-compose.yml up
```

## GitHub Actions

- The workflow file is in directory `.github/workflows` named `playwright.yml`
- Every push or pull request action will trigger the workflow
