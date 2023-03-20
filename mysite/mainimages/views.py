from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView

from .forms import CommentForm, CreatePostForm, CreateGroupForm, SaveToGroupForm
from .models import Post, Comment, GroupsPosts
from players.models import CustomUser

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'delete-post.html'

# def home1(request):
#     post = Post.objects.all().order_by('-created_at')
#
#     numbers_list = range(1, 1000)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(numbers_list, 20)
#     try:
#         numbers = paginator.page(page)
#     except PageNotAnInteger:
#         numbers = paginator.page(1)
#     except EmptyPage:
#         numbers = paginator.page(paginator.num_pages)
#     return render(request, 'home.html', {'numbers': numbers, 'post': post})


# Вывод постов на главной странице/вывод постов по поисковому запросу(по категории)
def posts(request):
    search_query = request.GET.get('q', '')
    if search_query:
        post = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(categorys__categories__contains=search_query)
        ).order_by('-created_at')
    else:
        post = Post.objects.all().order_by('-created_at')[:20]

    context = {
        "post": post,
        'title': 'NNCImages',
    }
    return render(request, "main_page1.html", context)


# def post_selection(request, pk):
#     post_one = Post.objects.get(pk=pk)
#
#     comments = post_one.comment1.order_by('-created_date')
#
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post_one
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'post_one': post_one,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#
#     return render(request, "post_selection.html", context)

# получение и вывод конкретного поста по pk, форма комментариев с возможностью добавления
def post_selection(request, pk):
    posts = Post.objects.filter(user_id=1).count
    post_one = get_object_or_404(Post, pk=pk)
    comments = post_one.comment1.order_by('-created_date')
    comment_form = CommentForm()
    user = request.user

    group = GroupsPosts.objects.filter(user=request.user).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = user
            new_comment.post = post_one
            new_comment.save()
            return redirect('post_selection', post_one.pk)
    else:
        comment_form = CommentForm()

    context = {
        'post_one': post_one,
        'comments': comments,
        'comment_form': comment_form,
        'posts': posts,
        'group': group,
    }

    return render(request, "post_selection.html", context)


def save_post_to_group(request, pk):
    post_one = get_object_or_404(Post, pk=pk)
    groups = GroupsPosts.objects.filter(user=request.user)[1]
    user = request.user

    if request.method == "POST":
        form = SaveToGroupForm(data=request.POST)
        if form.is_valid():
            form_new = form.save(commit=False)
            form_new.user = user
            form_new.groupposts = groups
            form_new.save()
    else:
        form = SaveToGroupForm()

    context = {
        'post_one': post_one,
        'groups': groups,
        'form': form
    }
    return render(request, "save_to_group.html", context)


# @login_required
# def save_to_group(request, pk):
#     post_one = get_object_or_404(Post, pk=pk)
#     user = request.user
#
#     if request.method == 'POST':
#         form = SaveToGroupForm(request.user, request.POST, instance=post_one)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = pin.user
#             instance.save()
#             board = GroupsPosts.objects.filter(id=request.POST.get('board')).first()
#             board.pins.add(pin)
#     return redirect(request.META.get('HTTP_REFERER'))


# def delete_post(request, id):
#     # post_del = get_object_or_404(Post, pk=pk)
#     post_del = Post.objects.filter(id=id)
#     post_del.delete()
#     return redirect('/')

    # return render(request, 'post_selection.html', {'post_del': post_del})

# def deleted_post()
# def create_post(request):
#
#     user = request.user
#
#     if request.method == "POST":
#         form_createpost = CreatePostForm(data=request.POST)
#         if form_createpost.is_valid():
#             new_post = form_createpost.save(commit=False)
#             new_post.user = user
#             new_post.save()
#             img_obj = new_post.instance
#             return render(request, 'create_post.html', {'form': form_createpost, 'img_obj': img_obj})
#     else:
#         form_createpost = CreatePostForm()
#
#     context = {
#         'title': 'Create post',
#         'form': form_createpost,
#     }
#
#     return render(request, 'create_post.html', context)


@login_required
def create_post(request):
    """Process images uploaded by users"""
    # user_creator =
    user = request.user
    if request.method == 'POST':
        form_post = CreatePostForm(request.POST, request.FILES)
        if form_post.is_valid():
            new_post = form_post.save(commit=False)
            new_post.user = user
            new_post.save()
            form_post.save_m2m()
            # Get the current instance object to display in the template
            # img_obj = form_post.instance
            # return render(request, 'create_post.html', {'form': form_post, 'img_obj': img_obj})
            return redirect('/')
    else:
        form_post = CreatePostForm()

    context = {
        'form': form_post,
    }
    return render(request, 'create_post.html', context)


# def messag(request):
#     if request.method == "POST":
#         id = request.POST.get('id', None)
#         if id:
#             try:
#                 post1 = Post.objects.get(pk=id)
#             except ObjectDoesNotExist:
#                 return ()
#             form1 = CommentFormReg(request.POST)
#             if form1.is_valid():
#                 form1 = form1.save(commit=False)
#                 form1.user = request.user
#                 form1.post = post1
#                 form1.save()
#                 return ()
#             return ()
#         return ()
#
#     context = {
#         'form1': CommentFormReg(),
#         'comments1': Comment.object.all()
#     }
#     return render(request, "post_selection.html", context)


# @login_required
# def create_groups(request):
#     if request.method == 'POST':
#         form = CreateGroupForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             check_name = request.user.group_user.filter(
#                 title=instance.title
#             ).first()
#             if not check_name:
#                 instance.save()
#             return redirect('postes')


@login_required
def home_page(request):
    posts_created = Post.objects.all()

    user = request.user

    if request.method == 'POST':
        form = CreateGroupForm(request.POST, request.FILES)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.user = user
            new_group.save()
            form.save_m2m()
            return redirect('home_page_create')
    else:
        form = CreateGroupForm()

    context = {
        'form': form,
        'posts_created': posts_created,
    }
    return render(request, 'home_page.html', context)


@login_required
def my_posts(request):
    """ Показывает пользователю загруженные им посты """
    my_post = Post.objects.filter(user=request.user)
    context = {
        'my_post': my_post,
    }
    return render(request, "my_posts.html", context)


@login_required
def home_page_create(request):
    group = GroupsPosts.objects.filter(user=request.user).order_by('-id')

    context = {
        'group': group,
        # 'postgroup': postgroup,
    }
    return render(request, 'home_page_create.html', context)


def open_group(request, title):
    # postes = GroupsPosts.objects.filter(user=request.user)
    # postes = GroupsPosts.objects.filter()
    postes = get_object_or_404(GroupsPosts, title=title)
    context = {
        'posts': postes,
    }

    return render(request, 'open_group.html', context)