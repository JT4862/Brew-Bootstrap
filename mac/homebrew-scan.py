import subprocess

def get_homebrew_packages():
    try:
        result = subprocess.run(['brew', 'list', '--formula'], capture_output=True, text=True, check=True)
        packages = result.stdout.strip().split('\n')
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Error while getting Homebrew packages: {e}")
        return []

def get_homebrew_casks():
    try:
        result = subprocess.run(['brew', 'list', '--cask'], capture_output=True, text=True, check=True)
        casks = result.stdout.strip().split('\n')
        return casks
    except subprocess.CalledProcessError as e:
        print(f"Error while getting Homebrew casks: {e}")
        return []

def get_homebrew_taps():
    try:
        result = subprocess.run(['brew', 'tap'], capture_output=True, text=True, check=True)
        taps = result.stdout.strip().split('\n')
        return taps
    except subprocess.CalledProcessError as e:
        print(f"Error while getting Homebrew taps: {e}")
        return []

def main():
    print("Scanning for Homebrew packages, casks, and taps...\n")

    packages = get_homebrew_packages()
    casks = get_homebrew_casks()
    taps = get_homebrew_taps()

    print("Installed Homebrew Packages:")
    for package in packages:
        print(f"  - {package}")

    print("\nInstalled Homebrew Casks:")
    for cask in casks:
        print(f"  - {cask}")

    print("\nHomebrew Taps:")
    for tap in taps:
        print(f"  - {tap}")

if __name__ == "__main__":
    main()
