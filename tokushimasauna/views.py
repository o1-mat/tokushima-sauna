from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Spa, Category, Favorite, Review
from .forms import SearchForm, LoginForm, RegistrationForm, ReviewForm
from django.contrib.auth.decorators import login_required




class SpaListView(ListView):
    model = Spa
    template_name = 'spa_list.html'
    context_object_name = 'spas'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', '')
        category_id = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(address__icontains=query) |
                Q(category__name__icontains=query)
            )

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = SearchForm(self.request.GET)
        return context


class SpaDetailView(DetailView):
    model = Spa
    template_name = 'spa_detail.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'mypage')
            messages.success(request, "ログインしました")
            return redirect(next_url)
        else:
            messages.error(request, "ユーザー名またはパスワードが正しくありません")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "登録が完了しました！ログインしてください。")
            return redirect('login')
        else:
            messages.error(request, "入力内容にエラーがあります。")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})



@login_required
def mypage_view(request):
    return render(request, 'mypage.html', {'user': request.user})



@login_required
def favorite_view(request, pk):
    spa = get_object_or_404(Spa, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, spa=spa)
    if created:
        messages.success(request, "お気に入りに登録しました。")  # 成功メッセージ
    else:
        messages.warning(request, "この施設はすでにお気に入り登録されています。")  # 警告メッセージ
    return redirect('spa_detail', pk=spa.id)  # 詳細ページにリダイレクト

@login_required
def delete_favorite_view(request, pk):
    spa = get_object_or_404(Spa, pk=pk)
    favorite = Favorite.objects.filter(user=request.user, spa=spa)
    if favorite.exists():
        favorite.delete()
        messages.success(request, "お気に入りを解除しました。")  # 成功メッセージ
    else:
        messages.warning(request, "お気に入り登録されていません。")  # 警告メッセージ
    return render(request, 'mypage.html', {'user': request.user}) # 詳細ページにリダイレクト


@login_required
def review_view(request, pk):
    spa = get_object_or_404(Spa, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.spa = spa
            review.save()
            return redirect('spa_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'spa': spa})

@login_required
def edit_review_view(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('spa_detail', pk=review.spa.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review_view(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    spa_id = review.spa.id
    review.delete()
    return redirect('spa_detail', pk=spa_id)