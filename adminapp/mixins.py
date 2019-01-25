from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin


class SuperUserMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            messages.error(request, 'Для доступа к данной странице требуются права администратора')
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
