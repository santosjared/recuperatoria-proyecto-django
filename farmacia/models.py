from django.db import models
from .validators import validate_alphabet
from .validators import validate_international_phone_number
from .validators import validate_no_negative
from .validators import validate_price_limit
from .validators import validate_stock_limit

class Medicament(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_no_negative,validate_price_limit])
    description = models.TextField(max_length=1000)
    photo = models.CharField(max_length=1000)
    stock = models.PositiveBigIntegerField(validators=[validate_stock_limit])
    expire_date = models.DateField()

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100,validators=[validate_alphabet])
    lastName = models.CharField(max_length=100, validators=[validate_alphabet])
    ci = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, validators=[validate_international_phone_number])
    address = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.lastName}"

class Venta(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_no_negative])
    def __str__(self):
        return f"venta a cliente: {self.client} - total: {self.total}"

class DetailVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[validate_no_negative])
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_no_negative])

