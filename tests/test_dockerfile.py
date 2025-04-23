import subprocess
import os

def test_dockerfile(file_path):
    try:
        result = subprocess.run(
            ["docker", "build", "--no-cache", file_path],
            capture_output=True,
            text=True

        )
        if "Successfully built" in result.stdout:
            print(f" Valid Dockerfile: {file_path}")
            return True
        else:
            print(f" Invalid Dockerfile: {file_path}")
            return False
    except FileNotFoundError:
        print("Error: Docker is not installed or not running")
        return False
    
def search_dockerfiles(root_dir):
    dockerfiles = []
    for root, dir, files in os.walk(root_dir):
        for file in files:
            if 'Dockerfile' in file:
                dockerfiles.append(root)
                break
    return dockerfiles

if __name__ == "__main__":
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(tests_dir)
    dockerfiles = search_dockerfiles(project_root)
    results = [test_dockerfile(f) for f in dockerfiles]
    success_count = sum(results)
    fail_count = len(results) - success_count
    for dockerfile in dockerfiles:
        test_dockerfile(dockerfile)

    if not dockerfiles:
        print("No Dockerfiles found")
        exit(1)
    elif fail_count > 0:
        print("Dockerfile test unsuccessfull")
        exit(1)
    else:
        print("Dockerfile tests passed")
        exit(0)