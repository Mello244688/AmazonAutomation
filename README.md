# Amazon Automation

## First time use:
install necessary packages and setup keyring to store your amazon password

```shell
pip install -r .\Configs\requirements.txt
```
### Using keyring to store your amazon password

1) you can either create a generic credential in windows credential manager with a network address of
amazon and your amazon username

2) or create a quick python script like the following, and run it

```python
import keyring
keyring.set_password("amazon", "username", "password")
```

## config.py

Stores the amazon username and service name used for keyring, as well as useful urls

```python
amazon_keyring = {
    "username": "[my_amazon_username]",
    "service_name": "amazon"
}

amazon_urls = {
    "signin": "https://www.amazon.com/gp/sign-in.html",
    "soy_sauce": "https://amzn.to/331XIra",
}
```