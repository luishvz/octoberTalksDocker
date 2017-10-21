FROM node:7.8.0

ENV NPM_CONFIG_LOGLEVEL warn

WORKDIR /usr/src/app

COPY package.json .
RUN npm install

COPY . /usr/src/app

RUN npm run build

EXPOSE 3000
CMD [ "npm", "run", "serve" ]
