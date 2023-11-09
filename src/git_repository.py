class GitRepository:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.current_branch = None
        self.remote_info = None

    def get_status(self):
        pass

    def fetch_commits(self):
        pass

    def checkout_branch(self, branch_name):
        pass

    def merge_branch(self, target_branch):
        pass