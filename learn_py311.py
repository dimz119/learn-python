from datetime import datetime

def divide(numerator, denominator):
    return numerator / denominator

try:
    print(divide(4, 0))
except Exception as err:
        err.add_note(f"error occurs at {datetime.now()}")
        raise
