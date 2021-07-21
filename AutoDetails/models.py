from django.db import models

class VehicleDetails(models.Model):
    manufacture_choices = (
        ('D', 'Choose the Manufacturer'),
        ('TM', 'Tata Motors'),
        ('MM', 'Mahindra & Mahindra Ltd'),
        ('MS', 'Maruti Suzuki'),
        ('HML', 'Hero MotoCorp Ltd'),
        ('BAL', 'Bajaj Auto Limited'),
        ('TMC', 'Toyota Motor Corporation'),
        ('C', 'Chevrolet'),
        ('MMC', 'Mitsubishi Motors Corporation')
    )
    mno_choices = (
        ('D', 'Choose the Model Number'),
        (1, 'ABC123'),
        (2, 'XYZ377'),
        (3, 'HJUSGE')
    )
    vt_choices = (
        ('D', 'Choose the Vehicle Type'),
        ('S', 'SEDAN'),
        ('C', 'COUPE'),
        ('SC', 'SPORTS CAR'),
        ('SW', 'STATION WAGON'),
        ('HB', 'HATCHBACK'),
        ('CN', 'CONVERTIBLE')
    )
    rto_choices = (
        ('D', 'Select the RTO Department'),
        ('RC', 'RTO Chandigarh'),
        ('RD', 'RTO Delhi'),
        ('RA', 'RTO Agra'),
        ('RJ', 'RTO Jaipur')
    )
    sap_code = models.CharField(max_length=20, default="")
    ledger_name = models.CharField(max_length=20, default="")
    manufacturer = models.CharField(max_length=30, choices=manufacture_choices, default="D")
    mno = models.CharField(max_length=20, choices=mno_choices, default="D")
    vehicle_type = models.CharField(max_length=20, choices=vt_choices, default="D")
    base_km = models.IntegerField(default=0)
    rto = models.CharField(max_length=20, choices=rto_choices, default="D")

    def __str__(self):
        return self.sap_code

class EngineDetails(models.Model):
    my_choices = (
        ('D', 'Choose the Model Year'),
        (1, 2000),
        (2, 2001),
        (3, 2002),
        (4, 2003)
    )
    ft_choices = (
        ('D', 'Choose the Fuel Type'),
        ('P', 'Petrol'),
        ('Di', 'Diesel'),
        ('G', 'Gasoline'),
        ('C', 'CNG')
    )
    model_year = models.CharField(max_length=20, choices=my_choices, default="D")
    chassis_no = models.CharField(max_length=20, default="")
    fuel_type = models.CharField(max_length=20, choices=ft_choices, default="D")
    old_vehicle_no = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.chassis_no