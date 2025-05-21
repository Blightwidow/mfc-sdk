from dotenv import load_dotenv

load_dotenv()  # take environment variables

import mfc.core.modules.airports as airports

__all__ = [
    "airports",
]
__author__ = 'Dammaretz Theo'
__version__ = '0.0.1'
__license__ = 'MIT'
