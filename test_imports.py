import sys
print("Python is working!")
print(f"Python version: {sys.version}")

try:
    import pdfplumber
    print("pdfplumber imported successfully")
except ImportError as e:
    print(f"pdfplumber import error: {e}")

try:
    import pandas
    print("pandas imported successfully")
except ImportError as e:
    print(f"pandas import error: {e}")
