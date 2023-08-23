# pull official base image
FROM python:3.10.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

## create directory for the app user
 #RUN mkdir -p /home/app
 #
 ## create the app user
 #RUN addgroup --system app && adduser --system --group app
 #
 ## create the appropriate directories
 #ENV HOME=/home/app
 #ENV APP_HOME=/home/app/web
 #RUN mkdir $APP_HOME
 #WORKDIR $APP_HOME
 #
 ## install dependencies
 #RUN apt-get update && apt-get install -y --no-install-recommends netcat
 #COPY --from=builder /usr/src/app/wheels /wheels
 #COPY --from=builder /usr/src/app/requirements.txt .
 #RUN pip install --upgrade pip
 #RUN pip install --no-cache /wheels/*
 #
 ## copy entrypoint.prod.sh
 #COPY ./entrypoint.prod.sh .
 #RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
 #RUN chmod +x  $APP_HOME/entrypoint.prod.sh
 #
 ## copy project
 #COPY . $APP_HOME
 #
 ## chown all the files to the app user
 #RUN chown -R app:app $APP_HOME
 #
 ## change to the app user
 #USER app
 #
 ## run entrypoint.prod.sh
 #ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]