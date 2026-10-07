from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def post_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)

    # HW-9 / 1: post səhifəsi hər açılanda baxış sayını bazada artır.
    post.views += 1
    post.save(update_fields=["views"])

    return render(request, "blog/post_detail.html", {"post": post})


def about(request):
    return render(request, "blog/about.html")


def category_list(request):
    categories = Category.objects.all()
    return render(request, "blog/category_list.html", {"categories": categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=slug, is_published=True)
    context = {"category": category, "posts": posts}
    return render(request, "blog/category_detail.html", context)


def contact(request):
    return render(request, "blog/contact.html")


def author_posts(request, name):
    # HW-9 / 2: yalnız həmin müəllifin dərc olunmuş postları.
    posts = Post.objects.filter(author=name, is_published=True)
    return render(request, "blog/author_posts.html", {"name": name, "posts": posts})


def latest(request):
    # HW-9 / 3: ən yeni 3 dərc olunmuş post, yenidən köhnəyə.
    posts = Post.objects.filter(is_published=True).order_by("-created_at")[:3]
    return render(request, "blog/latest.html", {"posts": posts})


def stats(request):
    # HW-9 / 4: statistika tam bazadan hesablanır.
    published_posts = Post.objects.filter(is_published=True)
    top_post = published_posts.order_by("-views").first()

    context = {
        "post_count": published_posts.count(),
        "category_count": Category.objects.count(),
        "top_post": top_post,
    }
    return render(request, "blog/stats.html", context)
