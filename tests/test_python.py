import ast
import os

def test_python(file_path):
    try:
        with open(file_path, 'r') as f:
            ast.parse(f.read())
        print(f" Valid Python: {file_path}")
        return True
    except SyntaxError as e:
        print(f" Invalid Python: {file_path}")
        return False
    
def search_python_files(root_dir):
    python_files = []
    for root, dir, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('py'):
                python_files.append(os.path.join(root, file))
    return python_files

if __name__ == "__main__":
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(tests_dir)
    python_files = search_python_files(project_root)
    if not python_files:
        print("No Python files found")
    else:
        results = [test_python(f) for f in python_files]
        success_count = sum(results)
        fail_count = len(results) - success_count
    for python_files in python_files:
        test_python(python_files)

    if fail_count > 0:
        print("Python test unsuccessfull")
        exit(1)
    else:
        print("Python tests passed")