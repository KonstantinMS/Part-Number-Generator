import pandas as pd


def write_to_excel(parts, output_file):
    """
    Функция для записи в Excel
    """
    try:
        df = pd.DataFrame(parts)
        df.to_excel(output_file, index=False)
        return True
    except ImportError:
        print("Для записи в Excel установите pandas: pip install pandas")
        return False
    except Exception as e:
        print(f"Ошибка записи в Excel: {e}")
        return False
