from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='名称')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')

    def __str__(self):
        return self.name

class Spa(models.Model):
    name = models.CharField(max_length=200, verbose_name='施設名')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='カテゴリ')
    homepage = models.URLField(blank=True, null=True, verbose_name='ホームページURL')
    img = models.ImageField( 
        upload_to='media/',  # Cloudinary内で保存されるフォルダ名
        blank=True,
        default='https://res.cloudinary.com/dd13xessz/image/upload/v1734362457/noImage_gos7nw.png',  # Cloudinary内に配置するデフォルト画像
        verbose_name='画像'
    )
    detail = models.TextField(blank=True, null=True, verbose_name='詳細')
    catchphrase = models.TextField(blank=True, null=True, verbose_name='キャッチフレーズ')
    address = models.CharField(max_length=200, verbose_name='住所')
    tel = models.CharField(max_length=20, verbose_name='電話番号')
    price = models.PositiveIntegerField(verbose_name="料金設定", default=0)
    holiday = models.CharField(max_length=50, blank=True, null=True, verbose_name='定休日')
    operating_hours = models.CharField(null=True, blank=True, max_length=100, verbose_name='営業時間')
    created_at = models.DateTimeField(auto_now_add=True, max_length=50, verbose_name='作成日')
    favorited_by = models.ManyToManyField(User, related_name='favorites', blank=True, verbose_name='お気に入り')
    
    def __str__(self):
        return self.name 


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    spa = models.ForeignKey(Spa, on_delete=models.CASCADE, related_name='spa_favorites')

    class Meta:
        unique_together = ('user', 'spa')  # ユーザーごとに同じ施設を一度だけお気に入り登録可

    def __str__(self):
        return f"{self.user.username} - {self.spa.name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    spa = models.ForeignKey(Spa, on_delete=models.CASCADE, verbose_name="施設")
    star = models.IntegerField(verbose_name="評価", choices=[(i, i) for i in range(1, 6)])
    content = models.TextField(verbose_name="レビュー内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return f"{self.user.username} - {self.spa.name} - {self.star} stars"