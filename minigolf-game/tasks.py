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
    ctx.run('python3 src/menu.py')
    
@task
def test(ctx):
    ctx.run('pytest')