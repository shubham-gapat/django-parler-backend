from django.conf import settings
from django.core.cache import cache
from googletrans import Translator


def translate_with_cache(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang).text
    return translation


def convert_data(data):
    response = {}
    for language in settings.LANGUAGES:
        lang_responses = {}
        for key, value in data.items():
            if value:
                if type(value) is str and value != "":
                    translated = translate_with_cache(value, language[0])
                    lang_responses[key] = translated
                elif type(value) is dict:
                    if value is not None:
                        response = {}
                        for k, val in value.items():
                            if type(val) is str and val != "" and val:
                                translated = translate_with_cache(val, language[0])
                                response[k] = translated
                            else:
                                response[k] = val
                        lang_responses[key] = response
                    else:
                        lang_responses[key] = value
                elif type(value) is list:
                    translated_list = []
                    for val in value:
                        translated = translate_with_cache(val, language[0])
                        translated_list.append(translated)
                    lang_responses[key] = translated_list
                else:
                    lang_responses[key] = value
            else:
                lang_responses[key] = value
        response[language[0]] = lang_responses
    return response


class ResponseInfo(object):
    """
    Class for setting how API should send response.
    """

    def __init__(self, **args):
        self.response = {
            "status_code": args.get("status", 200),
            "error": args.get("error", None),
            "data": args.get("data", []),
            "message": [args.get("message", "Success")],
        }