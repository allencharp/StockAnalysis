FROM ubuntu:14.04

RUN echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main" > /etc/apt/sources.list.d/deadsnakes.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DB82666C

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    vim \
    libpq-dev \
    make \
    mercurial \
    pkg-config \
    python3.4 \
    python3.4-dev \
    ssh \
    libxml2 \
    && apt-get autoremove \
    && apt-get clean

ADD https://raw.githubusercontent.com/pypa/pip/701a80f451a62aadf4eeb21f371b45424821582b/contrib/get-pip.py /root/get-pip.py
ADD . /stock
RUN python3.4 /root/get-pip.py
RUN pip3.4 install -U "setuptools==15.1"
RUN pip3.4 install -U "pip"
RUN pip3.4 install -U "virtualenv==12.1.1"
RUN pip3.4 install -U "gevent"
RUN pip3.4 install -U "lxml"
RUN pip3.4 install -U "pandas"
RUN pip3.4 install -U "requests"
RUN pip3.4 install -U "beautifulsoup4"
RUN pip3.4 install -U "flask"
RUN pip3.4 install -U "tushare"
RUN pip3.4 install -U "pymysql"


COPY /src/sina_analysis.py /src/sina_service.py /src/tushare_wrapper.py ./stock/

WORKDIR /stock

CMD ["python3", "/stock/sina_service.py"]

