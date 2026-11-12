import logging
import click

from .checker import check_urls

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%m:%S"
)

logger = logging.getLogger(__name__)

@click.command()
@click.argument("urls", nargs=-1)
@click.option("--timeout", default=5, help="Timeout in seconds for each request.")
@click.option("--verbose", "-v", is_flag=True, help="Enable debug logging.")
def main(urls, timeout, verbose):
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")
    if not urls:
        logger.warning("No URLs provided to check")
        click.echo("Usage: check-urls <URL1> <URL2> ...")
        return

    logger.info(f"Starting check for {len(urls)} URLs.")

    results = check_urls(list(urls), timeout)
    logger.info(f"Received urls: {urls}")
    logger.info(f"Received timeout: {timeout}")
    logger.info(f"Received verbose: {verbose}")


