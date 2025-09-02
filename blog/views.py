from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post

# Homepage view – shows all posts
def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Post detail view – used if you ever link to full post pages
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/post_detail.html', {'post': post})

# View tracker – triggered by JavaScript when a post is expanded
@csrf_exempt
def track_view(request, pk):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=pk)
            post.views += 1
            post.save(update_fields=['views'])
            return JsonResponse({'status': 'ok'})
        except Post.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Post not found'}, status=404)