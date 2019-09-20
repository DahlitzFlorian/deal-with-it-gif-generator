FROM node:10.6.0-alpine as node

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install rxjs-compat --save
RUN npm install bootstrap --save
RUN npm install ng2-file-upload --save

COPY . .

RUN npm run build

FROM nginx:1.17.3-alpine

COPY --from=node /usr/src/app/dist/dwi-frontend /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
