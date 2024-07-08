from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.generic import BSModalCreateView


from .models import Restaurant, Review

from .forms import (
    CreateRestaurantForm
)
    

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


class create_restaurant(LoginRequiredMixin, FormView):
    template_name = 'restaurants/create.html'
    form_class = CreateRestaurantForm

    def form_valid(self, form):
        restaurant = Restaurant()
        restaurant.name = form.cleaned_data['name']
        restaurant.street_address = form.cleaned_data['street_address']
        restaurant.description = form.cleaned_data['description']
        Restaurant.save(restaurant)

        messages.success(self.request, _('New restaurant has been successfully created.'))

        return redirect('restaurants:list')

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
