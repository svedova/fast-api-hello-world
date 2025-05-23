# Go Hello World Example

This repository contains a simple "Hello World" application written in FastAPI. Follow the steps below to build and deploy the project.

## Prerequisits

Before you begin, ensure you have the following installed on your system:

- **Python** (version 3.7 or higher): [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer): Comes bundled with Python, but you can verify by running `pip --version`.
- **Git**: [Download Git](https://git-scm.com/downloads)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fast-api-hello-world.git
   cd fast-api-hello-world
   ```

2. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:

   ```bash
   PORT=3000 python main.py
   ```

## ⚡️ Deployment with Stormkit

1. Login to your self-hosted Stormkit Instance. Here's [a guide](https://www.stormkit.io/tutorials/how-to-self-host-stormkit-on-hetzner-cloud) to set it up.
2. Import this project from URL
3. Configure the Server Settings:
   - Start command: `python main.go`
4. Click Save and Deploy

Note: Make sure `mise.toml` is present so that dependencies are installed automatically and that the server listens on the `PORT` environment variable.

- 🛠️ [Setup Stormkit on Hetzner](https://www.stormkit.io/tutorials/how-to-self-host-stormkit-on-hetzner-cloud)
- 📑 [Stormkit documentation](https://www.stormkit.io/docs/welcome/getting-started)
- 🌞 [Stormkit changelog](https://www.stormkit.io/blog/whats-new)
