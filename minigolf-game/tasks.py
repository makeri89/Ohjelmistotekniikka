from invoke import task

"""
Tasks for invoke
"""


@task
def pep(ctx):
    ctx.run('autopep8 --in-place --recursive src')


@task(pep)
def lint(ctx):
    ctx.run('pylint src')


@task
def start(ctx):
    ctx.run('python3 src/index.py')


@task
def test(ctx):
    ctx.run('pytest')


@task
def test_nonvisual(ctx):
    """
    Github actions cannot run visual pygame tests.
    """
    ctx.run('pytest -m "nonvisual"')


@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest')


@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report -m')


@task(coverage)
def coverage_html(ctx):
    ctx.run('coverage html')


@task
def initialize_db(ctx):
    ctx.run('python3 src/services/database/initialize_db.py')


@task
def print_scores(ctx):
    ctx.run('python3 src/db_handler.py')
