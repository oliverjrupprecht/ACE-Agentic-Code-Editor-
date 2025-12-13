from functions.get_files_info import get_files_info

print(f"test 1: {get_files_info("calculator", ".")}")
print(f"test 2: {get_files_info("calculator", "pkg")}")
print(f"test 3: {get_files_info("calculator", "/bin")}")
print(f"test 4: {get_files_info("calculator", "../")}")
