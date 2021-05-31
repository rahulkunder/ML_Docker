FROM centos:latest

RUN yum install python3 -y  
RUN pip3 install pandas 
RUN pip3 install sklearn

COPY predic.py /
COPY SalaryData.csv /

ENTRYPOINT python3 predic.py


