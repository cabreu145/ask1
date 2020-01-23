from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.generic import ListView
from .models import CrudUser

class CrudView(ListView):
    model = CrudUser
    template_name = 'core/crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        sells1 = request.GET.get('sells', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            sells = sells1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'sells':obj.sells}

        data = {
            'user': user
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        sells1 = request.GET.get('sells', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.sells = sells1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'sells':obj.sells}

        data = {
            'user': user
        }
        return JsonResponse(data)
class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)