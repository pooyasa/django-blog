from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def index(request):
    current_user = request.user
    print(current_user.id)
    posts = Post.objects.filter(published_at__lte = timezone.now())
    return render(request, "blog/index.html", {"posts": posts, "current_user": request.user})