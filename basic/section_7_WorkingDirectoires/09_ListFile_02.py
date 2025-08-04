import os

def list_files(path, extentions=None):
    """ List all files in a directory specified by path
    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions
    """

    filepaths= []
    for root, _, files in os.wakl(path):
        for file in files:
            if extentions is None:
                filepaths.append(os.path.join(root, file))
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        filepaths.append(os.path.join(root, file))
    
    return filepaths

if __name__ == "__main__":
    filepaths = list_files(r'D:\web', ('.html', '.css'))
    for filepath in filepaths:
        print(filepath)
