import random

"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """An placeholder for domestic and international shared attributes"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = ""
        self.tax = None

    def get_base_price(self):
        base_price = random.randint(5,9)
        return base_price

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()
        if self.species == "Christmas melons":
            base_price = 1.5 * base_price
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    def get_total(self):
        """Calculate price for international orders plus flat rate fee if applicable."""
        extra_base_cost = 0
        if self.qty < 10:
            extra_base_cost = 3
        return super(InternationalMelonOrder, self).get_total() + extra_base_cost


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government order"""

    def __init__(self, species, qty):
        """Initializes government orders"""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0
        self.order_type = "domestic"
        self.passed_inspection = False

    def mark_inspection(self, bool_value):
        self.passed_inspection = bool_value