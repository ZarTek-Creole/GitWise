UI Improvement Examples for GitWise CLI
=======================================

Usage Guides
------------
1. Checking Repository Status:
   Command: gitwise check
   Guide: Use this command to get a quick status report on your Git repository. It will tell you if you have uncommitted changes, untracked files, or if your branch is ahead of or behind the remote.

2. Getting AI-Based Recommendations:
   Command: gitwise recommend
   Guide: After making changes to your code, run this command to receive AI-based recommendations on commit messages and branch management.

Error Messages
--------------
1. Error: Uncommitted changes present.
   Improved Message: "You have uncommitted changes in the following files: [file list]. Consider committing them before proceeding."

2. Error: Remote repository not found.
   Improved Message: "The remote repository could not be reached. Check your network connection and remote repository URL."

3. Error: Merge conflict detected.
   Improved Message: "A merge conflict has occurred in [file name]. Resolve the conflict manually or use 'gitwise resolve' for guidance."

The improved guides and messages aim to make the user experience more intuitive and user-friendly. They will be incorporated into the actual CLI code to provide real-time assistance to the user.