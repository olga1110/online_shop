import json
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse


def mainapp_catalog(request):
    product_items = {'links':
        [{'href': '#', 'src': '/static/img/table.jpg', 'name': 'Обеденный стол(стекло)', },
        {'href': '#', 'src': '/static/img/sofa.png', 'name': 'Диван для кухни', },
        {'href': '#', 'src': '/static/img/kitchen_set.jpg', 'name': 'Кухонный гарнитур', },
        # {'href': '#', 'src': '/static/img/kukhonnyy_ugolok_komfort.jpg', 'name': 'Кухонный уголок(комфорт)', },
        ],
                    'proc':30.5555555555555555,
    }
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
    context = {'reg':'Регистрация'}
    return render(request, 'mainapp/registration.html', context)

# Create your views here.
