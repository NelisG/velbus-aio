#!/usr/bin/env python

import argparse
import asyncio
import sys

import mh_structlog as logging
from google.cloud import logging as gcp_logging
from google.oauth2 import service_account

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
        logging.info(mod)
        # print("")
    await asyncio.sleep(6000000000)


# Setup GCP logging
credentials = service_account.Credentials.from_service_account_file(
    "./gcp-credentials.json"
)
gcp_client = gcp_logging.Client(credentials=credentials)
gcp_client.setup_logging()
# logging.getLogger("velbusaio").setLevel(logging.DEBUG)
# logging.getLogger("velbus-protocol").setLevel(logging.DEBUG)
# logging.getLogger("velbus-module").setLevel(logging.DEBUG)
# logging.getLogger("velbus-handler").setLevel(logging.DEBUG)
# logging.getLogger("velbus-vlpFile").setLevel(logging.DEBUG)
# logging.getLogger("velbus").setLevel(logging.DEBUG)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    style="{",
    datefmt="%H:%M:%S",
    format="{asctime} {levelname:<9} {message}",
)
logging.getLogger("asyncio").setLevel(logging.DEBUG)

asyncio.run(main(args.connect), debug=True)
