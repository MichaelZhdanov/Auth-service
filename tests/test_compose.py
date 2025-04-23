import subprocess
import os

def test_compose(file_path):
    try:
        result = subprocess.run(
            ["docker-compose", "-f", file_path, "config"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f" Valid Docker Compose file: {file_path}")
            return True
        else:
            print(f" Invalid Docker Compose file: {file_path}")
            return False
    except FileNotFoundError:
        print("Error: Docker Compose is not installed")
        return False
    
if __name__ == "__main__":
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(tests_dir)
    compose_files = [
        os.path.join(root_dir, file)
        for file in os.listdir(root_dir)
        if file.lower().endswith('docker-compose.yml') or file.lower().endswith('docker-compose.yaml')
    ]

    if not compose_files:
        print("No Docker Compose files found")
        exit(1)
    else:
        for compose_file in compose_files:
            test_compose(compose_file)