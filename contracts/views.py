from django.shortcuts import render
from django.views import View, generic
from .forms import UserForm, LoginForm, CreateContractForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import redirect
from .models import ContractModel
from django.contrib.auth.models import User


class HomePage(View):
    template_name = 'home_page.html'

    def get(self, request):
        return render(request, self.template_name)


class CreateContract(View):
    form_class = CreateContractForm
    template_name = 'create_contract.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            contract_record = ContractModel(name=name)
            contract_record.save()
            return render(request, self.template_name, {'form': form, 'message': 'Successfully created!'})


class MyContracts(generic.ListView):
    template_name = 'my-contracts.html'

    # TODO display contracts of each user specifically

    def get_queryset(self):
        return ContractModel.objects.all()


class Login(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})


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

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})


