from django.contrib.auth.mixins import PermissionRequiredMixin


class NotPermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        if super().has_permission():
            return False
        return True