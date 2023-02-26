import csv
import numpy as np

file = "file_02.csv"
file_to_write_1 = "sortedByOne.txt"
file_to_write_2 = "sortedByTwo.txt"


def sort_data(file_to_read, mode, sort_option):
    with open(file_to_read, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        arr_count = 0
        object_array = np.zeros(4945, dtype={'names': ('index', 'Date', 'Region', 'Thermal Generation Actual (in MU)',
                                                       'Thermal Generation Estimated (in MU)',
                                                       'Nuclear Generation Actual (in MU)',
                                                       'Nuclear Generation Estimated (in MU)',
                                                       'Hydro Generation Actual (in MU)',
                                                       'Hydro Generation Estimated (in MU)'),
                                             'formats': ('i4', 'U10', 'U20', 'U7', 'U7', 'U7', 'U7', 'U7', 'U7')})
        for row in reader:
            object_array[arr_count]['index'] = row['index']
            object_array[arr_count]['Date'] = row['Date']
            object_array[arr_count]['Region'] = row['Region']
            object_array[arr_count]['Thermal Generation Actual (in MU)'] = row['Thermal Generation Actual (in MU)']
            object_array[arr_count]['Thermal Generation Estimated (in MU)'] = row['Thermal Generation Estimated (in MU)']
            object_array[arr_count]['Nuclear Generation Actual (in MU)'] = row['Nuclear Generation Actual (in MU)']
            object_array[arr_count]['Nuclear Generation Estimated (in MU)'] = row['Nuclear Generation Estimated (in MU)']
            object_array[arr_count]['Hydro Generation Actual (in MU)'] = row['Hydro Generation Actual (in MU)']
            object_array[arr_count]['Hydro Generation Estimated (in MU)'] = row['Hydro Generation Estimated (in MU)']
            arr_count += 1

        if mode == "one":
            sort_by_one(object_array, sort_option)
        if mode == "two":
            sort_by_two(object_array, sort_option)


def sort_by_one(data, sorting_mode):
    logs = open(file_to_write_1, "a")
    logs.write("==================================\n")
    logs.write(f"Sort mode: {sorting_mode}\n")
    logs.write("----------------------------------\n")
    logs.close()

    if sorting_mode == "up":
        sorted_array = np.sort(data, axis=0, order='index')
    if sorting_mode == "down":
        sorted_array = data
        sorted_array[::-1].sort(order='index')

    print(sorted_array)
    for row in sorted_array:
        write_in_file(file_to_write_1, row)
    logs = open(file_to_write_1, "a")
    logs.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    logs.close()


def sort_by_two(data, sorting_mode):
    logs = open(file_to_write_2, "a")
    logs.write("==================================\n")
    logs.write(f"Sort mode: {sorting_mode}\n")
    logs.write("----------------------------------\n")
    logs.close()

    if sorting_mode == "up":
        sorted_array = np.sort(data, axis=0, order=['index', 'Region'])
    if sorting_mode == "down":
        sorted_array = data
        sorted_array[::-1].sort(order=['index', 'Region'])

    print(sorted_array)
    for row in sorted_array:
        write_in_file(file_to_write_2, row)
    logs = open(file_to_write_2, "a")
    logs.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    logs.close()


def write_in_file(write_logs, data):
    logs = open(write_logs, "a")
    logs.write(f"{data['index']} {data['Date']} {data['Region']} {data['Thermal Generation Actual (in MU)']}" +
               f"{data['Thermal Generation Estimated (in MU)']} {data['Nuclear Generation Actual (in MU)']}" +
               f"{data['Nuclear Generation Estimated (in MU)']} {data['Hydro Generation Actual (in MU)']}" +
               f"{data['Hydro Generation Estimated (in MU)']}")
    logs.write("\n")
    logs.close()


def clear_logs(write_logs_1, write_logs_2):
    logs1 = open(write_logs_1, "w")
    logs2 = open(write_logs_2, "w")
    logs1.write("")
    logs2.write("")
    logs1.close()
    logs2.close()


clear_logs(file_to_write_1, file_to_write_2)
# Task 1
sort_data(file, "one", "up")
sort_data(file, "one", "down")

# Task 2
sort_data(file, "two", "up")
sort_data(file, "two", "down")