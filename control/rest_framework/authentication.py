from rest_framework.authentication import TokenAuthentication

from control.models import Token


class LongTokenAuthentication(TokenAuthentication):
    model = Token