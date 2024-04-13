from django.shortcuts import render, redirect
from .models import *
from .forms import *
from head.models import *
import datetime


def chats(request, pk):
    account = Profile.objects.get(user__pk=pk)
    if request.user != account.user:
        return render(request, 'error.html')
    all_my_companions = []
    my_data = Message.objects.filter(user=account.user)
    for data in my_data:
        if data.companion in all_my_companions:
            pass
        else:
            all_my_companions.append(data.companion)
    
    i_comp_data = Message.objects.filter(companion=account)
    i_comp_profs = []
    for data in i_comp_data:
        if data.user.profile in i_comp_profs:
            pass
        else:
            i_comp_profs += [data.user.profile]

    def etc(x):
        if len(x)>=37:
            return x[:38]+'...'
        elif 1<=len(x)<=36:
            return x
        

    all_companions = list(set(all_my_companions + i_comp_profs))
    last_dates = []
    last_messages = []
    for companion in all_companions:
        obj0 = my_data.filter(companion=companion).last()
        my_last_message_date = obj0.date if obj0 else datetime.datetime(2022, 1, 2, tzinfo=datetime.timezone.utc)
        obj1 = i_comp_data.filter(user=companion.user).last()
        comp_last_message_date = obj1.date if obj1 else datetime.datetime(2022, 1, 2, tzinfo=datetime.timezone.utc)
        last_dates.append([my_last_message_date, comp_last_message_date])
        obj2 = my_data.filter(companion=companion).last()
        my_last_message = etc(obj2.message) if obj2 else None
        obj3 = i_comp_data.filter(user=companion.user).last()
        comp_last_message = etc(obj3.message) if obj3 else None
        last_messages.append([my_last_message, comp_last_message])
    

    chats_data_unsort = list(zip(all_companions, last_dates, last_messages))
    chats_data = sorted(chats_data_unsort, key=lambda chat_data: max(chat_data[1]))[::-1]
    
    return render(request, 'companions.html', {'chats_data': chats_data, 'all_companions': all_companions, 'account': account}) 

def chat(request, pk):
    companion_pk = Profile.objects.get(pk=pk)
    if companion_pk == request.user.profile:
        return render(request, 'error.html')
    
    account = Profile.objects.get(user__username=request.user.username)
    
    form = MessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(commit=False)
        Message.objects.create(user=request.user, message=form.data['message'], companion=companion_pk)
        return redirect('messenger:chat', pk=pk)
    chat_my_data = Message.objects.filter(user=request.user, companion__pk=pk)
    chat_companion_data = Message.objects.filter(user=companion_pk.user, companion=account)
    chat_data=chat_my_data.union(chat_companion_data).order_by('date')
    return render(request, 'messages.html', {'chat_data': chat_data, 'companion': companion_pk, 'form': form, 'account': account})

def delete_message(request, id):
    action = request.GET.get('action')
    account = Profile.objects.get(user__username=request.user.username)
    
    if action == 'delete':
        Message.objects.get(user=account.user, id=id).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'messages.html', {}) 