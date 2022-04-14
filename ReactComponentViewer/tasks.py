"""Task module"""
from invoke import task


@task
def start(ctx):
    ctx.run("python ./src/index.py", pty=True)


@task
def which(ctx):
    ctx.run("which python", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
