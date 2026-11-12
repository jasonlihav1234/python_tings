"""
Click

- helps you make easy to use CLIs with python
- uses decorators to turn normal python functions into CLI commands
- @click.command() -> marks function as CLI command
- @click.option() -> defines optional flag parameters
- @click.argument() -> defines a required positional argument
    
"""
import click

# can call this like: ping-cli https://www.google.com --timeout 10
@click.command()
@click.argument("url")
@click.option("--timeout", default=5)
@click.option("--verbose", "-v", is_flag=True)
def ping(
    url: str,
    timeout: int,
    verbose: bool
):
    pass
