import csv
import argparse
import sys

EXPECTED_COLUMNS = {
    'data/careers.csv': ['career_id', 'career_name', 'career_slug'],
    'data/subjects.csv': [
        'subject_id', 'career_id', 'subject_name', 'term',
        'official_url', 'notes', 'starts'
    ],
}


def validate_file(path, expected_columns):
    with open(path, encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            raise ValueError(f'El archivo {path} está vacío.')

    missing = [col for col in expected_columns if col not in headers]
    extra = [col for col in headers if col not in expected_columns]

    if missing:
        raise ValueError(
            f'Faltan columnas en {path}: {missing}. '
            f'Columnas esperadas: {expected_columns}.'
        )

    if extra:
        print(f'Advertencia: columnas adicionales en {path}: {extra}', file=sys.stderr)

    return headers


def main():
    parser = argparse.ArgumentParser(
        description='Valida la estructura básica de los CSV del proyecto.'
    )
    parser.add_argument(
        'files', nargs='*', default=list(EXPECTED_COLUMNS.keys()),
        help='Archivos CSV a validar (por defecto valida todos).'
    )
    args = parser.parse_args()

    exit_code = 0
    for file_path in args.files:
        expected = EXPECTED_COLUMNS.get(file_path)
        if expected is None:
            print(f'No hay un esquema definido para {file_path}', file=sys.stderr)
            exit_code = 1
            continue

        try:
            headers = validate_file(file_path, expected)
            print(f'{file_path} OK ({len(headers)} columnas)')
        except Exception as exc:
            print(f'Error en {file_path}: {exc}', file=sys.stderr)
            exit_code = 1

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
