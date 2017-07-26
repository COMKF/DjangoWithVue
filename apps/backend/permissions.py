__author__ = 'YMH'
# 因为默认的权限模式是，认证用户能够修改删除所有文件，现在我们需要只有创建者才能删除或修改自己的文件。
# 就需要自定义权限认证方法。

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只有创建者才能编辑
    """

    def has_object_permission(self, request, view, obj):
        print(123123123)
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
