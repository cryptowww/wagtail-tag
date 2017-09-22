## wagtail snippet

> $ wagtail start wagsnip
> $ cd wagsnip
> $ mkdir home/templatetags
> $ mkdir templates/home/tags
> $ cd templatestags

_*** 新建文件 mytags.py ***_


```python

from django import template
from home.models import Advert

register = template.Library()


# Advert snippets
@register.inclusion_tag('home/tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'adverts': Advert.objects.all(),
        'request': context['request'],
    }

```


_*** 新建snippet模板文件 ***_
> $ cd templates/home/tags

```python
{% for advert in adverts %}
    <p>
        <a href="{{ advert.url }}">
            {{ advert.text }}
        </a>
    </p>
{% endfor %}

```

*** 修改home_page模板文件***

#### 引用标签
{% load mytags %}

#### 使用标签

{% adverts %}


*** 修改models.py ***
> 修改后，可以在管理控制台看到标签
> 

TO DO