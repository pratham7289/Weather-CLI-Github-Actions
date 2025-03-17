Weather CLI Tool - Build & Release Automation
This repository contains a Python-based Weather CLI Tool. The development and release process is fully automated using GitHub Actions, supporting both development and production builds.

🚀 Features
Automatic binary builds on dev and main branches.
Pre-release generation for dev branch.
Stable release generation for main branch.
Versioning and tagging based on GitHub Action's run number.
Artifacts upload for each build.
GitHub Releases publishing with appropriate tags.
📦 Branching & Release Workflow
Branch	Purpose	Output
feature	Development of new features	Merged into dev for testing
dev	Integration and testing of features	Pre-release uploaded to GitHub Releases
main	Production-ready code	Stable release uploaded to GitHub Releases
🔧 Build & Release Process
1. Feature Development
bash
Copy
Edit
git checkout feature
# Make changes and commit
git push origin feature
2. Merge Feature to Dev (Pre-release)
bash
Copy
Edit
git checkout dev
git pull origin dev
git merge feature
git push origin dev
⚙️ Triggers build and pre-release creation.
Binary named as dev-bin-<build_number>.
Tag format: v1.0.0-dev-<build_number>.
3. Merge Dev to Main (Stable Release)
bash
Copy
Edit
git checkout main
git pull origin main
git merge dev
git push origin main
⚙️ Triggers build and stable release creation.
Binary named as main-bin-<build_number>-from-dev-<dev_build_number>.
Tag format: v1.0.0-<build_number>.
📤 GitHub Releases Structure
Branch	Release Type	Tag Example	Binary Example
dev	Pre-release	v1.0.0-dev-42	dev-bin-42
main	Stable release	v1.0.0-43	main-bin-43-from-dev-42
🔑 Security & Authentication
Uses GitHub Token (GITHUB_TOKEN) for authentication.
No password required for build or release processes.
