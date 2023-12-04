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

                if not is_installed(target, is_cask=is_cask) or (is_installed(target, is_cask=is_cask) and is_outdated(target)):
                    to_install.append((command, target, is_cask))

    # Summary and user choice
    print(f"\nThere are {len(to_install)} items to install or update.")
    choice = input("Do you want to install all at once or individually? (a/i): ").strip().lower()

    # Installation process
    if choice == 'a':
        for command, target, is_cask in to_install:
            subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target])
        print(f"All items have been installed or updated.")
    elif choice == 'i':
        for command, target, is_cask in to_install:
            user_choice = input(f"Do you want to install/update {target}? (y/n): ").strip().lower()
            if user_choice == 'y':
                subprocess.run(['brew', 'install', '--cask' if is_cask else '--formula', target])
                print(f"{target} has been installed or updated.")
            else:
                print(f"Skipping {target}")

if __name__ == "__main__":
    main()
