import json
# import simplejson
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from . import models


def update_database(product):
    obj = models.Product.objects.get(name=product)

    path = 'mainapp/static/mainapp/files/description.json'
    with open(path) as json_data:
        data = json.load(json_data)

    obj.price = data['description'][product]
    obj.save()


def mainapp_catalog(request):

    query = models.Category.objects.all()

    # products = Product.objects.all()[: 4]
    # content = {'title': title, 'products': products}

    product_items = {'links':
                         [{'href': '/Catalog/Tables/Table/', 'src': '/static/img/table.jpg', 'name': 'Обеденный стол(стекло)', },
                          {'href': '/Catalog/Sofas/Sofa/', 'src': '/static/img/sofa.png', 'name': 'Диван для кухни', },
                          {'href': '/Catalog/Suite/Set/', 'src': '/static/img/kitchen_set.jpg', 'name': 'Кухонный гарнитур', },
                          {'href': '/Catalog/Suite/Couch/', 'src': '/static/img/corner_komfort.jpg',
                           'name': 'Кухонный уголок(комфорт)', },
                          ],
                     'proc': 20,
                     'categories': query,
                     }

    # product_items = {'links':
    #                      [{'href': 'Table/', 'src': '/static/img/table.jpg','name': 'Обеденный стол(стекло)', },
    #                       {'href': 'Sofa/', 'src': '/static/img/sofa.png', 'name': 'Диван для кухни', },
    #                       {'href': 'Kitchen_set/', 'src': '/static/img/kitchen_set.jpg', 'name': 'Кухонный гарнитур',},
    #                       {'href': 'Area/', 'src': '/static/img/corner_komfort.jpg', 'name': 'Кухонный уголок(комфорт)',},
    #                       ],
    #                  'name':query,
    #                  'proc': 20,
    #                  }
    return render(request, 'mainapp/catalog.html', product_items)


def mainapp_Contacts(request):
    # context = {'contact_details':
    #     {
    #         'tel': None, # '8(342)229-78-28'
    #         'address': 'г. Пермь, ул. Леонова, 68',
    #         'email': 'info@kitchen-perm.ru',
    #         'start_time': 10,
    #         'end_time': 21,
    #     }}

    path = 'mainapp/static/mainapp/files/organization.json'
    with open(path) as json_data:
        context = json.load(json_data)

    template = get_template('mainapp/Contacts.html')
    return HttpResponse(template.render(context))


def mainapp_index(request):
    context = {'company':
                   {'title': 'cozy kitchen',
                    'advertisement': 'Самая лучшая мебель для кухни здесь!!!'}
               }
    return render(request, 'mainapp/index.html', context)


def mainapp_registration(request):
    context = {'reg': 'Регистрация'}
    return render(request, 'mainapp/registration.html', context)


# Страницы товаров из каталога
# def mainapp_area_comfort(request):
#     update_database('Уголок')
#     table = models.Product.objects.get(name='Уголок')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/area_comfort.html', context)
#
#
# def mainapp_kitchen_set(request):
#     update_database('Гарнитур')
#     table = models.Product.objects.get(name='Гарнитур')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/kitchen_set.html', context)
#
#
# def mainapp_sofa(request):
#     update_database('Диван')
#     table = models.Product.objects.get(name='Диван')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/sofa.html', context)
#
#
# def mainapp_table(request):
#     update_database('Стол')
#     table = models.Product.objects.get(name='Стол')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#
#     return render(request, 'mainapp/components/product.html', context)


def product_detail(request, title):
    update_database(title)
    obj = get_object_or_404(models.Product, name=title)
    context = {'product': obj, 'new_price': obj.price * (1 - obj.discount / 100)}
    return render(request, 'mainapp/components/product.html', context)

def category_detail(request, title):
    cat = models.Category.objects.get(name=title)

    products = models.Product.objects.filter(category=cat.id)

    return render(request, 'mainapp/components/categories.html', {'products':products, 'category':cat})


