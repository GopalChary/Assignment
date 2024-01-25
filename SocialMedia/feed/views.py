
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Comment

@login_required
def feed(request):
    messages = Message.objects.all()
    return render(request, 'feed/feed.html', {'messages': messages})

@login_required
def post_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        Message.objects.create(user=request.user, text=text)
    return redirect('feed:feed')

@login_required
def post_comment(request, message_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        message = Message.objects.get(pk=message_id)
        Comment.objects.create(user=request.user, message=message, text=text)
    return redirect('feed:feed')

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    if message.user == request.user:
        message.delete()
    return redirect('feed:feed')

@login_required
def like_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.likes.add(request.user)
    return redirect('feed:feed')

@login_required
def like_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.likes.add(request.user)
    return redirect('feed:feed')
