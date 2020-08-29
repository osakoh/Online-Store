from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Due to the 'related_name=products', objects can access all products in that category(category.products.all())
    """
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        """
        Meta:tells Django things about the database table
        specify that the singular form of the object of the Category database table should be 'category'
         and the plural form of the Category database table should be 'categories'
        """
        ordering = ('name',)
        verbose_name = 'category'  # singular form of objects in the Category db is 'category'
        verbose_name_plural = 'categories'  # plural form is 'categories'

    def __str__(self):
        return self.name

    # get_absolute_url() is the convention to retrieve the URL for a given object
    # link to a specific category i.e product_list
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """
    each product will have a name, an optional description, an optional
    image, a price, and its availability.
    category is a ForeignKey to the Category model.
    - a product belongs to one category and a category can have multiple products (one-to-many relationship)
    """
    # when a product is deleted, the database will also delete all related blog posts.
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)  # to build  URLs.
    # location of photo in media root 'products/%Y/%m/%d/'
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # optional field,
    description = models.TextField(blank=True)  # optional field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    # date is saved the first time a product is created in the database
    created = models.DateTimeField(auto_now_add=True)
    # date field changes whenever the 'save' button is pressed
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)  # sort according to name (a,b,c.....z)
        index_together = (('id', 'slug'),)  # query products in db using id&slug, it makes querying faster

    def __str__(self):
        return self.name

    # get_absolute_url() is the convention to retrieve the URL for a given object
    def get_absolute_url(self):
        # format: reverse(viewname, urlconf, args)
        return reverse('shop:product_detail', args=[self.id, self.slug])