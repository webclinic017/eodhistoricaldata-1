"""API example"""

from eodhistoricaldata import APIClient


def main() -> None:
    """Main"""

    api = APIClient("") # <-- add your API key here!

    # resp = api.get_exchanges()
    # resp = api.get_exchange_symbols("CC")

    # resp = api.get_historical_data("BTC-USD.CC", "1m")
    # resp = api.get_historical_data("BTC-USD.CC", "1m", "2021-11-27 23:56:00")
    resp = api.get_historical_data(
        "BTC-USD.CC", "1m", "2021-11-27 23:56:00", "2021-11-27 23:59:00"
    )

    # resp = api.get_historical_data("BTC-USD.CC", "1d")
    # resp = api.get_historical_data("BTC-USD.CC", "1d", "2021-11-24")
    # resp = api.get_historical_data("BTC-USD.CC", "1d", "2021-11-24", "2021-11-27")

    print(resp.dtypes)
    print(resp.describe())
    print(resp)


if __name__ == "__main__":
    main()
