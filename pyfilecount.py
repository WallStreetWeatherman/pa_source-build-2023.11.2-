import os

# Hard-coded directory path
dir_path = "C:\\Users\\Nick\\Desktop\\Programming\\python\\stock strats"

def count_py_files(directory):
    """Count the number of .py files in the given directory and its subdirectories."""
    total_count = 0

    for root, dirs, files in os.walk(directory):
        total_count += sum([1 for filename in files if filename.endswith('.py')])
        
    return total_count

if __name__ == "__main__":
    if os.path.exists(dir_path):
        count = count_py_files(dir_path)
        print(f"Total number of .py files in '{dir_path}' and its subdirectories: {count}")
    else:
        print(f"The directory '{dir_path}' does not exist.")
