# Generated by Django 4.2.7 on 2023-12-17 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light_mode', '0002_alter_newsletter_options_newsletter_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-created_date']},
        ),
    ]