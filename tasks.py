import pathlib

from invoke import task

BASE_DIR = pathlib.Path(__file__).resolve().parent


@task
def generate_requirements(c):
    """Generate requirements.txt from requirements.in"""
    c.run(f"pip-compile requirements.in")
    print('done')


@task
def generate_dev_requirements(c):
    """Generate dev-requirements.txt"""
    c.run(f"pip-compile dev-requirements.in")
    print('done')


@task
def install_requirements(c):
    """Install requirements into venv"""
    c.run("pip install -r requirements.txt")
    print('done')


@task
def install_dev_requirements(c):
    """Install dev requirements into venv"""
    c.run("pip install -r dev-requirements.txt")
    print('done')


@task(pre=[generate_requirements, generate_dev_requirements])
def update(c):
    """Generate/update all requirements"""
    c.run("pip-sync requirements.txt dev-requirements.txt")
    print('done')
