import pandas as pd
import numpy as np
from collections import Counter
from typing import List


def get_nb_occurrences_of_combination_in_df(df: pd.DataFrame,
                                            combination_of_columns: List,
                                            column_of_occurences:str = "occurrences_of_combination"):
    """

    :param df:
    :param combination_of_columns: define list of columns
    :param column_of_occurences:
    :return:
    """

    df_copy = df.copy()
    df_copy[column_of_occurences] = None
    columns_to_check = combination_of_columns
    checked_combinations = list()

    for j, row in df_copy.iterrows():
        row_values = frozenset(row[columns_to_check].values)
        if row_values in checked_combinations:
            checked_combinations.append(row_values)
            c = Counter(checked_combinations)
            nb_of_occurrences = c[row_values]
            df_copy.loc[j, "occurrences_of_combination"] = f'occurrence number {nb_of_occurrences}'
            continue
        df_copy.loc[j, "occurrences_of_combination"] = 'first occurrence'
        checked_combinations.append(row_values)

    return df_copy


if __name__ == "__main__":
    # initialise data of lists.
    data = {'col1': ['a', '2', '3', 'a', 'c', '3', 'a','Teo', 'does not', 'use Jupyter','4'],
            'col2': ['3', 'a', 'a', '2', '4', 'a', '3', 'Jupyter', 'should', 'be illegal','c']}

    # Create DataFrame
    df = pd.DataFrame(data)
    print(df)
    cols_to_check = ['col1', 'col2']

    df_out = get_nb_occurrences_of_combination_in_df(df, cols_to_check)

    print(df_out)

    df_project = pd.read_csv("combinations.csv")

    print(df_project.columns)
    columns = ['geoma_nnid', 'geomb_nnid']
    df_out = get_nb_occurrences_of_combination_in_df(df_project, columns)
    df_out.to_csv("outputs.csv", index=False)
