import os


def flush_cache():
    """
    Deletes all files with the `.pickle` extension in the given directory.
    """
    directory = '../data/'
    for filename in os.listdir(directory):
        if filename.endswith(".pickle"):
            os.remove(os.path.join(directory, filename))
