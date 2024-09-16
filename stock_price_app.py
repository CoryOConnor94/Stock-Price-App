import yfinance as yf
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt


def get_stock_price():
    stock_symbol = entry.get().upper()
    ticker_data = yf.Ticker(stock_symbol)

    latest_price = ticker_data.history(period='1d')['Close'].iloc[-1]
    messagebox.showinfo(f"Stock Price: {stock_symbol}",f"Latest price: {latest_price}")

    # messagebox.showerror("Error","Unable to fetch data. Please check the stock symbol.")

    # Plot the closing prices over the selected time period
    historical_data = ticker_data.history(period='1mo')
    historical_data['Close'].plot(figsize=(10, 6))
    plt.title(f'{stock_symbol} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.show()


window = Tk()
window.title("Stock Price App")
window.config(padx=20, pady=20)

label = Label(window, text="Enter Stock Ticker:")
label.pack()

entry = Entry(window)
entry.pack()

button = Button(window, text="Get Price", command=get_stock_price)
button.pack()



window.mainloop()
