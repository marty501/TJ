from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from tjapp.templates.tjapp.post.forms import EmailPostForm
from tjapp.templates.tjapp.journey.forms import JourneyAddForm
from .models import Journey
from django.core.mail import send_mail


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form passed validation
            cd = form.cleaned_data  # dictionary of form fields and their values (VALID ones)
            # .... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) wants to notify you that there is a delay at "{}"'.format(cd['name'], cd['email'],
                                                                                         post.title)
            message = 'Delay status at: "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'],
                                                                                 cd['comments'])
            send_mail(subject, message, 'martyraychev@gmail.com', [cd['to']])

            # Get the recipient email
            recipient = cd['to']
            sent = True
    else:
        form = EmailPostForm()
        recipient = False
        return render(request, 'tjapp/post/share.html',
                      {
                          'post': post,
                          'form': form,
                          'sent': sent,
                          'recipient': recipient}
                      )


# Create your views here.
def post_list(request):  # request required for all views
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page not an INT - deliver Page 1
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'tjapp/post/list.html',
                  {'page': page, 'posts': posts})  # render the post with the given template


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'tjapp/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'tjapp/post/detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'tjapp/post/post_edit.html', {'form': form})
