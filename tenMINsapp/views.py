from django.shortcuts import render,redirect, HttpResponse
from tenMINsapp.models import Article,Comment,Ticket,UserProfile
from tenMINsapp.forms import CommentForm,LoginForm,MyinfoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def index_login(request):
    # 登陆
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm()
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='index')
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(username=username, password=password)
            # if user:
            #     login(request, user)
            #     return redirect(to='index')
        # else:
        #     return HttpResponse('<h1>NOT A USER !</h1>')
    context['form'] = form
    return render(request, 'register.html', context)

def index_register(request):
    # 注册
    context = {}
    if request.method == 'GET':
        form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            form.save()
            user = User.objects.get(username = username)
            user_profile,status = UserProfile.objects.get_or_create(belong_to=user)
            print('8'*60, user_profile, type(user_profile), '8'*60)
            user_profile.save()
            return redirect(to='index_login')
    context['form'] = form
    return render(request, 'register.html', context)

def index(request, cate=None):
    context = {}
    if cate == 'all':
        article_list = Article.objects.filter(all_choice=True)
    elif cate == 'new':
        article_list = Article.objects.filter(new_choice=True)
    elif cate == 'editors':
        article_list = Article.objects.filter(editors_choice=True)
    elif cate is None:
        article_list = Article.objects.all()

    page_robot = Paginator(article_list, 9)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    context['article_list'] = article_list
    return render(request,'index.html',context)


# def detail(request,page_num):
#     if request.method == 'GET':
#         form = CommentForm  # 创建表单
#     if request.method == 'POST':
#         form = CommentForm(request.POST)    # 绑定表单
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             content = form.cleaned_data['content']
#             article = Article.objects.get(id=page_num)
#             c = Comment(name=name, content=content,belong_to=article)
#             c.save()
#             return redirect(to='detail',page_num=page_num)
#     context = {}
#     article = Article.objects.get(id=page_num)
#     best_comment = Comment.objects.filter(best_comment=True,belong_to=article)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     # comment_list = Comment.objects.all()
#     context['article'] = article
#     # context['comment_list'] = comment_list
#     context['form'] = form
#     return render(request,'detail.html',context)


def detail(request, page_num, error_form=None):
    context = {}
    like_counts = Ticket.objects.filter(choice='like', article_id=page_num).count()
    dislike_counts = Ticket.objects.filter(choice='dislike', article_id=page_num).count()
    try:
        voter_id = request.user.profile.id
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=page_num)
        context['user_ticket'] = user_ticket_for_this_article
    except:
        pass
    # context['article_info'] = article_info
    form = CommentForm  # 创建表单
    article = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    elif error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    context['page_num'] = page_num
    context['article'] = article
    context['like_counts'] = like_counts
    context['dislike_counts'] = dislike_counts
    return render(request,'detail.html',context)


def detail_comment(request,page_num):
    form = CommentForm(request.POST)    # 绑定表单
    if form.is_valid():
        name = form.cleaned_data['name']
        content = form.cleaned_data['content']
        article = Article.objects.get(id=page_num)
        c = Comment(name=name, content=content,belong_to=article)
        c.save()
    else:
        return detail(request,page_num,error_form=form)
    return redirect(to='detail',page_num=page_num)


def detail_vote(request, page_num):
    if not isinstance(request.user, User):
        return redirect(to="detail", page_num=page_num)
    voter_id = request.user.profile.id
    try:
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=page_num)
        user_ticket_for_this_article.choice = request.POST['vote']
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=page_num, choice=request.POST['vote'])
        new_ticket.save()
    return redirect(to='detail',page_num=page_num)


def myinfo(request):
    if not isinstance(request.user, User):
        return redirect(to='index')
    context = {}
    profile = UserProfile.objects.all
    if request.method == 'GET':
        form = MyinfoForm
    elif request.method == 'POST':
        form = MyinfoForm(request.POST, request.FILES)
        print(form,'*'*80)
        print(form.errors, '='*80)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            profile_image = form.cleaned_data['image']
            user_sex = form.cleaned_data['sex']
            user = User.objects.get(username=request.user.username)
            User(username=username, password=password).save()
            # c.save()
            UserProfile(profile_image=profile_image, user_sex=user_sex, belong_to=user).save()
            # d.save()
            return redirect(to=myinfo)
    context['profile'] = profile
    context['form'] = form
    return render(request, 'myinfo.html', context)


def mycollection(request):
    context = {}
    if not isinstance(request.user, User):
        return redirect(to='index')
    voter = request.user.profile.id
    tickets = Ticket.objects.filter(voter=voter, choice='like') # 通过票对象的article字段，里面就可以获取到文章对象，然后去数据就可以了
    page_robot = Paginator(tickets, 3)
    page_num = request.GET.get('page')
    try:
        tickets = page_robot.page(page_num)
    except EmptyPage:
        tickets = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        tickets = page_robot.page(1)
    context['tickets'] = tickets
    return render(request, 'mycollection.html', context)






