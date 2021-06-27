from datetime import datetime
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm
from .models import Transaction, Store



@login_required(login_url='/api-auth/login')
def home(request):
    return HttpResponseRedirect('/transactions/upload', {'messages': messages})

@login_required(login_url='/api-auth/login')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/api-auth/login')
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = request.FILES['file']
            messages = cnab_upload_file(request, upload)
            return HttpResponseRedirect('/transactions/upload', {'messages': messages})
    else:
        form = UploadFileForm()
        return render(request, 'transactions/upload_CNAB.html', {'form': form})

def cnab_upload_file(request, upload):
    content = upload.read().decode("utf-8")
    content = content.splitlines()
    counter = 0
    for line in content:
        try:
            transaction_dict = {}
            store_dict = {}
            transaction_dict['type'] = line[0]
            transaction_dict['date'] = datetime.strptime(line[1:9] + ' ' + line[42:48], '%Y%m%d %H%M%S')
            transaction_dict['value'] = str(int(line[9:19])/10)
            transaction_dict['cpf'] = line[19:30]
            transaction_dict['card'] = line[30:42]
            store_dict['owner'] = line[48:62]
            store_dict['nome'] = line[62:81]
            store, created = Store.objects.get_or_create(**store_dict)
            transaction_dict['store'] = store
            Transaction.objects.create(**transaction_dict)
            counter += 1
        except Exception as err:
            messages.error(request, ('{} na linha {}').format(type(err).__name__, line))
    messages.success(request, ('{} Transações importadas').format(counter))
    return messages

@login_required(login_url='/api-auth/login')
def list(request):
    return render(request, 'transactions/list.html')