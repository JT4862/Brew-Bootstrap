import subprocess

def install_package(package_name):
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")

def main():
    with open('ubuntu-packages.txt', 'r') as f:
        packages = [line.strip() for line in f]

    for package in packages:
        install_package(package)

if __name__ == "__main__":
    main()