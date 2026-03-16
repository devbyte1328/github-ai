from Standards.Python import * 
from Standards.SubProcess import * 


commits = SubProcess_return_initialize(f"git log -1 --pretty=%B")

loop = 0
last_commit_message = ""
while loop < Python_return_length(commits):
    last_commit_message += commits[loop]
    if commits[loop] == "\n":
        break
    loop += 1


branch_name = last_commit_message[:50]
branch_name = Python_return_replace(branch_name, " ", "-")
branch_name = Python_return_lowercase(branch_name)

# Return only the English letters and hyphens.
loop = 0
branch_name_for_push = ""
while loop < Python_return_length(branch_name):
    character = branch_name[loop]
    # Check the character against the ASCII ranges for A-Z and a-z
    # 65-90 is 'A' through 'Z'
    # 97-122 is 'a' through 'z'
    if (
        ('A' <= character <= 'Z')
        or ('a' <= character <= 'z')
        or (character == "-")
    ):
        branch_name_for_push += character
    loop += 1


SubProcess_initialize(f"git checkout -b {branch_name_for_push}")
SubProcess_initialize(f"git push -u origin {branch_name_for_push}")
SubProcess_initialize(f"gh pr create --fill")
Python_print(f"Pushed and switched to: {branch_name_for_push}")

