import os
import subprocess

def is_installed(package, is_cask=False):
    list_command = ['brew', 'list', '--cask'] if is_cask else ['brew', 'list', '--formula']
    result = subprocess.run(list_command, capture_output=True, text=True)
    return package in result.stdout

def main():
    brewfile_path = "Brewfile"  # Path to the Brewfile
    to_uninstall = []

    if not os.path.exists(brewfile_path):
        print(f"Brewfile not found at {brewfile_path}")
        return

    # First pass: Determine what needs to be uninstalled
    with open(brewfile_path, 'r') as file:
        for line in file:
            if line.startswith(('brew install', 'cask install')):
                parts = line.split()
                command = parts[0]  # brew or cask
                target = ' '.join(parts[2:]).split('#')[0].strip().strip('"')
                is_cask = command == 'cask'

                if is_installed(target, is_cask=is_cask):
                    to_uninstall.append((command, target, is_cask))

    # Summary and user choice
    print(f"\nItems to uninstall: {len(to_uninstall)}")
    for _, target, _ in to_uninstall:
        print(f"  - {target}")

    choice = input("\nDo you want to uninstall 1. all at once, 2. individually, or 3. cancel? (1/2/3): ").strip().lower()

    # Uninstallation process
    if choice == '1':
        for command, target, is_cask in to_uninstall:
            subprocess.run(['brew', 'uninstall', '--cask' if is_cask else '--formula', target])
        print(f"All items have been uninstalled.")
    elif choice == '2':
        for command, target, is_cask in to_uninstall:
            user_choice = input(f"Do you want to uninstall {target}? (y/n): ").strip().lower()
            if user_choice == 'y':
                subprocess.run(['brew', 'uninstall', '--cask' if is_cask else '--formula', target])
                print(f"{target} has been uninstalled.")
            else:
                print(f"Skipping {target}")
    elif choice == '3':
        print("Uninstallation process canceled.")

if __name__ == "__main__":
    main()
