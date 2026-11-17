from django.db.models import Count
from django.shortcuts import redirect, render

from .forms import IdeaForm
from .models import Idea


def submit_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")
    else:
        form = IdeaForm()
    return render(request, "ideas/form.html", {"form": form})


def thanks(request):
    return render(request, "ideas/thanks.html")


def published_ideas(request):
    # Публично показываем только заявки, у которых автор разрешил
    # публикацию И модератор поставил статус "Опубликована".
    ideas = Idea.objects.filter(status="published", allow_publish=True)
    return render(request, "ideas/published.html", {"ideas": ideas})


def stats(request):
    total = Idea.objects.count()
    published = Idea.objects.filter(status="published").count()
    by_direction = (
        Idea.objects.values("direction").annotate(n=Count("id")).order_by("-n")
    )
    by_course = Idea.objects.values("course").annotate(n=Count("id")).order_by("course")
    return render(
        request,
        "ideas/stats.html",
        {
            "total": total,
            "published": published,
            "by_direction": by_direction,
            "by_course": by_course,
        },
    )
