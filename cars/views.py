from ast import keyword
from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date') # get all the data
    paginator = Paginator(cars, 4) # to show 3 objects in each one
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()  # it will retirn a LIST
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars' : paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request , 'cars/cars.html', data)

def car_detail(request , id):
    single_car = get_object_or_404(Car, pk=id) 
    # get_object_or_404 : it will return object of data for this id if exist, else will returm 404
    data = {
        'single_car' : single_car,
    }
    return render(request , 'cars/car_detail.html', data)

def search(request ):
    cars = Car.objects.order_by('-created_date')
    
    model_search = Car.objects.values_list('model', flat=True).distinct()  # it will retirn a LIST
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET: # if there was a keyword parameter in the link of request
        keyword = request.GET['keyword'] # put that keyword from the link to a parameter
        if keyword: # if the keyword not blank
            cars = cars.filter(description__icontains=keyword) # search for this keyword any where you find it

    if 'model' in request.GET: # model: at home.html  <select class="form-control search-fields" name="model">
        model = request.GET['model'] 
        if model: 
            cars = cars.filter(model__iexact=model) # model__iexact : because we need the exact matching vale from the model
    
    if 'city' in request.GET: 
        city = request.GET['city'] 
        if city: 
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET: 
        year = request.GET['year'] 
        if year: 
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET: 
        body_style = request.GET['body_style'] 
        if body_style: 
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price , price__lte=max_price)

    data  = {
        'cars': cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html' , data )