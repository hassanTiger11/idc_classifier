::
:: Enter your credentials here:
::

::
:: Enter the location of the folder containing your files here:
::

::
:: Nothing below this line should need to be changed
::

::
:: Upload the funding curve data
::
curl --request POST --url http://127.0.0.1:5000/upload_pic -F file=@".\pic.jpg"