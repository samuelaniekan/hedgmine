# Generated by Django 3.2.9 on 2021-12-02 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=40)),
                ('account_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=40)),
                ('bank', models.CharField(max_length=40)),
                ('balance_type', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_withdrawal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
