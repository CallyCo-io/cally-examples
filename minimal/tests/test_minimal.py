from unittest import TestCase

from cally import cli
from cally.testing import CallyTfTestHarness
from click.testing import CliRunner

from cally.idp.stacks.example import ExampleStack


class CliTests(TestCase):

    def test_example(self):
        result = CliRunner().invoke(
            cli.cally,
            ['example', 'hello', 'World'],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, 'Hello World\n')


class CallyStackTests(CallyTfTestHarness):

    def test_random_pets(self):
        config = self.get_cally_stack_config(stack_type='ExampleStack')
        stack = ExampleStack(service=config.config)
        result = self.synth_stack(stack)
        self.assertDictEqual(
            result.get('terraform', {}), self.load_json_file('example.json')
        )
