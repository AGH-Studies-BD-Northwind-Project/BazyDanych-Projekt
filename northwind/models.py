from django.db import models, connection


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.category_name}"

class CustomerDemographic(models.Model):
    customer_type_id = models.CharField(primary_key=True, max_length=30)
    customer_desc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customer_demographics'

class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=30)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    customer_demographics = models.ManyToManyField(CustomerDemographic)

    class Meta:
        db_table = 'customers'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_description = models.CharField(max_length=30)

    class Meta:
        db_table = 'region'


class Territory(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=20)
    territory_description = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'territories'
        verbose_name_plural = "territories"

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reports_to = models.ForeignKey('self', models.SET_NULL, db_column='reports_to', blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)
    territories = models.ManyToManyField(Territory)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.title + ' ' + self.firstname + ' ' + self.lastname

class OrderDetail(models.Model):
   # order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', models.SET_NULL, null=True)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    class Meta:
        db_table = 'order_details'
        unique_together = (('order', 'product'),)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_via = models.ForeignKey('Shipper', on_delete=models.SET_NULL, db_column='ship_via', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)
    ship_name = models.CharField(max_length=40, blank=True, null=True)
    ship_address = models.CharField(max_length=60, blank=True, null=True)
    ship_city = models.CharField(max_length=15, blank=True, null=True)
    ship_region = models.CharField(max_length=15, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=10, blank=True, null=True)
    ship_country = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'orders'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40)
    supplier = models.ForeignKey('Supplier', models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey('Category', models.SET_NULL, blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True, default=1)
    unit_price = models.FloatField(blank=True, null=True)
    units_in_stock = models.SmallIntegerField(blank=True, null=True, default=0)
    units_on_order = models.SmallIntegerField(blank=True, null=True, default=0)
    reorder_level = models.SmallIntegerField(blank=True, null=True, default=0)
    discontinued = models.IntegerField( default=0)
    picture = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"{self.product_name}"


class Shipper(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        db_table = 'shippers'

    def __str__(self):
        return self.companyname

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'suppliers'

    def __str__(self):
        return f"{self.company_name}"

class UsState(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    state_region = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'us_states'
