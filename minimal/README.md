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

### Using your own entrypoint
```bash
(venv) ➜  minimal git:(main) ✗ minimal-idp config print-service --environment dev --service pets
ENVIRONMENT: dev
NAME: pets
PROVIDERS:
  random:
    alias: foo
STACK_TYPE: RandomPets
```

### Pets Service Config
```bash
(venv) ➜  minimal git:(main) ✗ cally config print-service --environment dev --service pets
ENVIRONMENT: dev
NAME: pets
PROVIDERS:
  random:
    alias: foo
STACK_TYPE: RandomPets
```

### Generating a Terraform Template
```bash
(venv) ➜  minimal git:(main) ✗ cally tf print --environment dev --service pets
```

Produces this output, which be passed to terrafrom for plan/apply
```json
{
  "//": {
    "metadata": {
      "backend": "local",
      "stackName": "pets",
      "version": "0.20.5"
    },
    "outputs": {
    }
  },
  "provider": {
    "random": [
      {
        "alias": "foo"
      }
    ]
  },
  "resource": {
    "random_pet": {
      "another-random-pet": {
        "//": {
          "metadata": {
            "path": "pets/another-random-pet",
            "uniqueId": "another-random-pet"
          }
        },
        "depends_on": [
          "random_pet.random-pet"
        ],
        "provider": "random.foo"
      },
      "random-pet": {
        "//": {
          "metadata": {
            "path": "pets/random-pet",
            "uniqueId": "random-pet"
          }
        },
        "provider": "random.foo"
      }
    }
  },
  "terraform": {
    "backend": {
      "local": {
        "path": "state/pets.tfstate"
      }
    },
    "required_providers": {
      "random": {
        "source": "hashicorp/random",
        "version": "3.6.0"
      }
    }
  }
}
```
