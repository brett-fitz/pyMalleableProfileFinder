import logging
import argparse

# logger
logger = logging.getLogger('mc2pf')


def run():
    """
    cli entry point
    """
    parser = argparse.ArgumentParser(
        description='mc2pf: Malleable C2 Profile Finder'
    )
    parser.add_argument(
        "beacon_configs",
        nargs="+",
        help="File of beacon config(s) in json, one json blob per line."
    )
    parser.add_argument(
        "--debug",
        help="[OPTIONAL] show debug output",
        action="store_true",
        default=False
    )
    args = parser.parse_args()

    log_level = logging.WARNING
    if args.debug:
        log_level = logging.INFO
    logging.basicConfig(level=log_level,
                        format='%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p')

