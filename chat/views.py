from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .ZWrapper import ZWrapper
from .models import CollectionCache, ItemCache, CollectionItemRel, LastVersion
import json
import requests

# disable ssl warning
requests.packages.urllib3.disable_warnings()

# override the methods which you use
requests.post = lambda url, **kwargs: requests.request(
    method="POST", url=url, verify=False, **kwargs
)

requests.get = lambda url, **kwargs: requests.request(
    method="GET", url=url, verify=False, **kwargs
)

# Create your views here.
def index(request):
    return HttpResponseRedirect('/chat/chat_index')

def get_user_obj( request ):
    user_obj = request.user
    #print(user_obj)
    if str(user_obj) == 'AnonymousUser': #or not user_obj.is_approved:
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
    if user_obj is None:
        return render(request, 'chat/chat_index.html', {'user_obj': user_obj})
    zotero_user_id = user_obj.zotero_user_id
    #print("zotero user id:", zotero_user_id, 'username:', user_obj.username)
    #zotero_api_key = user_obj.zotero_api_key
    #z = ZWrapper(zotero_user_id, zotero_api_key)
    collection_list = CollectionCache.objects.filter(zotero_user_id=zotero_user_id)



    context = {
        'user_obj': user_obj, 
        'collection_list': collection_list,
        #'ask_redirection': ask_redirection,
        #'last_edit_finbox_url': last_edit_finbox_url,
    }
    return render(request, 'chat/chat_index.html', context)

def collection_tree(request):
    # read collection list from database
    user_obj = get_user_obj( request )
    zotero_user_id = user_obj.zotero_user_id

    collection_list = []
    for collection in CollectionCache.objects.filter(zotero_user_id=zotero_user_id):
        collection_list.append({'key': collection.key, 'parent_key': collection.parent_id, 'name': json.loads(collection.data)['name'], 'children': []})
    # sort collection list by its name
    collection_list.sort(key=lambda x: x['name'])
    
    collection_tree = {'key': 'root', 'parent_key': None, 'name': 'root', 'children': []}
    for collection in collection_list:
        if collection['parent_key'] is None:
            collection_tree['children'].append(collection)
        else:
            for col in collection_list:
                if col['key'] == collection['parent_key']:
                    col['children'].append(collection)
            #collection_list[collection['parent_key']]['children'].append(collection)

    return JsonResponse(collection_tree)

def item_list(request, colkey):
    user_obj = get_user_obj( request )
    zotero_user_id = user_obj.zotero_user_id
    # get items from database using CollectionItemRel
    item_list = []
    for itemrel in CollectionItemRel.objects.filter(collection__key=colkey,zotero_user_id=zotero_user_id):
        #print(itemrel)
        data = json.loads(itemrel.item.data)
        item_list.append({'key': itemrel.item.key, 'parent_key': itemrel.item.parent_id, 'name': data['title'], 'itemType': data['itemType'], 'children': []})
        if 'contentType' in data:
            item_list[-1]['contentType'] = data['contentType']

    item_tree = {'key': 'root', 'parent_key': None, 'name': 'root', 'children': []}
    for item in item_list:        
        if item['parent_key'] is None:
            item_tree['children'].append(item)
        else:
            for item2 in item_list:
                if item2['key'] == item['parent_key']:
                    item2['children'].append(item)
    return JsonResponse(item_tree)