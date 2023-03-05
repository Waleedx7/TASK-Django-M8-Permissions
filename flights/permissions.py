import datetime
from rest_framework.permissions import BasePermission
class IsBookingOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user


class IsEditableBooking(BasePermission):
    message = "Too close to booking date."

    def has_object_permission(self, request, view, obj):
        today = datetime.date.today()
        diff = obj.date - today
        return diff.days > 3