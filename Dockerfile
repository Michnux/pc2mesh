FROM ubuntu:20.04

RUN apt update
#RUN apt -y install python3.8
RUN apt -y install python3-pip
RUN apt -y install xvfb

RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install cloudcompare --fix-missing

#RUN apt-get update && apt-get install -y software-properties-common gcc && \
#RUN add-apt-repository -y ppa:deadsnakes/ppa
#RUN apt-get update && apt-get install -y python3.8 python3-distutils python3-pip python3-apt


RUN pip3 install alteia
RUN pip3 install pymeshlab


COPY script_dir /home/script_dir/

#CMD ["sleep", "1d"]
CMD ["python3", "/home/script_dir/main.py"]