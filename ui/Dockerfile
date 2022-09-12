FROM node:alpine
WORKDIR /ui
COPY ./* ./

EXPOSE 3000
RUN npm i
CMD ["npm", "run", "start", "--port", "3000"]