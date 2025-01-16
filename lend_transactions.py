import json
import time_transactions


def write_lend_file(veriler):
    pass
def read_lend_file():
    try:
        with open ("lend.json", "r", encoding="utf-8") as f:
            lend_listesi = json.dumps(f)
            return lend_listesi
    except (FileNotFoundError, json.JSONDecodeError):
        print("Emanet verileri bulunamadı veya dosya boş.")  