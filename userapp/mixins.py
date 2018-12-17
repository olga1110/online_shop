from django.shortcuts import redirect
from django.contrib import messages


class AnonRequiredMixin:
    redirect_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.GET.get('next', '').startswith('/admin_custom/'):
            messages.error(request, 'Для смены логина необходимо выбрать в меню пункт Выйти')
            return redirect(self.redirect_url)
        return super(AnonRequiredMixin, self).dispatch(request, *args, **kwargs)
        