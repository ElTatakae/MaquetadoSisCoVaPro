from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class usuarioAdmin(BaseUserManager):
    def create_user(self, numeroEmpleado, username, password=None):
        if not numeroEmpleado:
            raise ValueError('El usuario debe tener un número de empleado')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')

        user = self.model(
            numeroEmpleado=numeroEmpleado,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user