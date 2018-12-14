from django.shortcuts import redirect
from django.contrib import messages


class AnonRequiredMixin:
    redirect_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'Для смены логина необходимо выбрать пункт Выход в меню')
            return redirect(self.redirect_url)


        return super(AnonRequiredMixin, self).dispatch(request, *args, **kwargs)
        