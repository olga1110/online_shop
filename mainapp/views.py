import json
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from . import models


def mainapp_catalog(request):
    # query = models.Product.object.all()
    # query = get_object_or_404(models.Product)

    # products = Product.objects.all()[: 4]
    # content = {'title': title, 'products': products}


    product_items = {'links':
                         [{'href': 'Table/', 'src': '/static/img/table.jpg','name': 'Обеденный стол(стекло)', },
                          {'href': 'Sofa/', 'src': '/static/img/sofa.png', 'name': 'Диван для кухни', },
                          {'href': 'Kitchen_set/', 'src': '/static/img/kitchen_set.jpg', 'name': 'Кухонный гарнитур',},
                          {'href': 'Area/', 'src': '/static/img/corner_komfort.jpg', 'name': 'Кухонный уголок(комфорт)',},
                          ],
                     'proc': 20,
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
def mainapp_area_comfort(request):
    table = models.Product.objects.get(name='Уголок')
    context = {'product':table, 'new_price':table.price*(1-table.discount/100)}
    return render(request, 'mainapp/products/area_comfort.html', context)


def mainapp_kitchen_set(request):
    table = models.Product.objects.get(name='Гарнитур')
    context = {'product':table, 'new_price':table.price*(1-table.discount/100)}
    return render(request, 'mainapp/products/kitchen_set.html', context)


def mainapp_sofa(request):
    table = models.Product.objects.get(name='Диван')
    context = {'product':table, 'new_price':table.price*(1-table.discount/100)}
    return render(request, 'mainapp/products/sofa.html', context)


def mainapp_table(request):
    table = models.Product.objects.get(name='Стол')
    context = {'product':table, 'new_price':table.price*(1-table.discount/100)}

    return render(request, 'mainapp/products/table.html', context)
