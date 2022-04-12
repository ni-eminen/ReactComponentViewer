"""Task module"""
from invoke import task


@task
def start(ctx):
    """Runs the application"""
    ctx.run("python ./index.py", pty=True)


@task
def which(ctx):
    """Checks python path"""
    ctx.run("which python", pty=True)


@task
def test(ctx):
    """Runs pytest on src"""
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    """Runs coverage with pytest"""
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    """Generates coverage report"""
    ctx.run("coverage html", pty=True)
