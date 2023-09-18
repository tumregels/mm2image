import pathlib
import shutil

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


@task(help={'clean': 'remove old artifacts'})
def build_exe(ctx, clean=False):
    """Build single file executable"""
    if clean:
        shutil.rmtree("build")
        shutil.rmtree("dist")
    ctx.run("pyinstaller --onefile --noconsole --noconfirm mm2image.py")


@task(help={'clean': 'remove old artifacts'})
def build_sdist_wheel(ctx, clean=False):
    """Build source and build distributions"""
    if clean:
        shutil.rmtree("build")
        shutil.rmtree("dist")
    ctx.run("python -m build .")
