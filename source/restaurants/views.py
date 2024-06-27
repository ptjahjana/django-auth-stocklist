from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

from .models import Restaurant, Review

def list(request):
    print('Request for index page received')
    restaurants = Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review'))
    lastViewedRestaurant = request.session.get("lastViewedRestaurant", False)
    return render(request, 'restaurants/index.html', {'LastViewedRestaurant': lastViewedRestaurant, 'restaurants': restaurants})

@cache_page(60)
def details(request, id):
    print('Request for restaurant details page received')
    restaurant = get_object_or_404(Restaurant, pk=id)
    request.session["lastViewedRestaurant"] = restaurant.name
    return render(request, 'restaurants/details.html', {'restaurant': restaurant})


def create(request):
    print('Request for add restaurant page received')
    return render(request, 'restaurants/create.html')


@csrf_exempt
def add(request):
    try:
        name = request.POST['name']
        street_address = request.POST['street_address']
        description = request.POST['description']
    except (KeyError):
        # Redisplay the form
        return render(request, 'restaurants/create.html', {
            'error_message': "You must include a restaurant name, address, and description",
        })
        
    else:
        restaurant = Restaurant()
        restaurant.name = name
        restaurant.street_address = street_address
        restaurant.description = description
        Restaurant.save(restaurant)

        return redirect('restaurants:details', args=(restaurant.id,))


@csrf_exempt
def add_review(request):
    id = request.POST['id']
    restaurant = get_object_or_404(Restaurant, pk=id)
    try:
        user_name = request.POST['user_name']
        rating = request.POST['rating']
        review_text = request.POST['review_text']
    except (KeyError):
        # Redisplay the form.
        return render(request, 'restaurants/details.html', {
            'error_message': "Error adding review",
        })
    else:
        review = Review()
        review.restaurant = restaurant
        review.review_date = timezone.now()
        review.user_name = user_name
        review.rating = rating
        review.review_text = review_text
        Review.save(review)

        return redirect('restaurants:details', args=(restaurant.id,))
