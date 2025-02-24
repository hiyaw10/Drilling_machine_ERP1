# Generated by Django 5.1.3 on 2025-02-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="Transferred_from",
            new_name="Transferred_from_bank_name",
        ),
        migrations.RenameField(
            model_name="item",
            old_name="Transferred_to",
            new_name="Transferred_to_bank_name",
        ),
        migrations.AddField(
            model_name="item",
            name="Transferred_from_account_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="Transferred_from_sender_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="Transferred_to_account_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="Transferred_to_receiver_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
