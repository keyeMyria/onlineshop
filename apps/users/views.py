from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
# Create your models here.

User = get_user_model()       # get settings.AUTH_USER_MODEL


class CustomBackend(ModelBackend):
    """
    自定义用户验证，要继承自ModelBackend
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username)|Q(email=username))   # add support e-mail addr login
            if user.check_password(password):
                return user
        except Exception as e:
            return None