from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    subdomain = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    legal_name = models.CharField(max_length=100, blank=True, null=True)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    dun_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "organization"
        verbose_name = "organization"
        verbose_name_plural = "organizations"

    def __str__(self):
        return self.name
