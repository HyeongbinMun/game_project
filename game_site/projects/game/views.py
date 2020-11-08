from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'game/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'game/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('game:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'game/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('game:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'game/question_form.html', context)