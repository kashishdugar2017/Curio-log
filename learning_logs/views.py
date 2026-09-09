from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import Http404


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, topic_id, entry_id):
    """Edit an existing entry."""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entry = topic.entry_set.get(id=entry_id)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)