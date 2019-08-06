from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Expense(models.Model):
    type = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    userName = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "expense_info"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['post'] = Expense.objects.get(pk=self.kwargs['pk'])
        return context


    #def get_absolute_url(self):
     #   return reverse('expense_edit', kwargs={'pk': self.pk})

class Category(models.Model):
    userName = models.CharField(max_length=50, null=True)
    typeName = models.CharField(max_length=20)
    categoryName = models.CharField(max_length=50)

    class Meta:
        db_table = "category"
