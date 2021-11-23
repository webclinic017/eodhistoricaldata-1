"""apiclient.py"""

from enum import Enum
from re import compile as re_compile
from requests import get as requests_get
from requests import ConnectionError as requests_ConnectionError
from requests import Timeout as requests_Timeout
from requests.exceptions import HTTPError as requests_HTTPError
from rich.console import Console


class Interval(Enum):
    """Enum: infraday"""

    HOUR = "1h"


class TradingType(Enum):
    """Enum: infraday"""

    INTRADAY = "intraday"


class APIClient:
    """APIclass"""

    def __init__(self, api_key: str) -> None:
        # Validate API key
        prog = re_compile(r"^[A-z0-9.]{16,32}$")
        if not prog.match(api_key):
            raise ValueError("API key is invalid")

        self._api_key = api_key
        self._api_url = "https://eodhistoricaldata.com/api"

        self.console = Console()

    def get(
        self,
        trading_type: TradingType,
        symbol: str,
        interval: str = Interval
    ) -> dict:
        """Initiates a REST API call"""

        # Validate symbol
        prog = re_compile(r"^[A-z0-9-$\.]{5,48}$")
        if not prog.match(symbol):
            raise ValueError(f"Symbol is invalid: {symbol}")

        try:
            resp = requests_get(
                self._api_url + "/" +
                TradingType[trading_type].value + "/" +
                symbol +
                "?api_token=" + self._api_key + "&" +
                "interval=" + interval
            )

            if resp.status_code != 200:
                resp_message = resp.json()["message"]
                message = f"({resp.status_code}) {self._api_url} - {resp_message}"
                self.console.log(message)
                return {}

            resp.raise_for_status()
            return resp.text

        except requests_ConnectionError as err:
            self.console.log(err)
        except requests_HTTPError as err:
            self.console.log(err)
        except requests_Timeout as err:
            self.console.log(err)
