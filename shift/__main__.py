from ..util import console
from ..util import logging


logging.start()

print("Parsing command line arguments...")
args = console.parse()
missing = list(console.missing_keys("input", "output", "shift", args=args))
if missing:
    logging.terminate("Missing parameters: %s" % missing, -1)

logging.finish()
