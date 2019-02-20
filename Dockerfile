FROM arxiv/base-with-git:0.14.3

WORKDIR /opt/arxiv/

RUN pip install -U pip pipenv
RUN pipenv install uwsgi arxiv-marxdown
ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8

ARG NOCACHE=1

ENV PATH "/opt/arxiv:${PATH}"

EXPOSE 8000
ENV LOGLEVEL 40

ARG SITE_NAME
ARG SITE_HUMAN_NAME
ARG SITE_HUMAN_SHORT_NAME
ARG SITE_SEARCH_ENABLED
ARG VERSION
ARG SOURCE
ARG SOURCE_DIR
ARG BUILD_TIME

ENV SITE_NAME=$SITE_NAME
ENV SITE_HUMAN_NAME=$SITE_HUMAN_NAME
ENV SITE_HUMAN_SHORT_NAME=$SITE_HUMAN_SHORT_NAME
ENV SITE_SEARCH_ENABLED=$SITE_SEARCH_ENABLED
ENV VERSION=$VERSION
ENV SOURCE=$SOURCE
ENV SOURCE_DIR=$SOURCE_DIR
ENV SOURCE_PATH=/opt/arxiv/source/$SOURCE_DIR
ENV BUILD_TIME=$BUILD_TIME

ADD ./build /opt/arxiv/source/
ADD ./build/.git /opt/arxiv/source/.git/

ENV BUILD_PATH /opt/arxiv/build
RUN ls -la /opt/arxiv/source
RUN pipenv run python -m arxiv.marxdown.build

ENTRYPOINT ["pipenv", "run", "uwsgi"]
CMD ["--http-socket", ":8000", \
     "-M", \
     "-T", \
     "-t 3000", \
     "--manage-script-name", \
     "--processes", "8", \
     "--threads", "4", \
     "--mount", "/=arxiv.marxdown.wsgi:application", \
     "--static-map", "/static=${BUILD_PATH}/static", \
     "--static-map", "/_docs/static=/opt/arxiv/docs/static", \
     "--logformat", "%(addr) %(addr) - %(user_id)|%(session_id) [%(rtime)] [%(uagent)] \"%(method) %(uri) %(proto)\" %(status) %(size) %(micros) %(ttfb)"]
