from django.shortcuts import render
from django.views.generic import View
import json
from polls.models import Profile, Balance
import random
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import BaseDetailView
from polls.services.services import activebalance

class ProfileMixin:
    @staticmethod
    def render_to_response(contects):
        balances = []
        for balance in contects.balance.all():
            balances.append({
                'number': balance.number,
                'status': balance.status,
            })
        return JsonResponse({
            'id': contects.id,
            'name': contects.name,
            'surname': contects.surname,
            'balances': balances
        })


@method_decorator(csrf_exempt, name='dispatch')
class ProfileCreateAPI(ProfileMixin, View):
    def post(self, request):
        body = json.loads(request.body)
        data = {
            'name': body.get('name'),
            'surname': body.get('surname')
        }
        profile = Profile.objects.create(**data)
        Balance.objects.create(number=str(random.randint(1, 100000)), profile=profile)
        bal = Balance.objects.create(number=str(random.randint(1, 100000)), profile=profile)
        activebalance.delay(bal.id)

        contects = Profile.objects.filter(id=profile.id).prefetch_related('balance').first()
        return self.render_to_response(contects)


class ProfileDetailAPI(ProfileMixin, BaseDetailView):
    model = Profile
    http_method_names = ['get']

    def get_queryset(self):
        return Profile.objects.filter(id=self.kwargs['pk']).prefetch_related('balance')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs).get('object')
