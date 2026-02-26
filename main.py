import argparse
import csv
import tabulate


def read_csv(dataframe, filename, encoding="utf-8"):
    with open(filename, "r", encoding=encoding) as file:
        reader = csv.DictReader(file)
        if not dataframe:
            index = 0
            dataframe["index"] = []
        else:
            index = dataframe["index"][-1] + 1
        for row in reader:
            for item in row.items():
                if item[0] not in dataframe.keys():
                    dataframe[item[0]] = [item[1]]
                else:
                    dataframe[item[0]].append(item[1])
            dataframe["index"].append(index)
            index += 1
    return dataframe


def group_by(dataframe, group_column):
    group_by_dic = {}
    valid_keys = list(dataframe.keys())[1:]
    valid_keys.remove(group_column)
    for i in range(len(dataframe["index"])):
        if dataframe[group_column][i] not in group_by_dic.keys():
            group_by_dic[dataframe[group_column][i]] = {x: [] for x in valid_keys}
        for key in valid_keys:
            group_by_dic[dataframe[group_column][i]][key].append(dataframe[key][i])
    return group_by_dic


def average(group_by_dataframe, group_column, column):
    # index = 0
    # dataframe = {'index':[], group_column:[], column:[]}
    dataframe = {group_column: [], column: []}
    for key in group_by_dataframe.keys():
        dataframe[group_column].append(key)
        temp_sum = 0
        for value in group_by_dataframe[key][column]:
            temp_sum += float(value)
        dataframe[column].append(temp_sum / len(group_by_dataframe[key][column]))
        # dataframe['index'].append(index)
        # index+=1
    return dataframe


def sort_by(dataframe, column, ascending=False):
    temp_list = []
    col_num = 0
    tmp_dataframe = {x: [] for x in dataframe.keys()}
    for col in dataframe.keys():
        if col != column:
            col_num += 1
        else:
            break
    for x in zip(*dataframe.values()):
        temp_list.append(x)
    temp_list.sort(key=lambda x: x[col_num], reverse=not ascending)
    for row in temp_list:
        for col, value in zip(dataframe.keys(), row):
            tmp_dataframe[col].append(value)
    return tmp_dataframe


def average_report(group_column, filenames, report_type):
    dataframe = {}
    for file in filenames:
        dataframe = read_csv(dataframe=dataframe, filename=file)
    group_by_df = group_by(dataframe=dataframe, group_column=group_column)
    average_df = average(
        group_by_dataframe=group_by_df,
        group_column=group_column,
        column=report_type.split("-")[1],
    )
    average_df = sort_by(dataframe=average_df, column=report_type.split("-")[1])
    return average_df


parser = argparse.ArgumentParser(prog="report", description="Печатает отчёт в консоль")

parser.add_argument(
    "-f",
    "--files",
    nargs="*",
    help="Укажите пути до файлов через пробел, пример: --files ./foo.csv ./bar/bar.csv",
)
parser.add_argument(
    "-r",
    "--report",
    help="Укажите тип отчёта и колонку через тире, пример: --report averag-gdp или --report average-year",
)

args = parser.parse_args()


def main():
    print(
        tabulate.tabulate(
            average_report("country", args.files, args.report),
            headers="keys",
            showindex="always",
            floatfmt=".2f",
        )
    )


if __name__ == "__main__":
    main()
