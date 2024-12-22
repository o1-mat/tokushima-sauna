from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Category, Review

class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='キーワード検索',
        widget=forms.TextInput(attrs={
            'placeholder': '名前、住所で検索',
            'class': 'form-control',
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='カテゴリ検索',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="ユーザー名",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名を入力してください。'})
    )
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワードを入力してください。(8文字以上)'})
    )

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            # ユーザー名
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ユーザー名を入力してください。'
            }),
            # メールアドレス
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '例: example@example.com'
            }),
            # パスワード1: 
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'パスワードを入力してください。(8文字以上)'
            }),
            # パスワード2: パスワード1と一致するか確認
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '確認用のパスワードをもう一度入力してください。'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  # ヘルプテキストを削除
            field.error_messages = {}  # エラーメッセージを削除

        


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star', 'content']
        widgets = {
            'star': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'star': '評価 (星1〜5)',
            'content': 'レビュー内容',
        }



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名を入力してください。'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '例: example@example.com'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="現在のパスワード",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '現在のパスワードを入力してください。'}),
    )
    new_password1 = forms.CharField(
        label="新しいパスワード",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '新しいパスワードを入力してください。(8文字以上)'}),
    )
    new_password2 = forms.CharField(
        label="新しいパスワード (確認用)",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '確認用のパスワードをもう一度入力してください。'}),
    )