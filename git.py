import subprocess


def git_mv(file_src, file_dst, cwd="."):
    subprocess.run(["git", "mv", file_src, file_dst], cwd=cwd)


def git_reset(hard=False, cwd="."):
    if hard:
        subprocess.run(["git", "reset", "--hard"], cwd=cwd)
    else:
        subprocess.run(["git", "reset"], cwd=cwd)
