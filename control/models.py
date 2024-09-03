import binascii
import os

import rest_framework.authtoken.models
from django.db import models
from django.utils.translation import gettext_lazy as _


class Token(rest_framework.authtoken.models.Token):
    key = models.CharField(_("Key"), max_length=120, primary_key=True)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(60)).decode()
