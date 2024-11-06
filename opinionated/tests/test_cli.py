from unittest import TestCase

from cally import cli
from click.testing import CliRunner


class CliTests(TestCase):

    def test_example(self):
        result = CliRunner().invoke(
            cli.cally,
            ['example', 'hello', 'World'],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, 'Hello World\n')
