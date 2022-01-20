# coding=utf-8

from decouple import config

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


class ElementaryMyDearWatson:

    def __init__(self):
        self.apikey = config('apikey')
        self.url = config('url')
        self.version = '2018-05-01'

    def authentication(self):
        return IAMAuthenticator(self.apikey)

    def get_language_translator(self):

        # Return a list of dictionary with the languages.

        language_translator = LanguageTranslatorV3(version=self.version, authenticator=self.authentication())
        language_translator.set_service_url(self.url)
        return language_translator

    def get_languages(self):

        # Return a dict with the translated text.

        languages = self.get_language_translator().list_languages().get_result()
        available_languages = [{'language_name': language['language_name'], 'language': language['language']} for
                               language in languages.get('languages')]
        return available_languages

    def translate_text(self, text, translate_from, translate_to):
        translation = self.get_language_translator().translate(text=text,
                                                               model_id=f'{translate_from}-{translate_to}').get_result()
        return translation
