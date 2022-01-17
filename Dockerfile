FROM python:3.9.9-alpine3.15

ADD ./requirements.txt /app/requirements.txt

RUN apk update
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev unixodbc mariadb-dev libstdc++6
RUN apk add bash icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib curl gnupg

#Download the desired package(s)
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.8.1.1-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.8.1.1-1_amd64.apk

#(Optional) Verify signature, if 'gpg' is missing install it using 'apk add gnupg':
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.8.1.1-1_amd64.sig
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.8.1.1-1_amd64.sig

RUN curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import -
RUN gpg --verify msodbcsql17_17.8.1.1-1_amd64.sig msodbcsql17_17.8.1.1-1_amd64.apk
RUN gpg --verify mssql-tools_17.8.1.1-1_amd64.sig mssql-tools_17.8.1.1-1_amd64.apk

#Install the package(s)
RUN apk add --allow-untrusted msodbcsql17_17.8.1.1-1_amd64.apk
RUN apk add --allow-untrusted mssql-tools_17.8.1.1-1_amd64.apk

RUN apk update
#RUN apt-get install python3-venv
#RUN apt-get install unixodbc-dev && apt-get update

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps


ADD ./ /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

#RUN isql -v -k "DRIVER={ODBC Driver 17 for SQL Server};SERVER=library-devops.database.windows.net;UID=adminbro;PWD=RedLightGreenLight123"
#RUN cat /etc/odbc.ini
#RUN python manage.py makemigrations \
#    && python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "library.wsgi"]