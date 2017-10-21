FROM python:3.6.1

# working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

ENV APP_SETTINGS=project.config.DevelopmentConfig
ENV DATABASE_URL=postgres://postgres:postgres@uaa-db:5432/uaa_dev
ENV DATABASE_TEST_URL=postgres://postgres:postgres@uaa-db:5432/uaa_test

# add app
ADD . /usr/src/app

# run server
CMD python manage.py runserver -h 0.0.0.0