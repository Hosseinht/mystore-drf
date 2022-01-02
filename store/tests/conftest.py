from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest


# fixtures or reusable functions that we use here pytest will
# automatically load them without us having to import this module

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authentication(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))

    return do_authentication
