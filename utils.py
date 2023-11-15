from datetime import datetime
from pathlib import Path
import pandas as pd

def create_file(name: str) -> str:
    default_time_string = datetime.now().strftime("%y-%m-%d--%H-%M-%S")
    name = name if name else f"{default_time_string}.xlsx"
    filePath = Path(name)
    filePath.touch(exist_ok=True)
    return filePath

def to_path(path: str) -> Path:
    return Path(path)

def read_cad_nums(name: str) -> list[str]:
    df = pd.read_excel(name)
    return list(df.iloc[:, 1].values)

def write_data(path: str, data: list[list]) -> None:
    df = pd.DataFrame(data=data[1:], columns=data[0])
    writer = pd.ExcelWriter(path)
    df.to_excel(writer, sheet_name='Data', index=False)
    writer.close()
    