# Statistics API server

Microservice with some statistics APIs


## Development setup

### Prerequisites

1. (Optional) Install Pyenv ([Linux](https://github.com/pyenv/pyenv), [Windows](https://github.com/pyenv-win/pyenv-win)) and the [Python installation](.python-version) needed for this project:
```shell
pyenv install
```

2. [Install poetry](https://python-poetry.org/) to your system by following the [setup instructions](https://python-poetry.org/docs/#installation) convenient for you.

> [!IMPORTANT]
> You should **NOT** install poetry into your virtual environment as stated in their docs, as this may mess with your dependencies.

### Setup

1. Create a virtual environment:

> [!NOTE]
> For POSIX, pyenv can create a named virtual environment which you can use instead.
> For Windows, pyenv-win exists, but doesn't have this feature afaik.

```shell
# Create a local virtual environment (inside .venv/)
python3 -m venv .venv

# Activate it:

# Windows
./.venv/Scripts/activate

# POSIX
source ./.venv/bin/activate
```

2. Create development environment and install dependencies (pre-made script does it):

```shell
# [Windows] Run the `scripts/dev-setup.bat` script:
./scripts/dev-setup.bat

# [POSIX] Run the `scripts/dev-setup.sh` shell script using any bash-compatible shell:
bash ./scripts/dev-setup.sh
```

> [!NOTE]
> This scripts does the following:
> Creates a `dev/` folder needed to save log files and other persistent files used by the app, installs the requirements of the app using poetry, installs `pre-commit` hooks to this repository and also runs the pre-commit hooks.

3. Create a `.env` file from the given example and edit it:
```shell
cp .env.example .env

# Open the new .env file in your favourite editor and make the required changes
```

4. Run the dev server using `F5` key in VSCode. You can also use the `dev-launch` shell script:
```shell
# Windows
./scripts/dev-launch.bat

# POSIX
bash ./scripts/dev-launch.sh
```
