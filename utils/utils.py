import json

class Formatter:
    @staticmethod
    def format_price(price: float) -> str:
        return f"{price:,.2f}"
    
    @staticmethod
    def get_color_change(change: float) -> str:
        if change >= 0: return "green"
        return "red"

def parse_binance_data(json_str: str) -> dict:
    try:
        data = json.loads(json_str)

        if not all(k in data for k in ("c", "p", "P")):
            return None
        
        return {
            "price": float(data["c"]),
            "change": float(data["p"]),
            "percent": float(data["P"])
        }
    except(json.JSONDecodeError, KeyError, ValueError):
        return None
