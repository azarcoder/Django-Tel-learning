from django.shortcuts import render
from .models import Cars
# Create your views here.
def home(request):
    '''
    car_1 = Cars()
    car_1.model = 100
    car_1.name = 'BMW'
    car_1.img = '1.jpg'
    car_1.price = 2000000
    car_1.desc = 'Nice car with fast and smooth riding'

    car_2 = Cars()
    car_2.model = 200
    car_2.name = 'Audi'
    car_2.img = '2.jpg'
    car_2.price = 4000000
    car_2.desc = 'comfortable sports riding'

    car_3 = Cars()
    car_3.model = 300
    car_3.name = 'Benz'
    car_3.img = '3.jpg'
    car_3.price = 10000000
    car_3.desc = 'All rounder and fastest ever'

    cars = [car_1, car_2, car_3]
    '''

    cars = Cars.objects.all()
    return render(request, 'cars.html', {'car' : cars})