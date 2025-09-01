import csv
import uuid
from datetime import datetime
from decimal import Decimal
from config import CSV_FILES, HEADERS

def generar_uuid():
    return str(uuid.uuid4())

def leer_csv(tabla):
    path = CSV_FILES[tabla]
    if not path.exists():
        return []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def escribir_csv(tabla, registros):
    path = CSV_FILES[tabla]
    campos = HEADERS.get(tabla)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for r in registros:
            writer.writerow(r)

def append_csv(tabla, registro):
    path = CSV_FILES[tabla]
    campos = HEADERS.get(tabla)
    write_header = not path.exists()
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        if write_header:
            writer.writeheader()
        writer.writerow(registro)

def str_a_decimal(s):
    try:
        return Decimal(str(s))
    except Exception:
        return Decimal('0')

def ahora_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def inicializar_csvs():
    for tabla, campos in HEADERS.items():
        path = CSV_FILES[tabla]
        if not path.exists():
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
