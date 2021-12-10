import reticker

extract_tickers = lambda text: reticker.TickerExtractor().extract(text)
