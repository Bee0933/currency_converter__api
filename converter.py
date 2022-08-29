from forex_python.converter import CurrencyRates
import numpy as np
import datetime


# currency converter function
def convert(amount, base_currency, conv_currency) -> dict:

      date_obj = datetime.datetime.now()
      
      # exchange instance
      curr = CurrencyRates()
      AMOUNT = float(amount)
      FROM = str(base_currency).upper()
      TO = str(conv_currency).upper()
      exchange_rate = np.round(curr.get_rate(FROM,TO,date_obj),4)
      converted_result = np.round(curr.convert(FROM, TO, AMOUNT,date_obj),4)

      return {
            "price_date" : date_obj.strftime("%d/%m/%Y"),
            "from_currency" : FROM,
            "to_currency" : TO,
            "exchange_rate" : exchange_rate,
            "converted_value" : converted_result
      }


def availble_currencies() -> dict:
      c = CurrencyRates()
      rates = c.get_rates("USD")

      return {
            "available currencies" : list(rates.keys())
      }
