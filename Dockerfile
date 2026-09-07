FROM node:14-alpine
RUN apk add --no-cache curl
COPY package.json /app/
WORKDIR /app
RUN npm install
COPY . /app
EXPOSE 3000
CMD ["node", "server.js"]
