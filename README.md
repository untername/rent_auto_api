# API for the car rental platform

# A task - write an api in which you can:
1) Add users.
2) Add auto.
3) Change user and car data.
4) Get a list of all users.

Access to information was to be carried out by token. In all other cases - an error.

# Upload:
1) git clone https://github.com/django/django.git@45dfb3641aa4d9828a7c5448d11aa67c7cbd7966.
2) pip install -r requirements.txt.
3) pip install HTTPPie (Optional).

# Examples.
1) http http://127.0.0.1:8000/api-token-auth/cars/
![Output](https://postimg.cc/N5Gm8QS5) 

2) http post http://127.0.0.1:8000/api-token-auth/ username=kalabala971@gmail.com password=x
![Output](https://postimg.cc/6TfCG8Hk)

3) http http://127.0.0.1:8000/api-token-auth/cars/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04"
![Output](https://postimg.cc/GHMYqZnz)

4) http://127.0.0.1:8000/api-token-auth/renters/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04" email="ax@pox.com" language="en" name="Mark"
![Output](https://postimg.cc/pyHDTfBQ)

5) http http://127.0.0.1:8000/api-token-auth/renters/1/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04"
![Output](https://postimg.cc/TKpbSCRx)
