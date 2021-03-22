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
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest')
    
@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report -m')
    
@task(coverage)
def coverage_html(ctx):
    ctx.run('coverage html')