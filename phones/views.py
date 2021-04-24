from django.shortcuts import render
from phones.models import Apple, Samsung, Xiaomi


def show_catalog(request):
    template = 'catalog.html'
    # table_head = [
    #             'Модель',
    #             'Цена',
    #             'ОС',
    #             'RAM',
    #             'Память',
    #             'PPI',
    #             'Процессор',
    #             'Разрешение экрана',
    #             'Количество камер',
    #             'Оптимизация',
    #             'Качетво на рынке Android',
    #             'Соотношение цена-качество',
    #             ]

    phone = [
        Apple.objects.all(),
        Samsung.objects.all(),
        Xiaomi.objects.all(),
    ]
    context = {
        'phone': phone,
        'table_head' : [
                        'Модель',
                        'Цена',
                        'ОС',
                        'RAM',
                        'Память',
                        'PPI',
                        'Процессор',
                        'Разрешение экрана',
                        'Количество камер',
                        'Оптимизация',
                        'Качетво на рынке Android',
                        'Соотношение цена-качество',
                        ]
    }
    return render(
        request,
        template,
        context
    )
