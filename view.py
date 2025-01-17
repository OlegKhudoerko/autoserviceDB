def show_greetings():
    print("Добро пожаловать в меню услуги autoserviceDB!")


def input_client_fio():
    return input("Введите фио клиента\n")


def input_technician_fio():
    return input("Введите фио слесаря\n")


def input_vehicle_model():
    return input("Введите модель транспортного средства\n")


def input_gov_number():
    return input("Введите гос. номер\n")


def input_repairs_start():
    return input("Введите время начала ремонта\n")


def input_repairs_end():
    return input("Введите время окончания ремонта\n")


def show_srvice_menu():
    return input(
        "0 - Выход\n1 - Показать информацию\n2 - Добавить информацию\n3 - Удалить информацию\n")


def show_success():
    print("Успешно выполнено")


def show_result(result):
    print(f"Результат операции: {result}")


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
def show_table(table):
    spans = __count_spans(table)
    __print_row_border(spans)
    __print_table_rows(table, spans)


def show_error(error):
    print(f"Произошла ошибка: {error}")


def show_goodbye():
    print("Вы вышли из программы")


# Takes list of lengths of the columns in symbols
# @ param spans: List<Int>
def __print_row_border(spans):
    print(f"|{'|'.join(list(map(__int_to_span, spans)))}|")


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
# @param spans: List<Int>
def __print_table_rows(table, spans):
    for row in table:
        __print_table_row(row, spans)
        __print_row_border(spans)


# @param row: List<String>
# @param spans: List<Int>
def __print_table_row(row, spans):
    output_row = "|"
    index = 0
    while index < len(row):
        output_row += row[index]
        output_row += (" " * (spans[index] - len(row[index])))
        output_row += "|"
        index += 1
    print(output_row)


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
def __count_spans(table):
    spans = list(map(__map_list_to_spans, table))
    spans_rotated = [list(column) for column in zip(*spans)]
    max_spans = list(map(max, spans_rotated))
    return max_spans


def __int_to_span(num):
    return "-" * num


# @param row: List<String>
def __map_list_to_spans(row):
    return list(map(lambda s: len(s), row))
