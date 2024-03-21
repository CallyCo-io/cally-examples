from cally.cdk import CallyStack
from cally.cli.config.types import CallyStackService
from ..resources.random import Pet


class RandomPets(CallyStack):

    def __init__(self, service: CallyStackService) -> None:
        super().__init__(service)
        random_pet = Pet('random-pet')
        another_random_pet = Pet('another-random-pet', depends_on=[random_pet])
        self.add_resources([random_pet, another_random_pet])
