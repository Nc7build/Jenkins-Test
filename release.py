import os
import errno
import shutil
import subprocess
import time

def create_empty_dir(dir_name):
    # Delete directory if it exists, then recreate
    try:
        shutil.rmtree(dir_name)
    except OSError as e:
        if e.errno == errno.ENOENT:
            # directory does not exist
            pass
        else:
            raise
    time.sleep(.1)  # Directory may not be deleted by Windows when shutil.rmtree returns
    os.mkdir(dir_name)

if __name__ == '__main__':
	git_hash = subprocess.check_output(["git", "describe", "--abbrev=8", "--always", "--dirty"]).strip().split('\n')[0]
	create_empty_dir(git_hash)
	shutil.copy('README.MD', git_hash)
	print git_hash
	