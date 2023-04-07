from rolepermissions.roles import AbstractUserRole


class Dono(AbstractUserRole):
    available_permissions = {
        'criar_posts': True,
        'criar_tags': True,
        'tornar_staff': True,
        'comentar': True,
    }


class Staff(AbstractUserRole):
    available_permissions = {
        'criar_posts': True,
        'comentar': True,
    }


class Usuario(AbstractUserRole):
    available_permissions = {
        'comentar': True,
    }
