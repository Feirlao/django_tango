import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_tango.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages=[
        {"title":"offical python tutorial","url":"http://doc.python.org/"},
        {"title":"how to think like a computer scientist","url": "http://greenteapress.com/"},
        {"title": "the third part", "url": "http://doc.thirdparit.org/"},
    ]

    django_pages = [
        {"title": "django python tutorial", "url": "http://django.python.org/"},
        {"title": "django_to be a computer scientist", "url": "http://django.greenteapress.com/"},
        {"title": "django the third part", "url": "http://doc.djangothirdparit.org/"},
    ]

    other_pages = [
        {"title": "part one", "url": "http://one.python.org/"},
        {"title": "part two", "url": "http://two.greenteapress.com/"},
        {"title": "part three", "url": "http://the.djangothirdparit.org/"},
    ]

    cats={"python":{"pages":python_pages},
          "django":{"pages":django_pages},
          "other frameworks":{"pages":other_pages} }

    for cat,cat_data in cats.items():
        c=add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0}-{1}".format(str(c),str(p)))

def add_page(cat,title,url,views=0):
    p=Page.objects.get_or_create(category=cat,title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c=Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__=='__main__':
    print("start rango populatin script")
    populate()



