import subprocess

def install_package(package_name):
    print(f"Installing {package_name}...")
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
        print(f"Successfully installed {package_name}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")
        return False

def main():
    with open('ubuntu-packages.txt', 'r') as f:
        packages = [line.strip() for line in f]

    successful_installs = 0
    failed_installs = 0

    for package in packages:
        if install_package(package):
            successful_installs += 1
        else:
            failed_installs += 1

    print(f"\nInstallation Summary:")
    print(f"Successful installs: {successful_installs}")
    print(f"Failed installs: {failed_installs}")

if __name__ == "__main__":
    main()