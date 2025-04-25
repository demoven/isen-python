from django.urls import reverse, resolve
from django.test import Client

from home.views import RedirectHomeView, HomeView
from products.models import Product

from pytest_django.asserts import assertTemplateUsed
import pytest


CLIENT = Client()


@pytest.mark.django_db
def test_slash_route():

    """ 
    Our test approach starts with testing the 'redirect_home' route, whether it maps to 'RedirectHomeView'
    or not, then we test if RedirectHomeView redirected to '/home/' route. 
    Next we test if 'home' route maps to 'HomeView' and we check if the HomeView renders the 'home.html' template,
    also we check if it is rendering the data from the correct model (Product)
    """

    # Testing if the 'redirect_home' route maps to 'RedirectHomeView'
    url = reverse('redirect_home')
    assert resolve(url).func, RedirectHomeView

    # Testing if 'RedirectHomeView' redirected to '/home/' route
    response = CLIENT.get(reverse('redirect_home'))
    assert response.status_code == 302
    assert response.url == '/home/'

    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product



@pytest.mark.django_db
def test_home_route():

    """
    For this test approach, we are simply testing if 'home' route maps to 'HomeView', 
    and the 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    """

    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product


@pytest.mark.django_db
def test_home_sorting():

    """
    Test d'intégration pour vérifier que la vue HomeView trie correctement les produits
    par prix croissant et décroissant en fonction du paramètre 'sort'.
    """

    # Création de produits pour le test
    Product.objects.create(name="Produit A", price=10.0)
    Product.objects.create(name="Produit B", price=20.0)
    Product.objects.create(name="Produit C", price=15.0)

    # Test tri par prix croissant
    response_asc = CLIENT.get(reverse('home') + '?sort=asc')
    assert response_asc.status_code == 200
    assertTemplateUsed(response_asc, 'home.html')
    products_asc = list(response_asc.context['object_list'])
    assert [product.price for product in products_asc] == [10.0, 15.0, 20.0]

    # Test tri par prix décroissant
    response_desc = CLIENT.get(reverse('home') + '?sort=desc')
    assert response_desc.status_code == 200
    assertTemplateUsed(response_desc, 'home.html')
    products_desc = list(response_desc.context['object_list'])
    assert [product.price for product in products_desc] == [20.0, 15.0, 10.0]
