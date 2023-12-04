import os
import subprocess

def is_installed(package, is_cask=False):
    list_command = ['brew', 'list', '--cask'] if is_cask else ['brew', 'list', '--formula']
    result = subprocess.run(list_command, capture_output=True, text=True)
    return package in result.stdout

def is_outdated(package):
    result = subprocess.run(['brew', 'outdated', '--formula'], capture_output=True, text=True)
    return package in result.stdout

def main():
    brewfile_path = "Brewfile"  # Path to the Brewfile
    to_install = []
    to_update = []

    if not os.path.exists(brewfile_path):
        print(f"Brewfile not found at {brewfile_path}")
        return

    # First pass: Determine what needs to be installed or updated
    with open(brewfile_path, 'r') as file:
        for line in file:
            if line.startswith(('brew install', 'cask install')):
                parts = line.split()
                command = parts[0]  # brew or cask
                target = ' '.join(parts[2:]).split('#')[0].strip().strip('"')
                is_cask = command == 'cask'

                if not is_installed(target, is_cask=is_cask):
                    to_install.append((command, target, is_cask))
                elif is_outdated(target):
                    to_update.append((command, target, is_cask))

    # Summary and user choice
    print(f"\nItems to install: {len(to_install)}")
    for _, target, _ in to_install:
        print(f"  - {target}")

    print(f"\nItems to update: {len(to_update)}")
    for _, target, _ in to_update:
        print(f"  - {target}")

    choice = input("\nDo you want to install/update 1.all at once, 2.individually, or 3.cancel? (1/2/3): ").strip().lower()

    # Installation process
    if choice == '1':
        for command, target, is_cask in to_install + to_update:
            subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target])
        print(f"All items have been installed or updated.")
    elif choice == '2':
        for command, target, is_cask in to_install + to_update:
            user_choice = input(f"Do you want to install/update {target}? (y/n): ").strip().lower()
            if user_choice == 'y':
                subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target])
                print(f"{target} has been installed or updated.")
            else:
                print(f"Skipping {target}")
    elif choice == '3':
        print("Installation process canceled.")

if __name__ == "__main__":
    main()
