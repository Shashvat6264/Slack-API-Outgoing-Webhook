from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
import json
from django.template import loader
from .models import Message
from .extra import extract_link
# Create your views here.
token = 'TOKEN_ID'
def gets(request):
    if request.method == 'POST':
        # print(request.body)
        # json_data = json.loads(request.body)
        json_data = request.POST
        # print(json_data)
        try:
            data = json_data['text']
            # data = request.body
            data = extract_link(data)
            if data != '0':
                token_rec = json_data['token']
                # print(token_rec)
                if token_rec == token:
                    m = Message()
                    m.text = data
                    m.save()
        except KeyError:
            return HttpResponseServerError("Malformed data")
        return HttpResponse('Got it')
    else:
        all_messages = Message.objects.all()
        template = loader.get_template('get/index.html')
        context = {'msg': all_messages}
        return HttpResponse(template.render(context, request))
        # return HttpResponse('Waiting')