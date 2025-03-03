import os
import re

def extract_imports(file_path):
    imports = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'\s*(?:import|from)\s+([\w\.]+)', line)
            if match:
                imports.add(match.group(1).split('.')[0])
    return imports

def find_python_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

def main():
    folder = os.getcwd()
    py_files = find_python_files(folder)
    all_imports = set()
    
    for file in py_files:
        print(f'Scanning: {file}')
        all_imports.update(extract_imports(file))
    
    print("\nIdentified Imports:")
    for imp in sorted(all_imports):
        print(imp)

if __name__ == "__main__":
    main()
