from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "GET" and obj:
            if obj.status == 'Moderated':
                return True
            else:
                return request.user.is_authenticated and request.user.has_perms('api_v1.view_quote')
        elif request.method == "PUT":
            return request.user.is_authenticated and request.user.has_perms('api_v1.change_quote')
        elif request.method == "DELETE":
            return request.user.is_authenticated and request.user.has_perms('api_v1.delete_quote')