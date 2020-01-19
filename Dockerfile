FROM python:3.8

COPY requirements.txt /home

RUN pip install -r /home/requirements.txt

WORKDIR /home

ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD ["python", "LostCitiesScore/manage.py", "runserver", "0.0.0.0:8000"]
