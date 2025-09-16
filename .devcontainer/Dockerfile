FROM tensorflow/tensorflow:latest-gpu-jupyter

ARG MY-RPOJECT-NAME
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
ADD ./requirements.txt .
RUN apt-get update && apt-get install -y git
RUN apt-get install -y openssh-client
RUN apt-get install sudo
RUN apt-get install wget
RUN apt-get install pciutils
RUN apt-get install curl
RUN pip3 -q install pip --upgrade
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh
## Matching the cuda version for this container and T5 server Feb 2023
#RUN pip install --upgrade torch==1.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
#RUN pip install --upgrade torch==1.13.1 --extra-index-url https://download.pytorch.org/whl/cu113 


#TODO: How to change the project name dynamicaly
RUN git config --global --add safe.directory /workspaces/${MY-PROJECT-NAME}
EXPOSE 11434 8080