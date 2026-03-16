

# Github AI

This repository provides a setup to automatically go through the entire Git

add, commit, push, merge, and pull process with aicommit and github-cli.

---

## Manual Setup

```
# Your API Key for your LLM provider (e.g., OpenAI, Anthropic, or a self-hosted
# instance).
echo 'export AI_TOKEN="your_api_key_goes_here"' >> ~/.bashrc

# The exact model identifier you want to use (e.g., gpt-4o, claude-3-5-sonnet,
# or llama3).
echo 'export AI_NAME="your_llm_name_goes_here"' >> ~/.bashrc

# The base URL for the API. For standard providers, use their official URL;
# for local gateways, use your local IP.
echo 'export AI_ENDPOINT="your_api_endpoint_url_goes_here"' >> ~/.bashrc

# A GitHub Personal Access Token (Classic). Required for the CLI to automate
# pushes and merges.
echo 'export GH_TOKEN="your_github_classic_token_goes_here"' >> ~/.bashrc
```

---

## Installation

```
sudo pacman -S github-cli rust --noconfirm && \
cargo install aicommit && \
git clone https://github.com/devbyte1328/github-ai && \
cd github-ai && \
python Setup.py && \
cd .. && \
rm -rf github-ai && \
source ~/.bashrc
```

---

## Usage

AI commit message generation:
```
aicommit
```

Push new branch with last commit message:
```
aipush
```

The entire Git process:
```
aigit
```


