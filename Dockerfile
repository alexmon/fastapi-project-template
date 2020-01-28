FROM tiangolo/uvicorn-gunicorn:python3.7

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]