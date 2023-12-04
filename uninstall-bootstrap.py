import os
import subprocess

def is_installed(package, is_cask=False):
    list_command = ['brew', 'list', '--cask'] if is_cask else ['brew', 'list', '--formula']
    result = subprocess.run(list_command, capture_output=True, text=True)
    return package in result.stdout

def main():
    brewfile_path = "Brewfile"  # Path to the Brewfile
    uninstalled_count = 0

    if not os.path.exists(brewfile_path):
        print(f"Brewfile not found at {brewfile_path}")
        return

    with open(brewfile_path, 'r') as file:
        for line in file:
            if line.startswith(('brew install', 'cask install')):
                parts = line.split()
                command = parts[0]  # brew or cask
                target = ' '.join(parts[2:]).split('#')[0].strip().strip('"')
                is_cask = command == 'cask'

                if is_installed(target, is_cask=is_cask):
                    print(f"Installed: {command} {target}")
                    choice = input("Do you want to uninstall or skip this item? (u/skip): ").strip().lower()

                    if choice == 'u':
                        uninstall_command = ['brew', 'uninstall', '--cask' if is_cask else '--formula', target]
                        subprocess.run(uninstall_command)
                        uninstalled_count += 1
                    elif choice == 'skip':
                        print(f"Skipping {command} {target}")
                    else:
                        print(f"Invalid response. Skipping {command} {target}")
                else:
                    print(f"Not installed or not applicable: {command} {target}")

    print(f"\nSummary: {uninstalled_count} items were successfully uninstalled.")

if __name__ == "__main__":
    main()
