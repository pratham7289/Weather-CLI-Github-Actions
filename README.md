Weather CLI Tool
A command-line interface tool that retrieves real-time weather information using public weather APIs.
Overview
The Weather CLI Tool is designed to provide users with quick access to current weather data directly from their terminal. It connects to public weather APIs (such as OpenWeatherMap) to fetch temperature, humidity, weather conditions, and other relevant meteorological data for any specified city worldwide. The application is built with Python, packaged into a standalone executable, and deployed through an automated CI/CD pipeline.
Features

Real-time Weather Data: Fetches current weather conditions for any city
Simple Interface: Easy-to-use command-line arguments
Metric/Imperial Support: Choose your preferred unit system
Standalone Binary: No dependencies required to run the packaged application
Regular Updates: Automated build and release pipeline ensures the latest version is always available

Usage
The tool accepts several command-line arguments to customize the weather data retrieval:
bashCopy# Get weather by city name
./weather --city "San Francisco"

# Get weather with specified units
./weather --city "Chicago" --units imperial

# Get detailed weather information
./weather --city "Tokyo" --detailed
CI/CD Pipeline
This project uses GitHub Actions to automate the build and release process with separate pipelines for development and production releases.
Workflow Features

Automated Builds: Triggered automatically on pushes to dev and main branches
Versioning System:

Development builds: v1.0.0-dev-{BUILD_NUMBER}
Production builds: v1.0.0-{BUILD_NUMBER}


Build Tracking: Production releases reference which development build they originated from
Self-hosted Runners: Build job runs on self-hosted runners for controlled environments
Binary Distribution: Executables are available as GitHub Releases

CI/CD Pipeline Details

Build Process:

Uses PyInstaller to package the Python script into a standalone executable
Runs on self-hosted runners, giving you control over the build environment
Creates uniquely named binaries that include build numbers for tracking


Build Naming System:

Dev builds: dev-bin-{BUILD_NUMBER}
Main builds: main-bin-{BUILD_NUMBER}-from-dev-{DEV_BUILD}
This naming system ensures traceability between dev and production releases


Release Automation:

Creates GitHub releases automatically
Dev builds are marked as pre-releases with appropriate documentation
Main builds are marked as stable releases and reference their source dev build



Release Process

Development work happens on feature branches
Feature branches are merged into dev for testing
Merges to dev trigger automatic pre-release builds
After testing, dev is merged into main
Merges to main trigger automatic stable release builds

Deployment Environment
RHEL VM Setup
The tool is deployed to a Red Hat Enterprise Linux (RHEL) VM:

VM created in a hypervisor (VirtualBox, VMware) with RHEL
Minimal installation performed to reduce resource usage
Networking configured to allow SSH access

Alternatives:

Ubuntu or CentOS if RHEL is not available
Cloud provider (AWS, Azure) VM instances

SSH Configuration
The deployment process relies on secure SSH access to the target server:

OpenSSH Server installed and configured on the VM
SSH service enabled to start automatically on boot
Firewall configured to allow SSH connections
SSH configured for key-based authentication only

SSH Key Authentication
For secure, passwordless deployment:

SSH key pair generated on the deployment machine
Public key copied to the server's authorized keys
Proper permissions set on SSH directories and files
Password authentication disabled for enhanced security

Self-Hosted Runner Setup
For security and proper isolation, a dedicated user is used for the GitHub Actions runner:

A specific github-runner user created on the server
GitHub Actions runner software installed under this user
Runner configured to connect to the repository
Runner service set up to start automatically

Benefits of this approach:

Limits runner permissions to only what is necessary
Prevents interference with other system processes
Follows the principle of least privilege for security

GitHub Repository Setup
Creating the Repository
The project is hosted on GitHub for version control and CI/CD integration:

Repository created on GitHub to host the source code
Local development repository connected to GitHub remote
Branch protection rules established for dev and main branches

GitHub Secrets
To securely store deployment credentials:

Server connection details stored as GitHub Secrets
SSH private key securely stored for deployment access
API keys and other sensitive information protected

External Dependencies
Weather API
The tool relies on external weather APIs to function:

OpenWeatherMap API (primary)
Alternative options:

Weatherstack API
AccuWeather API
National Weather Service API (US only)



Development Dependencies

Python 3.9+
Requests library for API calls
PyInstaller for binary packaging

Installation
From Releases
Download the appropriate binary for your system from the Releases page:

Development Builds: Pre-release versions for testing new features
Stable Builds: Production-ready versions for reliable use

From Source
To build from source:

Clone the repository
Install the required dependencies
Run PyInstaller to create your own binary
(Optional) Configure for your preferred weather API

Configuration
Before using the tool, you need to:

Obtain an API key from your chosen weather service
Configure the tool to use your API key
(Optional) Set default preferences for units and output format

Contributing
We welcome contributions to improve the Weather CLI Tool:

Fork the repository
Create a feature branch from dev
Make your changes and commit
Push your feature branch and create a pull request to dev
After testing on dev, changes will be merged to main

Development Guidelines

Follow PEP 8 style guidelines for Python code
Include appropriate error handling
Add useful comments for complex functionality
Test thoroughly before submitting pull requests

Security Considerations
The project implements several security best practices:

GitHub's secure token system for authentication
SSH key-based authentication for deployment
Self-hosted runner under a dedicated user (not root)
Sensitive information stored as GitHub Secrets
Regular updates to dependencies to address vulnerabilities
