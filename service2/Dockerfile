FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask SQLAlchemy
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]
