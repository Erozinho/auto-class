from pathlib import Path
from datetime import datetime as dt

root_dir = Path('auto-class/AULA 20')
file_paths = root_dir.glob('**/*')

for path in file_paths:
    if path.is_file():
        stat = path.stat()
        stat = stat.st_ctime
        date = dt.fromtimestamp(stat)
        date = date.strftime("%d-%m-%Y %H-%M-%S")
        parts = path.parts
        new_name = date + "-" + path.name
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)