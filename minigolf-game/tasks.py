from invoke import task

"""
Tasks for invoke
"""

@task
def lint(ctx):
    ctx.run('pylint src')

@task
def pep(ctx):
    ctx.run('autopep8 --in-place --recursive src')
    