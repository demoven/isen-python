from django.shortcuts import redirect
from django.views.generic import ListView

from products.models import Product


def RedirectHomeView(request):
    '''
    Redirect url from '/' to '/home/'
    '''
    return redirect('home')

class HomeView(ListView):
    '''
    Renders home page with all the products
    '''
    template_name = 'home.html'
    model = Product

    def get_queryset(self):
        """
        Override get_queryset to apply sorting logic
        """
        sort_order = self.request.GET.get('sort', 'asc')
        if sort_order == 'desc':
            return Product.objects.all().order_by('-price')
        return Product.objects.all().order_by('price')