FROM node:14-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
ENV REACT_APP_API_URL http://127.0.0.1:8000/scrape/devops
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
