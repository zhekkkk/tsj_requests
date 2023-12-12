import json

from django.core.paginator import Paginator
from django.db.models import Max
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.serializers import serialize

from tsj.forms import AddAddressForm, AddWorkerForm, AddRequestForm, AddApartmentForm, AddResidentForm
from tsj.models import WorkType, WorkPosition, Address, Worker, Apartment, Resident, Request, Status, RequestType

menu = [
    {'title': "Работники", 'url_name': "workers"},
    {'title': "Жители", 'url_name': "residents"},
    {'title': "Заявки", 'url_name': "requests"},
    {'title': "Адреса", 'url_name': "addresses"},
    {'title': "Квартиры", 'url_name': "apartments"},
]

errors = {
    'wrong_position_error': "ошибка, специализация работника не соответствует типу услуги",
    'wrong_request_type': "ошибка, тип заявки не соответствует типу услуги",
    'wrong_request_status': "неправильно выбран статус заявки",
    'wrong_apartment': "выбрана неправильная квартира",
}

# не заработало
class AjaxUpdateView(View):
    def get(self, request, *args, **kwargs):
        address = request.GET.get('apartment', None)
        if address:
            data = Apartment.objects.filter(address_id=address)
            serialized_data = serialize('json', data)
            print(data)
            apartments = [Apartment.as_dict(item) for item in data]
            print(serialized_data)
            return JsonResponse({'apartment': serialized_data})
        return JsonResponse({'apartment': []})


def index(request):
    data = {
        'title': 'Главная страница информационного портала ТСЖ "Солнышко"',
        'menu': menu,
    }
    return render(request, 'tsj/index.html', context=data)


def show_workers(request):
    workers = Worker.objects.all()
    number_of_workers = Worker.objects.count()
    data = {
        'title': 'Работники',
        'menu': menu,
        'items': workers,
        'number': number_of_workers,
    }
    return render(request, 'tsj/list_workers.html', context=data)


def show_residents(request):
    residents = Resident.objects.all()
    number_of_residents = Resident.objects.count()
    data = {
        'title': 'Зарегистрированные жители',
        'menu': menu,
        'items': residents,
        'number': number_of_residents,
    }
    return render(request, 'tsj/list_residents.html', context=data)


def show_requests(request):
    requests = Request.objects.all()
    number_of_requests = Request.objects.count()
    max_price = WorkType.objects.aggregate(Max('price'))
    data = {
        'title': 'Все заявки',
        'menu': menu,
        'items': requests,
        'number': number_of_requests,
        'max_price': max_price['price__max']
    }
    return render(request, 'tsj/list_requests.html', context=data)


def show_request_by_type(request, type_slug):
    type = get_object_or_404(RequestType, slug=type_slug)
    requests = Request.objects.filter(request_type_id=type.pk)
    number_of_requests = requests.count()
    data = {
        'title': f"Заявки типа: {type.title}",
        'menu': menu,
        'items': requests,
        'number': number_of_requests,
    }
    return render(request, 'tsj/list_requests.html', context=data)


def show_worker_by_position(request, position_slug):
    position = get_object_or_404(WorkPosition, slug=position_slug)
    workers = Worker.objects.filter(work_position_id=position.pk)
    number_of_workers = workers.count()
    data = {
        'title': f"Работники по специальности: {position.title}",
        'menu': menu,
        'items': workers,
        'number': number_of_workers,
    }
    return render(request, 'tsj/list_workers.html', context=data)


def update_request(request, request_id=None):
    if request_id is not None:
        instance = Request.objects.get(pk=request_id)
    else:
        instance = None
    if request.method == 'POST':
        form = AddRequestForm(request.POST, instance=instance)
        if form.is_valid():
            status = form.cleaned_data['status']
            work_type = form.cleaned_data['work_type']
            worker = form.cleaned_data['worker']
            request_type = form.cleaned_data['request_type']
            address = form.cleaned_data['address']
            apartment = form.cleaned_data['apartment']
            if worker.work_position != work_type.work_position:
                form.add_error('worker', errors['wrong_position_error'])
            if request_type.pk != work_type.request_type_id:
                form.add_error('request_type', errors['wrong_request_type'])
            if worker is not None and (status.pk == 1 or status.pk == 5):
                form.add_error('status', errors['wrong_request_status'])
            if apartment.address != address:
                form.add_error('apartment', errors['wrong_apartment'])
            if form.is_valid():
                form.save()
                return redirect('requests')
        else:
            form.add_error(None, "ошибка")
    else:
        form = AddRequestForm(instance=instance)
    data = {
        'menu': menu,
        'title': 'Добавить/изменить заявку',
        'form': form,
    }
    return render(request, 'tsj/create.html', data)


def update_address(request, address_id=None):
    if address_id is not None:
        instance = Address.objects.get(pk=address_id)
    else:
        instance = None
    if request.method == 'POST':
        form = AddAddressForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('addresses')
        else:
            form.add_error(None, "ошибка")
    else:
        form = AddAddressForm(instance=instance)

    data = {
        'menu': menu,
        'title': 'Добавить/изменить адрес',
        'form': form,
    }
    return render(request, 'tsj/create.html', data)


def update_worker(request, worker_id=None):
    if worker_id is not None:
        instance = Worker.objects.get(pk=worker_id)
    else:
        instance = None
    if request.method == 'POST':
        form = AddWorkerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('workers')
        else:
            form.add_error(None, "ошибка")
    else:
        form = AddWorkerForm(instance=instance)

    data = {
        'menu': menu,
        'title': 'Добавить/изменить адрес',
        'form': form,
    }
    return render(request, 'tsj/create.html', data)


def update_resident(request, resident_id=None):
    if resident_id is not None:
        instance = Resident.objects.get(pk=resident_id)
    else:
        instance = None
    if request.method == 'POST':
        form = AddResidentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('residents')
        else:
            form.add_error(None, "ошибка")
    else:
        form = AddResidentForm(instance=instance)

    data = {
        'menu': menu,
        'title': 'Добавить/изменить жителя',
        'form': form,
    }
    return render(request, 'tsj/create.html', data)


def update_apartment(request, apartment_id=None):
    if apartment_id is not None:
        instance = Apartment.objects.get(pk=apartment_id)
    else:
        instance = None
    if request.method == 'POST':
        form = AddApartmentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('apartments')
        else:
            form.add_error(None, "ошибка")
    else:
        form = AddApartmentForm(instance=instance)

    data = {
        'menu': menu,
        'title': 'Добавить/изменить квартиру',
        'form': form,
    }
    return render(request, 'tsj/create.html', data)


def delete_request(request, request_id):
    Request.objects.get(pk=request_id).delete()
    return redirect('requests')


def delete_address(request, address_id):
    Address.objects.get(pk=address_id).delete()
    return redirect('addresses')


def delete_worker(request, worker_id):
    Worker.objects.get(pk=worker_id).delete()
    return redirect('workers')


def delete_resident(request, resident_id):
    Worker.objects.get(pk=resident_id).delete()
    return redirect('residents')


def delete_apartment(request, apartment_id):
    Worker.objects.get(pk=apartment_id).delete()
    return redirect('apartments')


def show_request(request, req_id):
    return HttpResponse("список заявок за счёт жильцов")


def show_addresses(request):
    addresses = Address.objects.all()
    number_of_addresses = Address.objects.count()
    data = {
        'title': "Адреса обслуживания",
        'menu': menu,
        'items': addresses,
        'number': number_of_addresses,
    }
    return render(request, 'tsj/list_addresses.html', context=data)


def show_apartmennnnnts(request):
    page = int(request.GET.get('page', 1))
    per_page = 40
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    data = Apartment.objects.all()[start_index:end_index].values()
    return JsonResponse({'data': list(data)})


def show_apartments(request):
    apartments = Apartment.objects.all()
    number_of_apartments = Apartment.objects.count()
    p = Paginator(apartments, 30)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    data = {
        'title': "Список квартир",
        'menu': menu,
        'items': page_obj,
        'number': number_of_apartments,
    }
    return render(request, 'tsj/list_apartments.html', context=data)


def show_work_types(request, work_position_id):
    work_pos = get_object_or_404(WorkPosition, id=work_position_id)
    work_types = WorkType.objects.filter(work_position_id=work_position_id)
    data = {
        'title': f"Должность: {work_pos.title}",
        'menu': menu,
        'items': work_types,
    }

    return render(request, 'tsj/list_work_types.html', context=data)