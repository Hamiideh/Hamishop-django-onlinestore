from django.contrib.auth import get_user_model
from django.db.models import TextField
from django.utils import timezone
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    top_products = models.ForeignKey('Product', related_name='+', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT, null=True, blank=True)
    description = TextField(verbose_name=_("description"))
    short_description = TextField(verbose_name=_("short_description"),blank=True)
    price = models.PositiveIntegerField(verbose_name=_("price"),default=0)
    inventory = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(verbose_name=_("active"),default=True)
    image = models.ImageField(verbose_name=_("Product image"), upload_to='product/product_cover/', blank=True, )


    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_("Date Time of Creation"))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_("Date Time of Modified"))


    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('product_detail', args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('Comment author'))
    body = models.TextField(verbose_name=_("comment text"))
    stars = models.CharField(choices=PRODUCT_STARS, max_length=10, verbose_name=_("what is your score?"))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)



    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

