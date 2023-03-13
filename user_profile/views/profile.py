from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import UserProfile
from ..forms import UserProfileForm
from django.urls import reverse_lazy


class ProfileBaseView(LoginRequiredMixin, View):
    model = UserProfile
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('user_profile:home')


class ProfileUpdate(ProfileBaseView, UpdateView):
    form_class = UserProfileForm
    template_name = "profile/edit.html"


class ProfileDelete(ProfileBaseView, DeleteView):
    template_name = "profile/confirm_delete.html"


class ProfileCreate(ProfileBaseView, CreateView):
    form_class = UserProfileForm
    template_name = "profile/create.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
