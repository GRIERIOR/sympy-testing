# Contributing
This file covers guidelines for contribution to this project.

## Pull Requests

### Commits
Use [conventional commit](https://www.conventionalcommits.org/) format for all commits:
```
feat: add new feature
fix: resolve bug
docs: change in documentation
refactor: changed module to happy_module
```

### Branch Naming
Use clear and consistent branch names:

```
feature/<short-description>
fix/<short-description>
refactor/<short-description>
docs/<short-description>
```

### PR Title and Template
PR's title also should obey [conventional commit](https://www.conventionalcommits.org/) format.

A [Pull Request template](../.github/pull_request_template.md) is provided in the repository.  
Please follow it when creating a PR and fill in all relevant sections to make the review process easier.

### PR Size
Pull Requests should be as small and focused as possible.  
Avoid mixing unrelated changes in a single PR.

Large PRs are acceptable only when justified (e.g. major refactor, architectural change), but should still be well described and structured.

## Issues
This repository provides only one issue template - [bug report](../.github/ISSUE_TEMPLATE/bug_report.md) 

Core team members may create issues outside of this template for internal tasks or quick TODOs.  
Such issues should be clearly labeled (e.g. `chore`, `todo`) and kept concise.

As this is a limited scope and finite project, there is no way to request a feature.