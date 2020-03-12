# arxiv/docs
#
# This image serves up the arXiv docs sites, including Help, About, Labs,
# CoRR, and HyperTeX Help.
FROM arxiv/base-with-git:0.14.3

WORKDIR /opt/arxiv/

RUN pip install -U pip pipenv && \
    pipenv install uwsgi arxiv-marxdown==0.2.4rc3  && \
    rm -rf ~/.cache/pip

EXPOSE 8000

ARG NOCACHE=1
ARG VERSION
ARG BUILD_TIME

ENV VERSION=$VERSION \
    BUILD_TIME=$BUILD_TIME \
    LOGLEVEL=40 \
    PATH="/opt/arxiv:${PATH}" \
    LC_ALL=en_US.utf-8 \
    LANG=en_US.utf-8 \
    UWSGI_PROCESSES=4

# Add the /about site.
ADD ./deploy/about /opt/arxiv/about/
COPY ./about /opt/arxiv/about/source/
COPY ./.git /opt/arxiv/about/source/.git/

# Add the /corr site.
ADD ./deploy/corr /opt/arxiv/corr/
COPY ./corr /opt/arxiv/corr/source/
COPY ./.git /opt/arxiv/corr/source/.git/

# Add the /help site.
ADD ./deploy/help /opt/arxiv/help/
COPY ./help /opt/arxiv/help/source/
COPY ./.git /opt/arxiv/help/source/.git/

# Add the /hypertex site.
ADD ./deploy/hypertex /opt/arxiv/hypertex/
COPY ./hypertex /opt/arxiv/hypertex/source/
COPY ./.git /opt/arxiv/hypertex/source/.git/

# Add the /labs site.
ADD ./deploy/labs /opt/arxiv/labs/
COPY ./labs /opt/arxiv/labs/source/
COPY ./.git /opt/arxiv/labs/source/.git/

# Add the uwsgi config, which mounts each of the sites above.
COPY ./deploy/uwsgi.ini /opt/arxiv/uwsgi.ini

# Build all sites.
#
# These are grouped together in a single RUN to cut down on layers.
RUN ls -la /opt/arxiv/about/source && \
    pipenv run python -m arxiv.marxdown.build \
     --build-path=/opt/arxiv/about/build \
     --instance-path=/opt/arxiv/about/instance && \
    pipenv run python -m arxiv.marxdown.build \
     --build-path=/opt/arxiv/corr/build \
     --instance-path=/opt/arxiv/corr/instance && \
    pipenv run python -m arxiv.marxdown.build \
     --build-path=/opt/arxiv/help/build \
     --instance-path=/opt/arxiv/help/instance && \
    pipenv run python -m arxiv.marxdown.build \
     --build-path=/opt/arxiv/hypertex/build \
     --instance-path=/opt/arxiv/hypertex/instance && \
    pipenv run python -m arxiv.marxdown.build \
     --build-path=/opt/arxiv/labs/build \
     --instance-path=/opt/arxiv/labs/instance

ENTRYPOINT ["pipenv", "run"]
CMD ["uwsgi", "--ini", "/opt/arxiv/uwsgi.ini"]
