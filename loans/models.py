from django.contrib.auth.models import User
from django.db import models

class Loans(models.Model):
    loan_title = models.CharField(max_length=255)
    loan_description = models.TextField()

    created_by = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_title


class Application(models.Model):
    loan = models.ForeignKey(Loans, related_name='applications', on_delete=models.CASCADE)

    apply_reason = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loan.loan_title





