import subprocess

def install_package(package_name):
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")

def main():
    packages = [
        "awscli", "bash", "bat", "cmake", "colordiff", "ctags", "docker-compose",
        "docker-machine", "git", "git-flow-avh", "go", "grep", "helm", "hub", "jq",
        "nmap", "node", "nvm", "pkg-config", "postgresql", "prettier", "rbenv", "redis",
        "rename", "ripgrep", "rsync", "ruby", "ruby-build", "ruby-install", "ssh-copy-id",
        "terraform", "thefuck", "vim", "wdiff", "wget", "yarn", "zlib"
        # Add more package names here
    ]

    for package in packages:
        install_package(package)

if __name__ == "__main__":
    main()
