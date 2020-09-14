from django.db import models

# Create your models here.

import re

from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def _create_user(self, username, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        username = self.model.normalize_username(username)
        user = self.model(username=username,
                          last_login=now, date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password,
                                 is_staff=True, is_admin=True, is_superuser=True,
                                 **extra_fields)
        user.save(using=self._db)
        return user


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(_('Tipo de Perfil'), max_length=30,
                            null=False, blank=False)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = _('Perfil de Acesso')
        verbose_name_plural = _('Perfis de Acesso')


class User(AbstractBaseUser, PermissionsMixin):

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null = True)
    username = models.CharField(_('username'), max_length=15, unique=True,
                                null=False, blank=False)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(_('first name'), max_length=30,
                                  null=False, blank=False)
    last_name = models.CharField(_('last name'), max_length=30,
                                 null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True,
                              validators=[
                                          validators.RegexValidator(re.compile(
                                              '^[\w.@+-]+$'),
                                              _('Enter a valid e-mail'),
                                              _('invalid'))],
                              null=False, blank=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
