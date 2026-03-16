

# Github AI

This repository provides a setup to automatically go through the entire Git

add, commit, push, merge, and pull process with aicommit and github-cli.

---

<table width="100%">
<thead>
<tr><th align="left">ℹ️ NOTE</th></tr>
</thead>
<tbody>
<tr><td>
This documentation does not cover how to host an LLM or how to obtain

credentials for cloud-based LLM services, these steps are the responsibility of

the user. The solution works with any OpenAI-compatible API endpoint and

follows the standard OpenAI API specification for request/response formatting

and authentication. In addition, users are responsible for selecting the LLM

model. You should look for the latest and best-performing LLMs. Below are some

useful resources to help you explore, host, or discover local LLMs:

```
https://github.com/ggml-org/llama.cpp
```

```
https://github.com/open-webui/open-webui
```

```
https://huggingface.co/
```

```
https://huggingface.co/TheBloke
```

</td></tr>
</tbody>
</table>

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


