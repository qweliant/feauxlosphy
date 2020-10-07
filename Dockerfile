FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PORT 8080
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

# Install spacy requirments separately first so that Docker will 
# cache the (somewhat) expensive download of a spacy model
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app/app