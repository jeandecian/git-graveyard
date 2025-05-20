import os
import subprocess

WORKSPACE_DIR = "/path/to/your/workspace"


def get_git_repositories(workspace_dir):
    git_repos = []

    for root, dirs, files in os.walk(workspace_dir):
        if ".git" in dirs:
            git_repos.append(root)
            dirs.remove(".git")

    return git_repos


def get_remote_url(repo_path):
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        return None


def get_owner_and_repo_name(remote_url):
    owner, repo_name = None, None

    if remote_url.startswith("git@"):
        owner_repo_name = remote_url.split(":")[1]
        owner, repo_name = owner_repo_name.split("/")
        repo_name = repo_name.replace(".git", "")

    elif remote_url.startswith("https://"):
        owner, repo_name = remote_url.split("/")[-2:]
        repo_name = repo_name.replace(".git", "")

    return owner, repo_name


print(f"[INFO] Scanning workspace directory: {WORKSPACE_DIR}")

git_repositories = get_git_repositories(WORKSPACE_DIR)

total_repos = len(git_repositories)
print(f"[INFO] Found {total_repos} git repositories in the workspace directory.")

for index, repo in enumerate(git_repositories):
    print(f"[INFO] Repository {index + 1}/{total_repos}: {repo}")

    remote_url = get_remote_url(repo)
    if remote_url:
        print(f"[INFO] Remote URL: {remote_url}")
    else:
        print(f"[ERROR] No remote URL found for {repo}")
        continue

    owner, repo_name = get_owner_and_repo_name(remote_url)
    if owner and repo_name:
        print(f"[INFO] Owner: {owner}, Repository Name: {repo_name}")
    else:
        print(
            f"[ERROR] Unable to parse owner and repository name from URL: {remote_url}"
        )

print(f"[INFO] Finished scanning workspace directory.")
