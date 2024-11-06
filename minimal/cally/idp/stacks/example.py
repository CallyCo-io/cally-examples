from cally.cdk import CallyStack
from cally.cli.config.config_types import CallyStackService


class ExampleStack(CallyStack):

    def __init__(self, service: CallyStackService) -> None:
        super().__init__(service)
        self.add_output('foo', self.service.get_stack_var('foo', 'foo'))
        self.add_output('bar', self.service.get_stack_var('bar', 'foo'))
