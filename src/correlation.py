def calculate_returns(df):
    df["daily_return"] = df["Close"].pct_change() * 100
    return df