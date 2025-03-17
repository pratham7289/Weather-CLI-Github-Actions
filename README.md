Weather CLI Tool - Build and Release Workflow
This repository contains a Weather CLI tool and a GitHub Actions workflow to automate building and releasing the tool. The workflow supports pre-releases for the dev branch and stable releases for the main branch.

Workflow Overview
The workflow is defined in .github/workflows/build.yml and performs the following tasks:

Build the Binary:

The workflow builds the Weather CLI tool using PyInstaller to create a single executable binary.

The binary is named differently for dev and main branches to distinguish between pre-releases and stable releases.

Create GitHub Releases:

For the dev branch, the workflow creates a pre-release with a version tag like v1.0.0-dev-{BUILD_NUMBER}.

For the main branch, the workflow creates a stable release with a version tag like v1.0.0-{BUILD_NUMBER}.

Artifact Management:

The built binary is uploaded as a workflow artifact during the build process.

The binary is then downloaded and attached to the GitHub release.

Workflow Steps
1. Build Job:
Runs on a self-hosted runner.

Checks out the code.

Installs Python dependencies (requests and PyInstaller).

Installs the GitHub CLI (gh) for managing releases.

Builds the binary using PyInstaller and sets outputs for:

Binary name (binary_name).

Release tag (release_tag).

Dev build number (dev_build_number).

Uploads the binary as a workflow artifact.

2. Release Job:
Runs on a GitHub-hosted runner.

Checks out the code.

Installs the GitHub CLI (gh).

Downloads the built binary artifact.

Creates a GitHub release:

Pre-release for the dev branch.

Stable release for the main branch.

How to Use the Workflow
1. Start Working on a Feature Branch
Create and switch to a new feature branch:

bash
Copy
git checkout -b feature
Make your changes and update the workflow file (if needed).

2. Replace the Old Workflow with the New Code
Add the updated workflow file:

bash
Copy
git add .github/workflows/build.yml
Commit the changes:

bash
Copy
git commit -m "Updated workflow for proper dev and main releases"
Push the feature branch to GitHub:

bash
Copy
git push origin feature
3. Merge Feature into dev for Testing
Switch to the dev branch:

bash
Copy
git checkout dev
Pull the latest changes:

bash
Copy
git pull origin dev
Merge the feature branch into dev:

bash
Copy
git merge feature
Push the changes to GitHub:

bash
Copy
git push origin dev
The workflow will automatically trigger and create a pre-release for testing.

4. Merge dev into main for Stable Release
After testing the pre-release, switch to the main branch:

bash
Copy
git checkout main
Pull the latest changes:

bash
Copy
git pull origin main
Merge the dev branch into main:

bash
Copy
git merge dev
Push the changes to GitHub:

bash
Copy
git push origin main
The workflow will automatically trigger and create a stable release.

Workflow Triggers
The workflow is triggered on pushes to the following branches:

dev: Creates a pre-release.

main: Creates a stable release.

Artifacts and Releases
Pre-Releases:

Created from the dev branch.

Tag format: v1.0.0-dev-{BUILD_NUMBER}.

Example: v1.0.0-dev-5.

Stable Releases:

Created from the main branch.

Tag format: v1.0.0-{BUILD_NUMBER}.

Example: v1.0.0-10.

Artifacts:

The built binary is uploaded as a workflow artifact during the build process.

The binary is attached to the GitHub release.

Example Workflow Run
Push to dev:

A pre-release is created with a binary named dev-bin-{BUILD_NUMBER}.

Push to main:

A stable release is created with a binary named main-bin-{BUILD_NUMBER}-from-dev-{DEV_BUILD_NUMBER}.

Requirements
GitHub CLI (gh):

The workflow uses the GitHub CLI to create releases. Ensure the CLI is installed on the runner.

Self-Hosted Runner:

The build job runs on a self-hosted runner. Ensure the runner is properly configured with Python and other dependencies.
