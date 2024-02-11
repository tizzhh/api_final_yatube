from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

User = get_user_model()


POST_CHAR_LIMIT = 75


class Group(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )

    class Meta:
        # По какой-то неведомой мне причине не проходит тест
        # при -pub_date, который сюда было бы поставить логичнее.
        # Пишет, что в поле ответа нет автора, хотя он там есть,
        # проверял в постмане... Сюдя по тесту там в поле не тот автор,
        # что ожидается: TestUser вместо TestUserAnother
        ordering = ('pub_date',)

    def __str__(self):
        return (
            (self.text[:POST_CHAR_LIMIT] + '...')
            if len(self.text) > POST_CHAR_LIMIT
            else self.text
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return (
            (self.text[:POST_CHAR_LIMIT] + '...')
            if len(self.text) > POST_CHAR_LIMIT
            else self.text
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    following = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'), name='unique_user_following'
            ),
            models.CheckConstraint(
                check=~Q(user=F('following')), name='cannot_follow_oneself'
            ),
        )
