FROM python:3.9

LABEL author="Iheb dhouibi"

WORKDIR /Microservices-App/payment

COPY ../requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

RUN python ./consumer.py

CMD ["uvicorn", "main:app", "--port", "8001"]