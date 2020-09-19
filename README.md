# API for the car rental platform

# There was a task - write an api in which you can:
1) Add users.
2) Add auto.
3) Change user and car data.
4) Get a list of all users.

Access to information was to be carried out by token. In all other cases - an error.

# Required fields:
Auto: name, year, time of entry into the base.

Tenant: name, mail, language.

The rest of the fields are determined dynamically

# Examples.
1) Check: http http://127.0.0.1:8000/api-token-auth/cars/
[Output](https://postimg.cc/N5Gm8QS5) 

2) Get Token: http post http://127.0.0.1:8000/api-token-auth/ username=kalabala971@gmail.com password=x
[Output](https://postimg.cc/6TfCG8Hk)

3) Checking with a token: http http://127.0.0.1:8000/api-token-auth/cars/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04"
[Output](https://postimg.cc/GHMYqZnz)

4) Set new renter: http://127.0.0.1:8000/api-token-auth/renters/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04" email="ax@pox.com" language="en" name="Mark"
[Output](https://postimg.cc/pyHDTfBQ)

5) Check first renter: http http://127.0.0.1:8000/api-token-auth/renters/1/ "Authorization:Token 610c911ab6a7823b2beea2b41e96b41e7d763a04"
[Output](https://postimg.cc/TKpbSCRx)

