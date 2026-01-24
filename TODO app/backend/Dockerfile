FROM node:20.19.6


WORKDIR /server

COPY src .

RUN ["npm", "i"]

EXPOSE 9000

ENTRYPOINT [ "node", "server.js" ]
