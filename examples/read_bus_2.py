#!/usr/bin/env python

import argparse
import asyncio

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
        logger.info(str(mod))
        # print("")
    await asyncio.sleep(6000000000)


# Setup GCP logging
credentials = service_account.Credentials.from_service_account_file(
    "./gcp-credentials.json"
)
gcp_client = gcp_logging.Client(credentials=credentials)
gcp_client.setup_logging()


asyncio.run(main(args.connect), debug=True)
