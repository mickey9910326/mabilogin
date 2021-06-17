import time
import subprocess
import csv
import sys
import os

from mabilogin.beanfun import BeanfunClient


class AutoFiller:

    def __init__(self, username, password):
        self.beanfunClient = BeanfunClient()
        self.beanfunClient.login(username, password)
        self.accounts = self.beanfunClient.get_accounts()
        self.beanfunClient.show_accounts()
        self.next_account = None


def open_mabi(username, password, path):
    auto_filler = AutoFiller(username, password)
    print(auto_filler.accounts[0].name)
    print(auto_filler.accounts[0].acc)
    print(auto_filler.accounts[0].sotp)
    otp = auto_filler.beanfunClient.get_account_otp(
        auto_filler.accounts[0])
    print(otp)
    password = otp.split(" ")[-1].replace("\x00", "")
    print(password)

    mabi_path = path + "\\Mabinogi.exe"
    acc = auto_filler.accounts[0].acc
    args = [mabi_path, f"/N:{acc}", f"/V:{password}", "/T:gamania"]
    subprocess.Popen(args=args, cwd=path)


delay_s = 25
main_path = "F:\\Nexon\\Mabinogi"
clone_path = "F:\\Nexon\\Mabinogi_clone"

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("py -m mabilogin [csv filename] [start num] [end num]")
        return

    filename = f'acc/{sys.argv[1]}.csv'
    print(filename)
    if os.path.isfile(filename) == False:
        print(f"csv file {filename} not exist")
        return

    if sys.argv[2].isdigit():
        start = int(sys.argv[2])
    else:
        print("py -m mabilogin [csv filename] [start num] [end num]")
        print("start num should be intger")
        return

    if len(sys.argv) == 3:
        end = start
    elif sys.argv[3].isdigit():
        end = int(sys.argv[3])
    else:
        print("py -m mabilogin [csv filename] [start num] [end num]")
        print("end num should be intger")
        return
    
    if sys.argv[1] == "main":
        p = main_path
    else:
        p = clone_path

    with open(filename, newline='') as csvfile:
        rows = list(csv.reader(csvfile))
        for row in rows[start:end + 1]:
            open_mabi(row[0], row[1], p)
            # time.sleep(delay_s)


if __name__ == '__main__':
    main()
