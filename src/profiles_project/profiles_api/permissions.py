from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to update their own profile. """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit it's own profile. """


        # SAFE_METHODS are read only methods, meaning that if the method is GET the user is only trying to see the users data
        if request.method in permissions.SAFE_METHODS: 
            return True

        # if obj.id (user id) is the same as in the request return True
        return obj.id == request.user.id
