try:
    import fitz
    print('fitz imported successfully')
except ImportError as e:
    print(f'Import error: {e}')
    import sys
    print('Python path:')
    for p in sys.path:
        print(p)