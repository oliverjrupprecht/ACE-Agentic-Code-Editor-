from os import listdir
from os.path import (
        getsize,
        abspath,
        join,
        isfile,
        isdir,
        normpath
        )

# directory variable shoudld be a relative path to the working directory
def get_files_info(working_directory, directory="."):
    full_path = normpath(join(
                abspath(working_directory), 
                directory
                ))

    header_string = f"Result for {("'" + directory + "'") if (directory != ".") else "current" } directory:\n"

    if not full_path.startswith(abspath(working_directory)): 
        return f"{header_string}    Error: Cannot list {directory} as it is outside the permitted working directory"

    if not isdir(full_path):
        return f"{header_string}    Error: {directory} is not a directory"

    try:
        metadata = [] 
        for file in listdir(full_path):
            path = join(full_path, file)
            metadata.append(
                    f"  - {file}: file_size={getsize(path)}, is_dir={isdir(path)}"
                    )
    except Exception as e:
        return f"{header_string}    Error: {e}"

    return f"{header_string}{"\n".join(metadata)}"

