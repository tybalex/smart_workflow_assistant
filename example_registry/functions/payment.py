"""Payment processing function implementations (Stripe)"""


def stripe_create_charge(amount: int, currency: str, source: str, description: str = None) -> str:
    """Create a charge in Stripe"""
    return ""


def stripe_create_customer(email: str, name: str = None, metadata: dict = None) -> str:
    """Create a customer in Stripe"""
    return ""

