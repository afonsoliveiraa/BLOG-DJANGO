from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.roles import assign_role, remove_role

from blog.admin import CustomUserCreationForm
from blog.forms import PostForm, CommentForm, TagForm
from blog.models import Post, Tag, Comment


# Create your views here.


def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()

            # Define a role do usuário como comum
            assign_role(user, 'usuario')

            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('login')

        else:
            print('invalid registration details')
    return render(request, "registration/register.html", {"form": form})


def index(request):
    # Lista de Post´s
    posts = Post.objects.all().order_by('-pk')

    # Último post
    ultimo = Post.objects.last()

    # Penúltimo
    pnt = 0
    if posts.count() >= 2:
        pnt = posts[1]

    # Paginação
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_page = paginator.get_page(page)

    # Variáveis
    context = {
        'ultimo': ultimo,
        'posts_page': posts_page,
        'pnt': pnt,
    }
    return render(request, 'blog/index.html', context)


# Variáveis globais, necessárias pois existem algumas instancias necessárias independente do template

def globais(request):
    # Posts´s
    posts = Post.objects.all().order_by('-pk')

    # Tag´s
    tags = Tag.objects.all()

    datas = []

    for post in posts:
        if post.date_create not in datas:
            datas.append(post.date_create)

    context = {
        'posts': posts,
        'tags': tags,
        'datas': datas,
    }
    return context


# Tudo sobre Post

@has_permission_decorator('criar_posts')
def post_page(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/post_page.html', context)


@has_permission_decorator('criar_posts')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = PostForm()
    contex = {
        'form': form,
    }
    return render(request, 'blog/post_page.html', contex)


@has_permission_decorator('criar_posts')
def post_edit(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


@has_permission_decorator('criar_posts')
def post_update(request, id):
    post = Post.objects.get(id=id)
    autor = post.author
    print(autor)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(index)


def post_detail(request, id):
    post = Post.objects.get(id=id)

    comments = Comment.objects.filter(post=id)

    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)


@has_permission_decorator('criar_posts')
def my_posts(request, user_id):
    usuario = User.objects.get(id=user_id)
    my_posts = Post.objects.filter(author=usuario)
    context = {
        'my_posts': my_posts,
    }
    return render(request, 'blog/my_posts.html', context)


# Criar comentário

@has_permission_decorator('comentar')
def comment_create(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/post_page.html', context)


# Buscas

def tag(request, tag):
    tag_obj = Tag.objects.get(name=tag)
    posts_tag = Post.objects.filter(tags=tag_obj)

    context = {
        'posts_tag': posts_tag,
    }
    return render(request, 'blog/tag.html', context)


def archive(request, data):
    posts_archive = Post.objects.filter(date_create=data)
    data_archive = data

    context = {
        'posts_archive': posts_archive,
        'data_archive': data_archive,
    }
    return render(request, 'blog/archive.html', context)


# Permissões

@has_role_decorator('dono')
def staff_page(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'blog/staff_page.html', context)


@has_role_decorator('dono')
def tornar_staff(request):
    usuario = request.POST.get('user')
    user_obj = User.objects.get(id=usuario)

    print(user_obj)

    assign_role(user_obj, 'staff')
    remove_role(user_obj, 'usuario')

    return redirect(index)


# Tag´s

def tag_page(request):
    form = TagForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/tag_page.html', context)


def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(tag_page)
