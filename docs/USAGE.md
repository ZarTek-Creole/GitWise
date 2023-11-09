# Usage

GitWise is designed to be easy to use from the command line. Below are some more detailed examples of how to use GitWise.

## Checking Repository Status

To check the status of your repository for any issues that need attention:

```bash
python -m src.main check <path-to-your-repository>
```

This command will provide an overview of the current state of your repository and suggest actions to take.

## Getting AI-based Recommendations

For AI-powered recommendations on how to manage your branches and commits:

```bash
python -m src.main recommend <path-to-your-repository>
```

GitWise will analyze your repository's history and structure, then provide recommendations tailored to your project.

## Quick Start Guide

1. Install GitWise by following the instructions in INSTALL.md.
2. Navigate to your repository's directory in the terminal.
3. Run `python -m src.main check .` to check the status of your repository.
4. Run `python -m src.main recommend .` to get AI-based recommendations.