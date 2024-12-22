from django import template

register = template.Library()

CENSOR_WORDS = [
    'редиска',
    'дурак',
]

@register.filter()
def censor(text):
    text_words = text.split()
    for i in range(len(text_words)):
        word = text_words[i]
        if word in CENSOR_WORDS:
            text_words[i] = word[0] + '*' * len(word - 1)
    return ' '.join(text_words)