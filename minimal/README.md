# Minimal Cally Example
This project contains a minimal example of how you could use cally to form the base of your install developer tools.

## Assumptions
The project makes some assumptions

- You have at least a currently supported version of Python
- The Venv project installed (this is not recommend for deployment, but useful for testing)

## Prepare
Clone the examples
```bash
git clone https://github.com/CallyCo-io/cally-examples.git
```

Change into the minimal directory
```bash
cd cally-examples/minimal
```

Install + Activate your Venv
```bash
python3 -m venv venv
source venv/bin/activate
```

Install the minimal idp
```bash
pip install -e . --upgrade
```

## Examples

### Hello World
```bash
(venv) ➜  minimal git:(main) ✗ cally example hello world
Hello world
```

### Pets Service Config
```bash
(venv) ➜  minimal git:(main) ✗ cally config print-service --environment dev --service example
BACKEND:
  path: '{name}/{environment}'
ENVIRONMENT: dev
NAME: example
STACK_TYPE: ExampleStack
```

### Generating a Terraform Template
```bash
(venv) ➜  minimal git:(main) ✗ cally tf print --environment dev --service example
```

Produces this output, which be passed to terrafrom for plan/apply
```json
{
  "//": {
    "metadata": {
      "backend": "local",
      "stackName": "example",
      "version": "0.20.5"
    },
    "outputs": {
    }
  },
  "terraform": {
    "backend": {
      "local": {
        "path": "example/dev"
      }
    }
  }
}
```
