import os

WORKSPACE_DIR = "/path/to/your/workspace"


def get_git_repositories(workspace_dir):
    git_repos = []

    for root, dirs, files in os.walk(workspace_dir):
        if ".git" in dirs:
            git_repos.append(root)
            dirs.remove(".git")

    return git_repos


print(f"[INFO] Scanning workspace directory: {WORKSPACE_DIR}")

git_repositories = get_git_repositories(WORKSPACE_DIR)

total_repos = len(git_repositories)
print(f"[INFO] Found {total_repos} git repositories in the workspace directory.")

for index, repo in enumerate(git_repositories):
    print(f"[INFO] Repository {index + 1}/{total_repos}: {repo}")

print(f"[INFO] Finished scanning workspace directory.")
