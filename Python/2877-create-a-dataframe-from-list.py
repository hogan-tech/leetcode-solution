from typing import List
import pandas as pd


def createDataframe(studentData: List[List[int]]) -> pd.DataFrame:
    header = ['student_id', 'age']
    df = pd.DataFrame(studentData, columns=header)
    return df


studentData = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
print(createDataframe(studentData))
