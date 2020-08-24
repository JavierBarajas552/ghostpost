from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import PostModle
from homepage.forms import PostForm
# Create your views here.


def index(request):
    all_post = PostModle.objects.order_by('-post_time').all()
    return render(request, 'index.html', {'posts': all_post})


def votes(request):
    all_post = PostModle.objects.extra(
        select={'score': 'upvotes - downvotes'}).extra(order_by=['-score'])
    return render(request, 'index.html', {'posts': all_post})


def boasts(request):
    all_post = PostModle.objects.filter(is_roast__exact='False').all()
    return render(request, 'index.html', {'posts': all_post})


def roasts(request):
    all_post = PostModle.objects.filter(is_roast__exact='True').all()
    return render(request, 'index.html', {'posts': all_post})


def upvote(request, post_id):
    post = PostModle.objects.filter(id=post_id).first()
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, post_id):
    post = PostModle.objects.filter(id=post_id).first()
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            is_roast = False
            if data.get('post_type') == "2":
                is_roast = True
            PostModle.objects.create(
                body=data.get('body'),
                is_roast=is_roast
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = PostForm()
    return render(request, "generic_form.html", {'form': form})
