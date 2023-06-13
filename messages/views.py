from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.
@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    response = MessagingResponse()
    response.message('Hey Koech Whatsapp Meen!!!')
    return HttpResponse(str(response))