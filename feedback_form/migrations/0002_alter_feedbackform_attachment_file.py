# Generated by Django 4.2.3 on 2023-07-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackform',
            name='attachment_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
