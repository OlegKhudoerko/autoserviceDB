import view
import check
import model_common as com
import test_model_view as tmv
#import view_tests as vt
#import model_csv as cs
#import read_write as rw

view.show_greetings()
while True:
    ch = check.input_main()

    match ch:
        case 0:
            view.show_goodbye()
            break
        case 1:
            f_name = 'db/clients.csv'
            show_field_names = []
            table = tmv.view_all(f_name)
            # view.show_table(table)
            print()
            view.show_success()
            print()
        case 2:
            f_name = 'db/clients.csv'
            new_rec_dat = {}
            tbl_field_names = []
            id_name = '0'
            com.create_rec_table(f_name, new_rec_dat, tbl_field_names, id_name)
            # view.show_result(result)
            view.show_success()
        case 3:
            print("Пока это невозможно!")


def perform_data():
    check.data_check(y, m, d)


def perform_reg(reg_num):
    check.reg_num_check(reg_num)


def perform_phone():
    check.phone_check(num)
