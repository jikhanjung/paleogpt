from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the chat index.")

def get_user_obj( request ):
    user_obj = request.user
    #print(user_obj)
    if str(user_obj) == 'AnonymousUser' or not user_obj.is_approved:
        return None
    #print("user_obj:", user_obj)
    user_obj.groupname_list = []
    for g in request.user.groups.all():
        user_obj.groupname_list.append(g.name)

    return user_obj

def check_admin(user_obj):
    if 'Administrators' in user_obj.groupname_list:
        #print(user_obj.username)
        return True
    else:
        return False

def chat_index(request):
    user_obj = get_user_obj( request )
    #print(user_obj)

    context = {
        'user_obj': user_obj, 
        #'ask_redirection': ask_redirection,
        #'last_edit_finbox_url': last_edit_finbox_url,
    }
    return render(request, 'chat/chat_index.html', context)
