from django import template
import datetime

register = template.Library()

@register.simple_tag
def my_tag(arg):
    return f'{arg}elo'

@register.simple_tag
def remaining_days(input_date):
    today_date = datetime.datetime.now().replace(tzinfo=None)
    input_date = input_date.replace(tzinfo=None)
    result = input_date - today_date
    result = str(result).split()[0]
    if len(str(result).split()[0])>7:
        result = 0
    return result

@register.simple_tag
def remaining_days_hours(input_date):
    now = datetime.datetime.today().replace(tzinfo=datetime.timezone.utc)
    total_sec = int((input_date - now).total_seconds())
    if total_sec<0:
        days = 0
        hours = 0
    else:
        hours = int((total_sec/3600)%24)
        days = int(total_sec/86400)
    result = f'{days}d {hours}h'
    return result



