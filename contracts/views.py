from django.shortcuts import render
from django.views import View
from .forms import UserForm, LoginForm, CreateContractForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import ContractModel, WebsiteUser
from django.http import HttpResponseRedirect
from django.urls import reverse


class HomePage(View):
    template_name = 'home_page.html'

    def get(self, request):
        print(request.user.is_authenticated)
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
            contract_record = form.save()
            contract_record.author = self.request.user
            contract_record.save()
            return render(request, self.template_name, {'form': form, 'message': 'Successfully created!'})


class AllContracts(View):
    template_name = 'all-contracts.html'

    def get(self, request):
        all_posts = ContractModel.objects.all()
        return render(self.request, self.template_name, {'all_posts': all_posts})


class MyContracts(View):
    template_name = 'my-contracts.html'

    def get(self, request):
        logged_in_user = request.user
        logged_in_user_posts = ContractModel.objects.filter(author=logged_in_user)
        return render(self.request, self.template_name, {'posts': logged_in_user_posts})
        # return ContractModel.objects.all()


from django.http import HttpResponse


class Login(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request=request, email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                    # return render(request, 'home_page.html', locals())
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

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})
