from elementary import ElementaryMyDearWatson


def test_get_languages():
    elem = ElementaryMyDearWatson()
    languages = elem.get_languages()
    language_test = list(filter(lambda item: item['language_name'] == 'Portuguese', languages))
    assert 'Portuguese' in language_test[0]['language_name']


def test_translation():
    elem = ElementaryMyDearWatson()
    translation = elem.translate_text('Hello', 'en', 'pt')
    assert translation.get('translations')[0]['translation'] == 'Olá'
