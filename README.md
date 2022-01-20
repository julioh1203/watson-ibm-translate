
# IBM WATSON TRANSLATE


## Description
This project provides a class to translate texts using IBM Watson SDK.

## Requirements
- Python 3.9 or above
- python-decouple
- ibm-watson
- pytest (optional)

## Installation
First of all, you need to creat an account in IBM Cloud (https://cloud.ibm.com/login). 

After, you need to create a .env file in the root directory with these content:

apikey=" "

url=" "

## Usage

1. Return a list with languages supported:
> elem = ElementaryMyDearWatson()
> 
> languages = elem.get_languages()

2. Translate a text. It requires a text, the language from, and the language to translate the text:
>
> elem = ElementaryMyDearWatson()
> 
> translation = elem.translate_text(text, translate_from, translate_to)








