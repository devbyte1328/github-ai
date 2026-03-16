from Standards.Python import *
from Standards.OS import *
from Standards.SubProcess import *


PATH_OF_HOME_USER = OS_return_path_of_home_user()
DIRECTORY_PATH_OF_GITHUB_AI = f"{PATH_OF_HOME_USER}/.github_ai"
DIRECTORY_PATH_OF_STANDARDS = f"{PATH_OF_HOME_USER}/.github_ai/Standards"
FILE_PATH_OF_BASHRC_SCRIPT = f"{PATH_OF_HOME_USER}/.bashrc"


if OS_return_boolean_directory(DIRECTORY_PATH_OF_GITHUB_AI) == False:
    OS_initialize_directory(DIRECTORY_PATH_OF_GITHUB_AI)
if OS_return_boolean_directory(DIRECTORY_PATH_OF_STANDARDS) == False:
    OS_initialize_directory(DIRECTORY_PATH_OF_STANDARDS)
bashrc_script = ""
if OS_return_boolean_filesystem(FILE_PATH_OF_BASHRC_SCRIPT) == True:
    bashrc_script = Python_read_file(FILE_PATH_OF_BASHRC_SCRIPT)
bashrc_cargo_path = "export PATH=\"$HOME/.cargo/bin:$PATH\""
if bashrc_cargo_path not in bashrc_script:
    Python_write_file(FILE_PATH_OF_BASHRC_SCRIPT, bashrc_cargo_path)
aicommit_config_function = Python_fstring(f"""
aicommit --add-provider --add-openai-compatible --openai-compatible-api-key
''''''
 \"{$AI_TOKEN}\" --openai-compatible-api-url \"{$AI_ENDPOINT}\"
''''''
 --openai-compatible-model \"{$AI_LLM_NAME}\"
""")
SubProcess_initialize(aicommit_config_function)
SubProcess_initialize(f"cp STANDARDS.md ~/.github_ai/STANDARDS.md")
SubProcess_initialize(f"cp Python.py ~/.github_ai/Python.py")
SubProcess_initialize(f"cp SubProcess.py ~/.github_ai/SubProcess.py")
SubProcess_initialize(f"cp aipush.py ~/.github_ai/aipush.py")
bashrc_aipush_function = Python_fstring(f"""

aipush() {{
    python ~/.github_ai/aipush.py "$1"
}}


""")
if "aipush()" not in bashrc_script:
    Python_write_file(PATH_OF_BASHRC_SCRIPT, bashrc_aipush_function)
bashrc_aigit_function = Python_fstring(f"""

aigit() {
    git add . && \
    aicommit && \
    aipush && \
    gh pr merge --merge --delete-branch && \
    git checkout main && \
    git pull && \
    git branch | xargs git branch -D && \
    git restore . && \
    git clean -fd
}

""")
if "aipush()" not in bashrc_script:
    Python_write_file(PATH_OF_BASHRC_SCRIPT, bashrc_aigit_function)

