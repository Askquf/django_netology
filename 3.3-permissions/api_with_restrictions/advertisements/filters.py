from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    class FilterSet(filters.FilterSet):
        created_at = filters.DateFromToRangeFilter()
        status = filters.Filter()

        class Meta:
            model = Advertisement
            fields = ['created_at', 'status']
