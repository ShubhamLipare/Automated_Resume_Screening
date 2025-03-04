import os
from pathlib import Path


folder_list =[
    f"src/__init__.py",
    f"src/data_ingestion/__init__.py",
    f"src/data_ingestion/injest.py",
    f"src/data_transformation/__init__.py",
    f"src/data_transformation/transform.py",
    f"src/model/__init__.py",
    f"src/model/train.py",
    f"src/model/predict.py",
    f"src/logger.py",
    f"src/exception.py",
    f"src/utils.py",
    f"ui/__init__.py",
    f"ui/app.py",
    f"requirements.txt",
    f"api/__init__.py",
    f"api/api.py",
    f"main.py",
]


for path in folder_list:
    path=Path(path)

    file_dir,filename=os.path.split(path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)

    if not (os.path.exists(path)) or os.path.getsize(path)==0:
        path.touch()
    else:
        print(f"{path} already exists")

