from forex_python.converter import CurrencyRates
import numpy as np
import datetime

# currency converter function
def convert(amount, base_currency, conv_currency):

      date_obj = datetime.datetime.now()
      
      # exchange instance
      curr = CurrencyRates()
      AMOUNT = float(amount)
      FROM = str(base_currency).upper()
      TO = str(conv_currency).upper()
      exchange_rate = np.round(curr.get_rate(FROM,TO,date_obj),4)
      converted_result = np.round(curr.convert(FROM, TO, AMOUNT,date_obj),4)

      return (date_obj.strftime("%d/%m/%Y"),exchange_rate, converted_result)


if __name__ == '__main__':
      date, rate, amnt = convert(500,'USD','EUR')
      print(f"exchange rate at {date} is {rate}, amount {amnt}")




