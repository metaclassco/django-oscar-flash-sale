# Generated by Django 2.1 on 2019-09-16 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0012_customabsolutediscountbenefit_custompercentagediscountbenefit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomAbsoluteDiscountBenefit',
            new_name='CustomAbsoluteDiscountPerProductBenefit',
        ),
    ]
