from django.db import models
from django.urls import reverse


class Request(models.Model):
    work_type = models.ForeignKey('WorkType', on_delete=models.PROTECT, verbose_name="Тип услуги")
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, null=True, verbose_name="Работник")
    resident = models.ForeignKey('Resident', on_delete=models.PROTECT, verbose_name="Житель")
    address = models.ForeignKey('Address', on_delete=models.PROTECT, verbose_name="Адрес", blank=True)
    apartment = models.ForeignKey('Apartment', on_delete=models.PROTECT, verbose_name="Квартира")
    status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1, verbose_name="Статус")
    request_type = models.ForeignKey('RequestType', on_delete=models.PROTECT, verbose_name="Тип заявки")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"Заявка на {self.work_type} по адресу: {self.address}"

    def get_absolute_url(self):
        return reverse('update_request', kwargs={'request_id': self.pk})

    class Meta:
        ordering = ['pk']


class RequestType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Worker(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=255, null=True, verbose_name="Номер телефона", blank=True)
    work_position = models.ForeignKey('WorkPosition', on_delete=models.PROTECT, verbose_name="Должность")
    # work_types = models.ManyToManyField('WorkType')

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        ordering = ['pk']

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.work_position}"

    def get_absolute_url(self):
        return reverse('update_worker', kwargs={'worker_id': self.pk})


class Resident(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # address = models.ForeignKey('Address', on_delete=models.PROTECT)
    apartment = models.ForeignKey('Apartment', on_delete=models.PROTECT)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('update_resident', kwargs={'resident_id': self.pk})


class WorkType(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Стоимость")
    description = models.TextField(null=True, verbose_name="Описание")
    work_position = models.ForeignKey('WorkPosition', on_delete=models.PROTECT, verbose_name="Должность")
    request_type = models.ForeignKey('RequestType', on_delete=models.PROTECT, verbose_name="Тип заявки")

    class Meta:
        verbose_name = "Тип работы"
        verbose_name_plural = "Типы работ"
        ordering = ['pk']

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Address(models.Model):
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField()

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        ordering = ['pk']

    def __str__(self):
        return f"{self.street_name}, дом {self.house_number}"

    def get_absolute_url(self):
        return reverse('update_address', kwargs={'address_id': self.pk})

    def as_dict(self):
        address = {
            'id': self.pk,
            'street-name': self.street_name,
            'house-number': self.house_number,
        }
        return address


class Apartment(models.Model):
    number = models.IntegerField()
    address = models.ForeignKey('Address', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        ordering = ['pk']

    def __str__(self):
        return f"{self.address}, кв. {self.number}"

    def get_absolute_url(self):
        return reverse('update_apartment', kwargs={'apartment_id': self.pk})

    def as_dict(self):
        apartment = {
            'id': self.pk,
            'number': self.number,
            'address': Address.as_dict(self.address),
        }
        return apartment


class WorkPosition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ['pk']

    def __str__(self):
        return self.title

