from rest_framework.request import Request

from common.http import is_true
from perms.utils import UserPermTreeRefreshUtil
from users.models import User

__all__ = ['RebuildTreeMixin']


class RebuildTreeMixin:
    user: User

    def get(self, request: Request, *args, **kwargs):
        force = is_true(request.query_params.get('rebuild_tree'))
        UserPermTreeRefreshUtil(self.user).refresh_if_need(force)
        return super().get(request, *args, **kwargs)
