import subprocess

def install_package(package_name):
    print(f"Installing {package_name}...")
    try:
        subprocess.run(["sudo", "yum", "install", "-y", package_name], check=True)
        print(f"Successfully installed {package_name}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")
        return False

def main():
    with open('centos-packages.txt', 'r') as f:
        packages = [line.strip() for line in f]

    successful_installs = []
    failed_installs = []

    for package in packages:
        if install_package(package):
            successful_installs.append(package)
        else:
            failed_installs.append(package)

    print(f"\nInstallation Summary:")
    print(f"Successful installs: {len(successful_installs)}")
    print(f"Failed installs: {len(failed_installs)}")

    if successful_installs:
        print("\nSuccessful Installations:")
        for package in successful_installs:
            print(package)

    if failed_installs:
        print("\nFailed Installations:")
        for package in failed_installs:
            print(package)

if __name__ == "__main__":
    main()
