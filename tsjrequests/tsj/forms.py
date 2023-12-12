from django import forms
from .models import Worker, WorkType, Address, Apartment, WorkPosition, Resident, Status, RequestType, Request


class AddAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['street_name', 'house_number']
        labels = {
            'street_name': 'Название улицы',
            'house_number': 'Номер дома',
        }


class AddApartmentForm(forms.ModelForm):

    address = forms.ModelChoiceField(queryset=Address.objects.all(), empty_label="Адрес не выбран", label="Адрес")

    class Meta:
        model = Apartment
        fields = ['address', 'number']
        labels = {
            'address': "Адрес",
            'number': "Номер"
        }


class AddWorkerForm(forms.ModelForm):
    work_position = forms.ModelChoiceField(queryset=WorkPosition.objects.all(), label="Должность",
                                           empty_label="должность не выбрана")

    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'phone_number', 'work_position']
        labels = {
            'first_name': "Имя",
            'last_name': "Фамилия",
            'phone_number': "Номер телефона",
        }


class AddResidentForm(forms.ModelForm):
    apartment = forms.ModelChoiceField(queryset=Apartment.objects.all(), label="Адрес проживания",
                                           empty_label="Адрес не выбран")

    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'apartment']
        labels = {
            'first_name': "Имя",
            'last_name': "Фамилия",
        }


class AddRequestForm(forms.ModelForm):
    work_type = forms.ModelChoiceField(queryset=WorkType.objects.all(), empty_label="услуга не выбрана",
                                       label="Тип услуги")
    worker = forms.ModelChoiceField(queryset=Worker.objects.filter(), required=False,
                                    empty_label="работник не выбран",
                                    label="Работник")
    resident = forms.ModelChoiceField(queryset=Resident.objects.all(), empty_label="житель не выбран",
                                      label="Житель")
    address = forms.ModelChoiceField(queryset=Address.objects.all(), empty_label="адрес не выбран",
                                     label="Адрес")
    apartment = forms.ModelChoiceField(queryset=Apartment.objects.all(),
                                       empty_label="квартира не выбрана",
                                       label="Квартира")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label="статус заявки не выбран",
                                    label="Статус заявки")
    request_type = forms.ModelChoiceField(queryset=RequestType.objects.all(), empty_label="тип заявки не выбран",
                                          label="Тип заявки")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['apartment'].choices

    class Meta:
        model = Request
        fields = ['work_type', 'worker', 'resident', 'address', 'apartment', 'status', 'description', 'request_type']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

