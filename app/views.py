from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(full_name=full_name, email=email, password=password)

            if user is not None:
                if user.is_active():
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})


