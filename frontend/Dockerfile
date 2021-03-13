FROM node:lts-alpine

WORKDIR /usr/app

COPY package*.json ./

RUN npm install
RUN npm install -g @vue/cli

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]