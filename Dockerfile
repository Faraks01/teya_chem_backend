FROM python:3
RUN mkdir /teya_chem_backend
WORKDIR /teya_chem_backend
ADD requirements.txt /teya_chem_backend/
RUN pip install -r requirements.txt
ADD . /teya_chem_backend/
EXPOSE 8000
