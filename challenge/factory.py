from challenge.model import DelayModel
from challenge.service import DelayService


def delay_service_factory():
    model = DelayModel()
    return DelayService(model)
