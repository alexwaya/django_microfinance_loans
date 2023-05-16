from django.contrib.auth.models import User
from django.db import models
from dateutil.relativedelta import relativedelta
from pages.models import CustomUser


STATUS = (
    ("Pending","Pending"),
    ("Approved","Approve"),
    ("Declined","Decline"),
)


class Loans(models.Model):
    loan_title = models.CharField(max_length=255)
    loan_description = models.TextField()

    interest = models.IntegerField()
    thumbnail = models.ImageField(upload_to ='uploads/')

    created_by = models.ForeignKey(CustomUser, related_name='loans', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_title


class Application(models.Model):
    loan = models.ForeignKey(Loans, related_name='applications', on_delete=models.CASCADE)

    #apply_reason = models.TextField()

    amount_applied = models.DecimalField(max_digits=10, decimal_places=2)
    period_applied = models.IntegerField(default=1)
    total_applied = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    status = models.CharField(choices=STATUS, max_length=50, default='Pending')

    created_by = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loan.loan_title
    
    # def due_date(self):
    #     return self.objects.all() + relativedelta(months=self.period_applied)

    @property
    def cal_date(self):
        return self.created_at.date() + relativedelta(months=+self.period_applied)


