from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import RoomPost, Comment
from .forms import CommentForm, RoomPostForm



def home_view(request):
    """ Return the home page view """
    return render(request, 'room/index.html')


class PostList(generic.ListView):
    """
    Display the rooms post in list on index page
    """
    queryset = RoomPost.objects.all()
    template_name = "room/browseRental.html"
    paginate_by = 3

def post_detail(request):
    """
    Display the blog in detail when click on the title or text below the title.
    """
    queryset = RoomPost.objects.all()
    post = get_object_or_404(queryset)
    comment = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and waiting for approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {"post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form, },
        )


def comment_edit(request, comment_id):
    """
    Edit the single comment which have already submitted.
    """
    if request.method == "POST":
        queryset = Post.objects.all()
        post = get_object_or_404(queryset)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment has beed Updated!')
        else:
            messages.add_message(
                    request, messages.ERROR, 'Error Updating Comments')

    return HttpResponseRedirect(reverse('post_detail'))


def comment_delete(request, slug, comment_id):
    """
    Delete the single Comment from Comment List
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment has deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse("post_detail"))


def post_room(request):
    if request.method == 'POST':
        form = RoomPostForm(request.POST, request.FILES)
        if form.is_valid():
            room_post = form.save(commit=False)
            room_post.post_user = request.user
            room_post.save()           
            return redirect('post_detail')
    else:
        form = RoomPostForm()

    return render(request, 'room/post_room.html', {'form': form})