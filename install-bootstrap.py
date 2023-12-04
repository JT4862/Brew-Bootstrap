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

def is_outdated(package, is_cask=False):
    outdated_command = ['brew', 'outdated', '--cask'] if is_cask else ['brew', 'outdated', '--formula']
    try:
        result = subprocess.run(outdated_command, capture_output=True, text=True, check=True)
        return package in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error while checking if {package} is outdated: {e}")
        return False

def extract_target(line):
    if 'brew install --cask' in line or 'cask install' in line:
        return line.split('"')[1], True
    elif 'brew install' in line:
        return line.split('"')[1], False
    return None, False

def main():
    brewfile_path = "Brewfile"  # Path to the Brewfile
    to_install = []
    to_update = []

    if not os.path.exists(brewfile_path):
        print(f"Brewfile not found at {brewfile_path}")
        return

    with open(brewfile_path, 'r') as file:
        for line in file:
            if line.startswith(('brew install', 'brew install --cask')):
                target, is_cask = extract_target(line)
                if target and not is_installed(target, is_cask=is_cask):
                    to_install.append((target, is_cask))
                elif target and is_outdated(target, is_cask=is_cask):
                    to_update.append((target, is_cask))

    print(f"\nItems to install: {len(to_install)}")
    for target, _ in to_install:
        print(f"  - {target}")

    print(f"\nItems to update: {len(to_update)}")
    for target, _ in to_update:
        print(f"  - {target}")

    choice = input("\nDo you want to install/update 1.all at once, 2.individually, or 3.cancel? (1/2/3): ").strip().lower()

    if choice == '1':
        for target, is_cask in to_install + to_update:
            try:
                subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target], check=True)
                print(f"{target} has been installed or updated.")
            except subprocess.CalledProcessError as e:
                print(f"Error while installing/updating {target}: {e}")
    elif choice == '2':
        for target, is_cask in to_install + to_update:
            user_choice = input(f"Do you want to install/update {target}? (y/n): ").strip().lower()
            if user_choice == 'y':
                try:
                    subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target], check=True)
                    print(f"{target} has been installed or updated.")
                except subprocess.CalledProcessError as e:
                    print(f"Error while installing/updating {target}: {e}")
            else:
                print(f"Skipping {target}")
    elif choice == '3':
        print("Installation process canceled.")

if __name__ == "__main__":
    main()
