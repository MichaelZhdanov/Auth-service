import subprocess
import os

def test_haproxy(file_path):
    try:
        result = subprocess.run(
            ["haproxy", "-c", "-f", file_path],
            capture_output=True,
            text=True
        )
        if "" in result.stdout:
           # print(f" Valid HAProxy config: {file_path}")
            return True
        else:
           # print(f" Invalid HAProxy config: {file_path}")
            return False
    except FileNotFoundError:
        print("Error: HAProxy is not installed")
        return False

def search_haproxy_files(root_dir):
    haproxy_files = []
    for root, dir, files in os.walk(root_dir):
        for file in files:
            if'haproxy' in file.lower():
                haproxy_files.append(os.path.join(root, file))
                return haproxy_files
            
if __name__ == "__main__":
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(tests_dir)
    haproxy_files = search_haproxy_files(project_root)
    results = [test_haproxy(f) for f in haproxy_files]
    success_count = sum(results)
    fail_count = len(results) - success_count
    for haproxy_file in haproxy_files:
        test_haproxy(haproxy_file)

    if not haproxy_files:
        print("No HAProxy files found")
        exit(1)
    elif fail_count > 0:
        print("HAProxy test unsuccessfull")
        exit(1)
    else:
        print("HAProxy tests passed")
        exit(0)