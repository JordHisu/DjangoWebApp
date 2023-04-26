# syntax=docker/dockerfile:1

FROM python:3.10
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY ./nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /app
RUN mkdir -p /app/pip_cache
RUN mkdir -p /app/app
COPY start-server.sh /app
COPY requirements.txt /app
WORKDIR /
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt --cache-dir /app/pip_cache
RUN chown -R www-data:www-data /app
COPY . /app
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/app/start-server.sh"]
#ENTRYPOINT ["python3"]

#CMD ["manage.py", "runserver", "0.0.0.0:8080"]

