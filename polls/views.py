from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader
from .models import Question, Choice


# Create your views here.
# def index(request):
#     latest_ques_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {"latest_ques_list": latest_ques_list}
#     # output = ", ".join([q.question_text for q in latest_ques_list])
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_ques_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_ques_list": latest_ques_list}
    return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     try:
#         q = Question.objects.get(pk=id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question":q})

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":q})

def results(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": ques})

def vote(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = ques.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":ques,
                "error_message": "You didn't select a choice."
            }

        )
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(ques.id,)))