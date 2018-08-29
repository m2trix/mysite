from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.urls import reverse

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    # ���ݼ��
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message':'�û�δ��¼', 'redirect_to': referer})

    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'message':'��������Ϊ��', 'redirect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except expression as e:
        return render(request, 'error.html', {'message':'���۶��󲻴���', 'redirect_to': referer})
    
    # ���ͨ������������
    comment = Comment()
    comment.user = request.user
    comment.text = text
    # Blog.objects.get(pk=object_id)
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)