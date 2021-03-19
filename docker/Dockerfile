# image
FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
ARG DEBIAN_FRONTEND=noninteractive


# apt-get
RUN apt-get update -qq && \
		apt-get install -y \
			curl git sudo tree vim wget build-essential software-properties-common unzip && \
		apt-get install -y \
			python3 python3-pip libopencv-dev libsm6 libxext6 libxrender-dev && \
        apt-add-repository ppa:fish-shell/release-3 && \
        apt-get update && \
        apt-get install -y fish fonts-powerline && \
        apt-get clean && \
		rm -rf /var/lib/apt/lists/* && \
		rm -rf /var/cache/apk/

# For jp_JP.UTF-8 and JST(Asia/Tokyo)
ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:en
ENV LC_ALL ja_JP.UTF-8
RUN apt-get update \
  && apt-get install -y language-pack-ja tzdata \
  && rm -rf /var/lib/apt/lists/* \
  && update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja" \
  && echo "${TZ}" > /etc/timezone \
  && rm /etc/localtime \
  && ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && dpkg-reconfigure -f noninteractive tzdata


# pip install
ENV WORK_PATH /workspace
COPY requirements.txt $WORK_PATH/docker/
ENV PIP_OPTIONS "--no-cache-dir --progress-bar off"
RUN pip3 install -U pip
RUN pip3 install ${PIP_OPTIONS} -r $WORK_PATH/docker/requirements.txt && \
		pip3 install ${PIP_OPTIONS} -U setuptools

# streamlit
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'
EXPOSE 8501

# duser setting
ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID $USERNAME && \
    adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USERNAME && \
    adduser $USERNAME sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $USERNAME

# set current dir
WORKDIR /workspace