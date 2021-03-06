# Generated by Django 2.2.6 on 2019-10-10 19:29

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address')),
                ('logged_in', models.DateTimeField(auto_now=True, verbose_name='Last login date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DefaultSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('TEXT', 'Texte'), ('DATETIME', 'Date & heure'), ('DATE', 'Date'), ('DATERANGE', 'Plage de date'), ('TIME', 'Heure'), ('TIMERANGE', 'Plage horaire'), ('SELECT', 'Choix'), ('INTEGER', 'Nombre entier'), ('FLOAT', 'Nombre décimal'), ('BOOLEAN', 'Booléen (oui/non)')], default=('TEXT', 'Texte'), max_length=9)),
                ('optional', models.BooleanField(default=True)),
                ('choices', models.TextField(blank=True, null=True)),
                ('default', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('color', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('#(?:[A-Fa-f0-9]{3}){1,2}', 'Please use a valid hexadecimal color format, eg. #268CCE, or #FFF')])),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
                ('abbreviation', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('[a-z_\\-]{2,3}', 'Please use exactly 2 or 3 lower-case letters (- and _ are also accepted)')])),
                ('goal', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, 'This should be a value between 0 and 1')])),
                ('weight', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0, "The grade's weight cannot be negative")])),
                ('room', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('value', models.TextField(blank=True, null=True)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.DefaultSetting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
