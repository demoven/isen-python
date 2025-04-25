from django.urls import reverse 
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest

from home.views import RedirectHomeView, HomeView
from products.models import Product


def test_RedirectHomeView():
    client = Client()
    response = client.get(reverse('redirect_home'))

    """ 
    Testing if our RedirectHomeView redirects succuessfully (status_code 302)
    For the second assert, We are testing if we redirect to the '/home/' url
     """

    assert response.status_code == 302
    assert response.url == '/home/'

@pytest.mark.django_db
def test_HomeView():
    client = Client()
    response = client.get(reverse('home'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')

@pytest.mark.django_db
def test_HomeView_sorting():
    client = Client()

    # Création de produits pour le test
    Product.objects.create(name="Produit A", price=10.0)
    Product.objects.create(name="Produit B", price=20.0)
    Product.objects.create(name="Produit C", price=15.0)

    # Test tri par prix croissant
    response_asc = client.get(reverse('home') + '?sort=asc')
    assert response_asc.status_code == 200
    assertTemplateUsed(response_asc, 'home.html')
    products_asc = list(response_asc.context['object_list'])
    assert [product.price for product in products_asc] == [10.0, 15.0, 20.0]

    # Test tri par prix décroissant
    response_desc = client.get(reverse('home') + '?sort=desc')
    assert response_desc.status_code == 200
    assertTemplateUsed(response_desc, 'home.html')
    products_desc = list(response_desc.context['object_list'])
    assert [product.price for product in products_desc] == [20.0, 15.0, 10.0]