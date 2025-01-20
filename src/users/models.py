from django.contrib.auth.hashers import make_password, is_password_usable
from django.core.exceptions import ValidationError
from validate_docbr import CPF
from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    login = models.CharField(max_length=70, unique=True)
    last_login = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=150, unique=True)  
    email = models.EmailField(max_length=125, unique=True)

    def save(self, *args, **kwargs) -> None:
        self.cpf = self.cpf.strip().replace(".", "").replace("-", "")
        if not CPF().validate(self.cpf):
            raise ValidationError("Invalid CPF")

        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
        
    def check_password(self, password: str) -> bool:
        """Check if the password is correct.

        Args:
            password (str): Password of the user.

        Returns:
            bool: Boolean indicating if the password is correct.
        """
        return check_password(password, self.password)

    def setPassword(self, password: str) -> None:
        """
        Set a new password for the user.

        Args:
            password (str): New password to set.

        Returns:
            str: the password status.
        """
    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.login
