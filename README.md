# Weather CLI Tool

A command-line interface tool that retrieves real-time weather information using public weather APIs.

## Overview

The Weather CLI Tool is designed to provide users with quick access to current weather data directly from their terminal. It connects to public weather APIs (such as OpenWeatherMap) to fetch temperature, humidity, weather conditions, and other relevant meteorological data for any specified city worldwide. The application is built with Python, packaged into a standalone executable, and deployed through an automated CI/CD pipeline.

## Features

- **Real-time Weather Data**: Fetches current weather conditions for any city
- **Simple Interface**: Easy-to-use command-line arguments
- **Metric/Imperial Support**: Choose your preferred unit system
- **Standalone Binary**: No dependencies required to run the packaged application
- **Regular Updates**: Automated build and release pipeline ensures the latest version is always available

## Usage

The tool accepts several command-line arguments to customize the weather data retrieval:

```bash
# Get weather by city name
./weather --city "San Francisco"

# Get weather with specified units
./weather --city "Chicago" --units imperial

# Get detailed weather information
./weather --city "Tokyo" --detailed
```

## CI/CD Pipeline

This project uses GitHub Actions to automate the build and release process with separate pipelines for development and production releases.

### Workflow Features

- **Automated Builds**: Triggered automatically on pushes to `dev` and `main` branches
- **Versioning System**: 
  - Development builds: `v1.0.0-dev-{BUILD_NUMBER}`
  - Production builds: `v1.0.0-{BUILD_NUMBER}`
- **Build Tracking**: Production releases reference which development build they originated from
- **Self-hosted Runners**: Build job runs on self-hosted runners for controlled environments
- **Binary Distribution**: Executables are available as GitHub Releases

### CI/CD Pipeline Details

1. **Build Process**:
   - Uses PyInstaller to package the Python script into a standalone executable
   - Runs on self-hosted runners, giving you control over the build environment
   - Creates uniquely named binaries that include build numbers for tracking

2. **Build Naming System**:
   - Dev builds: `dev-bin-{BUILD_NUMBER}`
   - Main builds: `main-bin-{BUILD_NUMBER}-from-dev-{DEV_BUILD}`
   - This naming system ensures traceability between dev and production releases

3. **Release Automation**:
   - Creates GitHub releases automatically
   - Dev builds are marked as pre-releases with appropriate documentation
   - Main builds are marked as stable releases and reference their source dev build

### Release Process

1. Development work happens on feature branches
2. Feature branches are merged into `dev` for testing
3. Merges to `dev` trigger automatic pre-release builds
4. After testing, `dev` is merged into `main`
5. Merges to `main` trigger automatic stable release builds

## Deployment Environment

### RHEL VM Setup

The tool is deployed to a Red Hat Enterprise Linux (RHEL) VM:

1. VM created in a hypervisor (VirtualBox, VMware) with RHEL
2. Minimal installation performed to reduce resource usage
3. Networking configured to allow SSH access

Alternatives:
- Ubuntu or CentOS if RHEL is not available
- Cloud provider (AWS, Azure) VM instances

### SSH Configuration

The deployment process relies on secure SSH access to the target server:

1. OpenSSH Server installed and configured on the VM
2. SSH service enabled to start automatically on boot
3. Firewall configured to allow SSH connections
4. SSH configured for key-based authentication only

### SSH Key Authentication

For secure, passwordless deployment:

1. SSH key pair generated on the deployment machine
2. Public key copied to the server's authorized keys
3. Proper permissions set on SSH directories and files
4. Password authentication disabled for enhanced security

## Self-Hosted Runner Setup

For security and proper isolation, a dedicated user is used for the GitHub Actions runner:

1. A specific `github-runner` user created on the server
2. GitHub Actions runner software installed under this user
3. Runner configured to connect to the repository
4. Runner service set up to start automatically

Benefits of this approach:
- Limits runner permissions to only what is necessary
- Prevents interference with other system processes
- Follows the principle of least privilege for security

## GitHub Repository Setup

### Creating the Repository

The project is hosted on GitHub for version control and CI/CD integration:

1. Repository created on GitHub to host the source code
2. Local development repository connected to GitHub remote
3. Branch protection rules established for `dev` and `main` branches

### GitHub Secrets

To securely store deployment credentials:

1. Server connection details stored as GitHub Secrets
2. SSH private key securely stored for deployment access
3. API keys and other sensitive information protected

## External Dependencies

### Weather API

The tool relies on external weather APIs to function:

1. OpenWeatherMap API (primary)
2. Alternative options:
   - Weatherstack API
   - AccuWeather API
   - National Weather Service API (US only)

### Development Dependencies

- Python 3.9+
- Requests library for API calls
- PyInstaller for binary packaging

## Installation

### From Releases

Download the appropriate binary for your system from the [Releases](../../releases) page:

1. **Development Builds**: Pre-release versions for testing new features
2. **Stable Builds**: Production-ready versions for reliable use

### From Source

To build from source:

1. Clone the repository
2. Install the required dependencies
3. Run PyInstaller to create your own binary
4. (Optional) Configure for your preferred weather API

## Configuration

Before using the tool, you need to:

1. Obtain an API key from your chosen weather service
2. Configure the tool to use your API key
3. (Optional) Set default preferences for units and output format

## Contributing

We welcome contributions to improve the Weather CLI Tool:

1. Fork the repository
2. Create a feature branch from `dev`
3. Make your changes and commit
4. Push your feature branch and create a pull request to `dev`
5. After testing on `dev`, changes will be merged to `main`

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Include appropriate error handling
- Add useful comments for complex functionality
- Test thoroughly before submitting pull requests

## Security Considerations

The project implements several security best practices:

- GitHub's secure token system for authentication
- SSH key-based authentication for deployment
- Self-hosted runner under a dedicated user (not root)
- Sensitive information stored as GitHub Secrets
- Regular updates to dependencies to address vulnerabilities

## Troubleshooting

Common issues and solutions:

1. **API Rate Limiting**: Weather APIs often have request limits; implement caching if needed
2. **Network Connectivity**: Ensure proper internet access on the deployment server
3. **Permission Issues**: Check file and directory permissions if deployment fails
4. **API Key Validation**: Verify your API key is active and correctly configured
