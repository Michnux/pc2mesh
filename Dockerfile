FROM ubuntu:20.04

RUN apt update
#RUN apt -y install python3.8
RUN apt -y install python3-pip
RUN apt -y install xvfb

RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install cloudcompare --fix-missing

RUN pip3 install alteia
RUN pip3 install pymeshlab


COPY script_dir /home/script_dir/

#CMD ["sleep", "1d"]
CMD ["python3", "/home/script_dir/main.py"]