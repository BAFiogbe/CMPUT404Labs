import requests

# VERSION OF REQUEST PACKAGE
print(requests.__version__)

# GOOGLE MAIN PAGE
response = requests.get('http://www.google.com')
print(response.text)

# PRINT SOURCE CODE
response = requests.get('https://raw.githubusercontent.com/BAFiogbe/CMPUT404Labs/main/lab_1.py')
print(response.text)
