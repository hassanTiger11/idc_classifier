::
:: build docker
::
docker build -t hassantiger11/idc_identifier .
::
:: push docker image
::
docker tag 05ff620868d1 hassantiger11/idc_identifier:latest
docker push hassantiger11/idc_classifier:latest

::
:: for aws port is 8080
::
