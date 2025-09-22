#!/usr/bin/env python

import argparse
import asyncio

import mh_structlog as logging

from velbusaio.controller import Velbus

logging.setup()
logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "--connect", help="Connection string", default="tls://192.168.1.9:27015"
)
args = parser.parse_args()


async def main(connect_str: str):
    velbus = Velbus(connect_str)
    await velbus.connect()
    await velbus.start()
    for mod in (velbus.get_modules()).values():
        print(mod)
        print("")
    await asyncio.sleep(6000000000)


asyncio.run(main(args.connect), debug=True)
