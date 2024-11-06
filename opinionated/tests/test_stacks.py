from cally.cli.config.config_types import CallyStackService
from cally.idp.stacks.pets import RandomPets
from cally.idp.resources.random import Pet

from cally.cdk import CallyStack
from cally.testing import CallyTfTestHarness


class CallyStackTests(CallyTfTestHarness):

    def test_random_provider_our_defaults(self):
        config = self.get_cally_stack_config(stack_type='Pet')

        class PetRandom(CallyStack):
            def __init__(self, service: CallyStackService) -> None:
                super().__init__(service)
                self.add_resource(Pet('beagle'))

        stack = PetRandom(service=config.config)
        result = self.synth_stack(stack)
        self.assertEqual(
            result.get('provider', {}).get('random', {})[0].get('alias', ''), 'foo'
        )

    def test_random_pets(self):
        config = self.get_cally_stack_config(stack_type='RandomPets')
        stack = RandomPets(service=config.config)
        result = self.synth_stack(stack)
        self.assertDictEqual(
            result.get('resource', {}), self.load_json_file('random-pets.json')
        )
