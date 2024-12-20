from os.path import realpath, isabs, exists
from os import remove

class FilePath:
    def __init__(self, path: str):
        self.path = path
        if not isinstance(self.path, str):
            raise ValueError(f"Invalid path: {self.path}. Path must be a string.")
        if not isabs(self.path):
            self.path = realpath(self.path)
        if not exists(self.path):
            raise FileNotFoundError(f"File does not exist: {self.path}")

    def delete(self):
        """
        Deletes the file at the specified path.
        """
        try:
            remove(self.path)
        except Exception:
            pass
            
    def __str__(self):
        return self.path
