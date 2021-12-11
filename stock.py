import reticker

"""Returns a list of stock tickers in the text"""
extract_tickers = lambda text: reticker.TickerExtractor().extract(text)
