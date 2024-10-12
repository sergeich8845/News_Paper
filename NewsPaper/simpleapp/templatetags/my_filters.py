from django import template
import re

register = template.Library()


def load_censored_words():
    with open('simpleapp/templatetags/censored_words.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


CENSORED_WORDS = load_censored_words()


@register.filter
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр 'censor' может применяться только к строкам.")

    def replace(match):
        word = match.group(0)
        return word[0] + '*' * (len(word) - 1)

    pattern = '|'.join([fr'\b{word}\b' for word in CENSORED_WORDS])
    censored_value = re.sub(pattern, replace, value, flags=re.IGNORECASE)
    return censored_value