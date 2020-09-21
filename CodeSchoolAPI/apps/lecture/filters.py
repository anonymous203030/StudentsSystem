from rest_framework import filters


class IsOwnerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)