FROM arxiv/base

WORKDIR /opt/arxiv/

ADD Pipfile Pipfile.lock /opt/arxiv/
RUN pip install -U pip pipenv
ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8
RUN pipenv install
ADD docs/ /opt/arxiv/docs/
ADD site/ /opt/arxiv/site/

ENV PATH "/opt/arxiv:${PATH}"

ADD build.py /opt/arxiv/
ADD wsgi.py uwsgi.ini /opt/arxiv/

EXPOSE 8000

RUN pipenv run python build.py

CMD pipenv run uwsgi --ini uwsgi.ini
