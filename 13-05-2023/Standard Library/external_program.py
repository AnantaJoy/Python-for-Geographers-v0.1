import subprocess

completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(completed)

print("args are: ", completed.args)
print("return code is: ", completed.returncode)
print("stderr is: ", completed.stderr)
print("stdout is: ", completed.stdout)
print("check is: ", completed.check_returncode())
