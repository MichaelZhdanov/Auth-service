import os
from bs4 import BeautifulSoup as bs

def test_html(file_path):
    try:
        with open(file_path) as f:
            soup = bs(f.read(), 'html.parser')
        print(f" Valid HTML: {file_path}")
        return True
    except Exception as e:
        print(f" Invalid HTML in {file_path}: {str(e)}")
        return False

def search_html_files(root_dir):
    html_files = []
    for root, dir, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('html'):
                html_files.append(os.path.join(root, file))
    return html_files

if __name__ == "__main__":
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(tests_dir)
    html_files = search_html_files(project_root)
    if not html_files:
        print("No HTML files found")
    else:
        results = [test_html(f) for f in html_files]
        success_count = sum(results)
        fail_count = len(results) - success_count
    for html_file in html_files:
        test_html(html_file)

    if fail_count > 0:
        print("HTML test unsuccessfull")
        exit(1)
    else:
        print("HTML tests passed")