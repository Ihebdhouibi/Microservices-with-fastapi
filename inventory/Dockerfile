FROM tiangolo/uvicorn-gunicorn:python3.9

LABEL author="Iheb dhouibi"

WORKDIR /Microservices-App/inventory

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

CMD ["python", "main.py"]



