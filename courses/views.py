from .models import Course, Lesson, Comments
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserAddCourse, AddComment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import Http404

import logging


logger = logging.getLogger(__name__)


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Main page'
        return ctx


def tariffsPage(request):
    return render(request, 'courses/tariffs.html', {'title': 'Site rates'})


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        ctx['comment_form'] = AddComment()
        ctx['comments'] = Comments.objects.filter(course_exactly=self.get_object())
        return ctx

    def post(self, request, *args, **kwargs):
        form = AddComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.course_exactly = self.get_object()
            new_comment.save()
            messages.success(request, 'Your comment was successfully added.')
        return redirect(self.get_object().get_absolute_url())


class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'courses/comment-delete.html'

    def get_success_url(self):
        course_slug = self.object.course_exactly.slug  # Получаем slug курса из комментария
        return reverse('course-detail', kwargs={'slug': course_slug})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        logger.info(f"Author of the comment: {self.object.author}")  # Debugging line
        logger.info(f"Current user: {request.user}")  # Debugging line

        if self.object.author == request.user:
            messages.success(request, 'Comment deleted successfully')
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, 'You do not have permission to delete this comment')
            return redirect(self.get_success_url())

    def get_object(self):
        course_id = self.kwargs.get("course_id")
        pk = self.kwargs.get("pk")
        comment = get_object_or_404(Comments, id=pk, course_exactly_id=course_id)

        if comment.author != self.request.user:
            raise Http404("You do not have permission to delete this comment")

        return comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_slug'] = self.object.course_exactly.slug
        return context


class AddCourse(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/add-course.html'
    form_class = UserAddCourse

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        current_user = request.user
        user_status = current_user.profile.user_status
        if user_status == 'Redaction':
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.warning(request, 'You do not have permission to add courses.')
            return HttpResponseRedirect(reverse('home'))


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lessons-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split("=")[1].split("&")[0]
        return ctx