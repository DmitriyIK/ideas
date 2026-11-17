from django.db import models


class Idea(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("published", "Опубликована"),
        ("rejected", "Отклонена"),
    ]

    # Данные автора
    fio = models.CharField("ФИО", max_length=200)
    group = models.CharField("Группа", max_length=50)
    course = models.CharField("Курс", max_length=50)
    direction = models.CharField("Направление обучения", max_length=200)
    phone = models.CharField("Телефон", max_length=30)
    email = models.EmailField("Почта")
    telegram = models.CharField("Telegram", max_length=100)

    # Содержание заявки
    idea_brief = models.TextField("Краткое описание идеи (1–3 предложения)")
    problem = models.TextField("Какую проблему (боль клиента) решает")
    audience = models.TextField("Для какого потребителя продукт")
    feasible = models.TextField("Реализуема ли сейчас, если нет — что мешает")
    competitors = models.TextField("Конкуренты и чем вы лучше")
    ready_to_work = models.BooleanField("Готовы работать над идеей")
    need_team = models.BooleanField(
        "Нужна ли команда (помощники, наставники)", default=False
    )
    allow_publish = models.BooleanField(
        "Разрешаю опубликовать краткое описание идеи на сайте", default=False
    )

    # Служебные поля
    status = models.CharField(
        "Статус модерации", max_length=20,
        choices=STATUS_CHOICES, default="new",
    )
    created_at = models.DateTimeField("Дата заявки", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.fio} — {self.idea_brief[:60]}"
