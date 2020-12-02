import yfinance as yf
from typing import List
import pandas.core.frame


def fetching_data(name: str,
                  start: str,
                  stop: str
                  ) -> pandas.core.frame.DataFrame:
    """ Fetching data for multiple tickers.
    :param name: ticker symbol example "RIG"
    :param start: data beginning "y-m-d"
    :params end: end data "y-m-d"
    :returns: dataframe['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    """
    data = yf.download(name, start, stop)
    return data


class BaseModel(object):
    __slots__ = ('high', 'low', 'n')

    def __init__(self, high: float, low: float, n: int):
        """
        :param high: bar high
        :param low: bar low
        :param n: periods
        """
        self.high = high
        self.low = low
        self.n = n

    def payment_tr(self) -> float:
        """ The difference between the current high and low. """
        tr = self.high - self.low
        return tr

    def payment_art(self) -> float:
        """ The average value of TR over N periods. """
        tr = self.payment_tr()
        atr = tr/self.n
        return atr


if __name__ == '__main__':
    BaseModel()