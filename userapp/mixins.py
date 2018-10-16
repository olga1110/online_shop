from django.shortcuts import redirect


class AnonRequiredMixin:
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)

        return super(AnonRequiredMixin, self).dispatch(request, *args, **kwargs)
