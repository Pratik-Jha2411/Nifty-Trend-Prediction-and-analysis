import json
import glob
for f in glob.glob('*.ipynb'):
    with open(f, 'r', encoding='utf-8') as file:
        nb = json.load(file)
    if 'metadata' in nb and 'widgets' in nb['metadata']:
        del nb['metadata']['widgets']
        with open(f, 'w', encoding='utf-8') as file:
            json.dump(nb, file, indent=1)
        print(f'Fixed {f}')
