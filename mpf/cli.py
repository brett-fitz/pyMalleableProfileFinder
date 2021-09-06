import logging
import argparse
import asyncio
import os
from json import loads, JSONDecodeError
from typing import Union, Dict
from mpf.compare import Compare

# logger
logger = logging.getLogger('mpf')

# repo location
repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _guess_config(
        beacon_config: str,
        malleable_profiles: list
) -> Union[Dict, None]:
    result = {
        'beacon_config': None,
        'matching_fields': [],
        'malleable_profile': None,
        'confidence': 0
    }
    try:
        result['beacon_config'] = loads(beacon_config)
    except JSONDecodeError:
        logger.error(f'could not parse json: {beacon_config}')
        return None

    for malleable_profile in malleable_profiles:
        res = asyncio.run(
            Compare.compare_beacon_config(
                beacon_config=result['beacon_config'],
                malleable_profile=malleable_profile
            )
        )
    return result


def run():
    """
    cli entry point
    """
    parser = argparse.ArgumentParser(
        description='mpf: Cobalt Strike Malleable Profile Finder'
    )
    parser.add_argument(
        "file",
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

    try:
        logger.info(f'reading file {args.file}')
        with open(args.file, "r") as file:
            beacon_configs = [*file.read().splitlines()]
    except FileNotFoundError:
        logger.error(f'error file {args.file} does not exist')
        exit(1)

    logger.info(f'getting available malleable profiles')
    malleable_profiles = []
    for root, dirs, files in os.walk(f'{repo}/mpf/malleable_c2_profiles/Malleable-C2-Profiles/'):
        for file in files:
            if file.endswith('.profile') and file != 'template.profile':
                logger.info(f'loaded malleable profile {root}/{file}')
                malleable_profiles.append(f'{root}/{file}')

    results = []
    for beacon_config in beacon_configs:
        results.append(_guess_config(beacon_config, malleable_profiles))

    for result in results:
        print(result)
