import glob

for f in glob.glob('chapter/*.tex'):
    with open(f, 'r') as file:
        content = file.read()
    if r'\cite{' in content:
        content = content.replace(r'\cite{', r'\citep{')
        with open(f, 'w') as file:
            file.write(content)
        print(f'Fixed {f}')
