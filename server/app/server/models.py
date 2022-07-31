from django.db import models

class PizzaOrder(models.Model):
    """
    Model representing a pizza order.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pizzas = models.ManyToManyField('Pizza', related_name='pizzas')
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.first_name + ' ' + self.last_name


class Pizza(models.Model):
    """
    Model representing a pizza.
    """
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField('Ingredient', related_name='ingredients')
    image = models.ImageField(upload_to='pizza_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Pizzas'
        verbose_name = 'Pizza'

class Ingredient(models.Model):
    """
    Model representing an ingredient.
    """
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ingredients'
        verbose_name = 'Ingredient'