from django.conf import settings
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        ## 이렇게 하면 html이 저장됩니다.
        # 지정한 언어(language)에 대한 분석기 (lexer)할당
        lexer = get_lexer_by_name(self.language)

        # 줄 표시 여부
        linenos = 'table' if self.linenos else False

        # self.title이 존재하면 options에 'title'키가 들어있는 dict를 전달
        options = {'title': self.title} if self.title else {}

        # 위에서 지정한 여러 변수를 사용해서 formatter객체 생성
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **options,
        )


        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
