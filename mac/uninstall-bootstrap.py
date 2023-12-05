import os
import subprocess

def is_installed(package, is_cask=False):
    list_command = ['brew', 'list', '--cask'] if is_cask else ['brew', 'list', '--formula']
    try:
        result = subprocess.run(list_command, capture_output=True, text=True, check=True)
        return package in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error while checking if {package} is installed: {e}")
        return False

def extract_target(line):
    if 'brew install --cask' in line or 'cask install' in line:
        return line.split('"')[1], True
    elif 'brew install' in line:
        return line.split('"')[1], False
    return None, False

def main():
    brewfile_path = "mac/brewfile"  # Path to the Brewfile
    to_uninstall = []

    if not os.path.exists(brewfile_path):
        print(f"Brewfile not found at {brewfile_path}")
        return

    with open(brewfile_path, 'r') as file:
        for line in file:
            if line.startswith(('brew install', 'brew install --cask')):
                target, is_cask = extract_target(line)
                if target and is_installed(target, is_cask=is_cask):
                    to_uninstall.append((target, is_cask))

    print(f"\nItems to uninstall: {len(to_uninstall)}")
    for target, _ in to_uninstall:
        print(f"  - {target}")

    choice = input("\nDo you want to uninstall 1.all at once, 2.individually, or 3.cancel? (1/2/3): ").strip().lower()

    if choice == '1':
        for target, is_cask in to_uninstall:
            try:
                subprocess.run(['brew', 'uninstall', '--cask' if is_cask else '--formula', target], check=True)
                print(f"{target} has been uninstalled.")
            except subprocess.CalledProcessError as e:
                print(f"Error while uninstalling {target}: {e}")
    elif choice == '2':
        for target, is_cask in to_uninstall:
            user_choice = input(f"Do you want to uninstall {target}? (y/n): ").strip().lower()
            if user_choice == 'y':
                try:
                    subprocess.run(['brew', 'uninstall', '--cask' if is_cask else '--formula', target], check=True)
                    print(f"{target} has been uninstalled.")
                except subprocess.CalledProcessError as e:
                    print(f"Error while uninstalling {target}: {e}")
            else:
                print(f"Skipping {target}")
    elif choice == '3':
        print("Uninstallation process canceled.")

if __name__ == "__main__":
    main()
