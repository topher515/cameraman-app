FROM node:4.1.1-wheezy

MAINTAINER Chris Wilcox <ckwilcox@gmail.com>

WORKDIR /asset-pipeline/

# We install these individually (instead of via package.json) so we get benefit of docker cache on re-build

RUN npm install del@2.0.2
RUN npm install browserify@11.2.0
RUN npm install event-stream@3.3.1
RUN npm install gulp@3.9.0
RUN npm install gulp-less@3.0.3
RUN npm install gulp-concat@2.6.0
RUN npm install gulp-watch@4.3.5
RUN npm install vinyl-transform@1.0.0
RUN npm install watchify@3.4.0

ADD gulpfile.js gulpfile.js
ADD package.json package.json