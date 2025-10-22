import json
import sys

# Leer el notebook
with open('1-DescargarImagYFirmasfromGEE.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f'Total de celdas ANTES: {len(notebook["cells"])}')

# Mantener solo las primeras 8 celdas (índices 0-7) y las celdas 8-md y 8
# Las celdas duplicadas están después
unique_cells = []
seen = set()

for i, cell in enumerate(notebook['cells']):
    cell_id = cell.get('id', f'cell-{i}')
    cell_type = cell.get('cell_type')

    # Crear identificador único
    if cell_type == 'markdown':
        source = ''.join(cell.get('source', []))[:50]
        unique_id = f"{cell_type}_{source}"
    else:
        source = ''.join(cell.get('source', []))[:100]
        unique_id = f"{cell_type}_{source}"

    if unique_id not in seen:
        unique_cells.append(cell)
        seen.add(unique_id)
        print(f'Celda {i}: {cell_id} - {cell_type} - MANTENIDA')
    else:
        print(f'Celda {i}: {cell_id} - {cell_type} - ELIMINADA (duplicada)')

notebook['cells'] = unique_cells

# Ahora agregar la línea mágica de matplotlib al inicio de la celda 8
for cell in notebook['cells']:
    if cell.get('id') == 'cell-8' and cell.get('cell_type') == 'code':
        source = cell.get('source', [])
        if isinstance(source, list):
            source_text = ''.join(source)
        else:
            source_text = source

        # Verificar si ya tiene la línea mágica
        if '%matplotlib inline' not in source_text:
            # Agregar la línea mágica al inicio
            new_source = '%matplotlib inline\n' + source_text
            cell['source'] = new_source
            print('✅ Línea mágica de matplotlib agregada a celda-8')

print(f'\nTotal de celdas DESPUÉS: {len(notebook["cells"])}')

# Guardar
with open('1-DescargarImagYFirmasfromGEE.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print('✅ Notebook corregido y guardado')
