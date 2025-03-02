# Generated by Django 5.1.3 on 2025-02-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0002_item_bank_transfer_file_item_receipt_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="bank_transfer_file",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AlterField(
            model_name="item",
            name="receipt_file",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
