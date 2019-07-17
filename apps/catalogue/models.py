from django.utils.timezone import now

from oscar.apps.catalogue.abstract_models import AbstractProduct
from oscar.core.loading import get_model


ConditionalOffer = get_model('offer', 'ConditionalOffer')


class Product(AbstractProduct):

    def sale_price(self):
        if self.includes.filter(
            benefit__offers__offer_type=ConditionalOffer.SALE,
            benefit__offers__start_datetime__lt=now(),
            benefit__offers__end_datetime__gt=now(),
        ).exists():
            range_ = self.includes.first()
            benefit = range_.benefit_set.first()
            return benefit.calculate_sale_price(self)


from oscar.apps.catalogue.models import *  # noqa isort:skip