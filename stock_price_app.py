import yfinance as yf
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

BACKGROUND = '#040404'
DARK_BLUE = '#0a1e33'
def get_stock_price():
    stock_symbol = entry.get().upper()
    ticker_data = yf.Ticker(stock_symbol)

    latest_price = ticker_data.history(period='1d')['Close'].iloc[-1]
    # Display the price using the canvas's create_text method
    canvas_text.create_text(150, 20, text=f"Latest {stock_symbol} Close Price: ${latest_price:.2f}",
                            font=('Arial', 12), fill='blue')

    plot_stock(ticker_data)

def plot_stock(ticker_data):
    # Plot the closing prices over the selected time period
    historical_data = ticker_data.history(period='1mo')
    historical_data['Close'].plot(figsize=(10, 6))
    plt.title(f'{ticker_data.info.get("shortName")} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.show()


window = Tk()
window.title("Stock Price App")
window.geometry("800x600")
# Load the image file
bg_image = PhotoImage(file="background.png")

# Create a Canvas widget
canvas = Canvas(window, width=800, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Add the image to the canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create a Canvas to display text
canvas_text = Canvas(canvas, width=300, height=40, bg=DARK_BLUE, highlightthickness=0)
canvas_text.pack(side=BOTTOM)

label = Label(canvas, text="Enter Stock Ticker:")
label.pack(side=TOP, anchor='nw', padx=5, pady=5)  # Top-left (northwest)

entry = Entry(canvas)
entry.pack(side=TOP, anchor='nw', padx=5, pady=5)

button = Button(canvas, text="Get Price", command=get_stock_price)
button.pack(side=TOP, anchor='nw', padx=5, pady=5)



window.mainloop()
