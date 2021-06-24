# https://jonathanmh.com/deploying-a-nuxt-js-app-with-docker/

FROM node:latest as build
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN yarn
RUN yarn generate

FROM nginx:stable-alpine
COPY --from=build /usr/src/app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# FROM node:14.15.3-buster

# # create destination directory
# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

# # ENV PATH /usr/src/app/node_modules/.bin:$PATH
# # COPY package.json /usr/src/app/package.json
# # RUN yarn install --silent
# COPY . /usr/src/app
# RUN yarn generate

# # copy the app, note .dockerignore
# COPY . /usr/src/nuxt-app/

# # build necessary, even if no static files are needed,
# # since it builds the server as well
# RUN yarn

# # build the production nuxt app
# RUN yarn generate

# # expose 5000 on container
# EXPOSE 5000

# # set the browser base URL
# ARG BROWSER_BASE_URL
# ENV BROWSER_BASE_URL=$BROWSER_BASE_URL

# # set app serving to permissive / assigned
# ENV NUXT_HOST=0.0.0.0
# # set app port
# ENV NUXT_PORT=5000

# # start the app
# CMD [ "yarn", "start" ]