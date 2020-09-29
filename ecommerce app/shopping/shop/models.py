from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Role(models.Model):
    title = models.CharField(max_length=20)  # Customer or Vendor
    is_active = models.BooleanField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    """
    USERNAME_FIELD set the default Username for login, which is USERNAME as default
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.CharField(max_length=64, auto_created=True)
    customer = models.OneToOneField(User,
                                    on_delete=models.CASCADE, related_name='customer_email')
    vendor = models.OneToOneField(User,
                                  on_delete=models.CASCADE, related_name='vendor_email')
    order_status = models.CharField(max_length=20)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE, related_name='product_selected')
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.BooleanField()