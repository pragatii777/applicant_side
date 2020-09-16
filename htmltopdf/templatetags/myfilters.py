from django import template

register=template.Library()

def correct(value):
    value=value.title()
    return value.replace('_',' ')

def forvalue(value):
    if value[:2]=="[\"":
        value=value[2:len(value)-2]
    return value

register.filter('correct',correct)
register.filter('forvalue',forvalue)
