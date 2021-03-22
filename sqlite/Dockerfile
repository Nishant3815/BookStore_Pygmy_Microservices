FROM alpine:3.10
RUN apk add --update sqlite

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN mkdir /db
WORKDIR /db

ENTRYPOINT ["/docker-entrypoint.sh"]
