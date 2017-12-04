import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_tango.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages=[
        {"title":"offical python tutorial","url":"http://doc.python.org/","views":32},
        {"title":"how to think like a computer scientist","url": "http://greenteapress.com/","views": 32},
        {"title": "the third part", "url": "http://doc.thirdparit.org/","views": 32},
    ]

    django_pages = [
        {"title": "django python tutorial", "url": "http://django.python.org/","views":32},
        {"title": "django_to be a computer scientist", "url": "http://django.greenteapress.com/","views":32},
        {"title": "django the third part", "url": "http://doc.djangothirdparit.org/","views":32},
    ]

    other_pages = [
        {"title": "part one", "url": "http://one.python.org/","views":32},
        {"title": "part two", "url": "http://two.greenteapress.com/","views":32},
        {"title": "part three", "url": "http://the.djangothirdparit.org/","views":32},
    ]

    cats = {"python": {"pages": python_pages, "views": 128,"likes": 64},
            "django": {"pages": django_pages, "views": 64, "likes": 32},
            "other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}
    for cat,cat_data in cats.items():
        c=add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"],p["views"])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0}-{1}".format(str(c),str(p)))

def add_page(cat,title,url,views=0,likes=0):
    p=Page.objects.get_or_create(category=cat,title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    c=Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__=='__main__':
    print("start rango populatin script")
    populate()



