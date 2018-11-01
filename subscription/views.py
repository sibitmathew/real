from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscription

# Create your views here.
# Get all subscriptions
def get_subscriptions(request, sub_id = ''):
    if request.method == 'GET':
        if(sub_id == ''):
            subscribers = Subscription.objects.filter().values()
        else:
            subscribers = Subscription.objects.filter(id=sub_id).values()
    return JsonResponse({"subscribers": list(subscribers)})

#Submit subscription

def add_subscription(request):
    subscription_form = Subscription(request.POST or None)
    if request.method == 'POST' and request.is_ajax():
        if subscription_form.is_valid():
            subscription_form.save()
            return JsonResponse({"code": "200", "response": "Success", "msg": "Successfully Created", "id": "0"})
        else:
            return JsonResponse({"code": "401", "response": "Error", "msg": "Invalid request", })
    else:
        return JsonResponse({"code":"400","response": "Error","msg":"Bad request",})

