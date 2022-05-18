FROM node:14-alpine

LABEL author="iheb dhouibi"

ENV PORT=3000

WORKDIR /Microservices-App/inventory-frontend

COPY    package.json .

RUN npm install

COPY . .

EXPOSE $PORT

CMD ["npm", "start"]