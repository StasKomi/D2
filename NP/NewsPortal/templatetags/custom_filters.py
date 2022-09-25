from django import template

register = template.Library()

BAD_WORDS = ('world', 'striker', 'new', 'chaos', 'target')


@register.filter()
def censor(text):
    sp = text.split()
    sp2 = []
    for i in sp:
        if i.lower() in BAD_WORDS:
            sp2.append(i[0] + (len(i) - 1) * '*')
        else:
            sp2.append(i)
    return " ".join(sp2)
