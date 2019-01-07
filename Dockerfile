FROM arxiv/base:0.12.1

WORKDIR /opt/arxiv/

# Install MySQL.
RUN yum install -y which mysql mysql-devel

ADD Pipfile Pipfile.lock /opt/arxiv/
RUN pip install -U pip pipenv uwsgi
ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8
RUN pipenv install

ARG NOCACHE=1

ADD docs/ /opt/arxiv/docs/
ADD bin/start.sh /opt/arxiv/

ENV PATH "/opt/arxiv:${PATH}"

ADD build.py /opt/arxiv/
ADD wsgi.py uwsgi.ini /opt/arxiv/

EXPOSE 8000
ENV LOGLEVEL 10

ARG SITE_NAME
ARG SITE_HUMAN_NAME
ARG VERSION
ARG SOURCE
ARG BUILD_TIME

ENV SITE_NAME=$SITE_NAME
ENV SITE_HUMAN_NAME=$SITE_HUMAN_NAME
ENV VERSION=$VERSION
ENV SOURCE=$SOURCE
ENV BUILD_TIME=$BUILD_TIME

ADD source/ /opt/arxiv/source/
ENV SOURCE_PATH /opt/arxiv/source
ENV BUILD_PATH /opt/arxiv/build
RUN pipenv run python build.py

ENTRYPOINT ["/opt/arxiv/start.sh"]
CMD ["--http-socket", ":8000", \
     "-M", \
     "-t 3000", \
     "--manage-script-name", \
     "--processes", "8", \
     "--threads", "1", \
     "--async", "100", \
     "--ugreen", \
     "--mount", "/=wsgi.py", \
     "--logformat", "%(addr) %(addr) - %(user_id)|%(session_id) [%(rtime)] [%(uagent)] \"%(method) %(uri) %(proto)\" %(status) %(size) %(micros) %(ttfb)"]
