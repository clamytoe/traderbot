from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
    symbol_or_symbols=[
        "BTC/USD",
        "ETH/USD",
        "XRP/USD",
        "XLM/USD",
        "HBAR/USD",
        "SHIB/USD",
    ],
    timeframe=TimeFrame.Day,
    start="2022-07-01",
)

bars = client.get_crypto_bars(request_params)

# Convert CryptoBars to a Pandas DataFrame
df = bars.df

# Convert to JSON
json_data = df.to_json()

with open("crypto_data.json", "w") as f:
    f.write(json_data)


print(json_data)
