from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType

def blog_list(request):
    # localhost:8000/blog?page=[page_num]
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 10) # 每 10 个元素进行分页
    page_num = request.GET.get('page', 1) # 获取 URL 的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context)

def blog_with_type(request, blog_type_pk):
    context = {}
    type_name = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=type_name)
    context['type_name'] = type_name
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_with_type.html', context)