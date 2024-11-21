try:
    import pandas as pd
    print("Pandas is working correctly! Version:", pd.__version__)
except ModuleNotFoundError:
    print("Pandas is not installed.")
