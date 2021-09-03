import time
import subprocess
import csv
import sys
import os

from mabilogin.beanfun import BeanfunClient
import win32gui
import win32process


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
    # 有時候DES解好後面會帶 "\x00" ，不知原因
    password = otp.split(" ")[-1].replace("\x00", "")
    print(password)

    mabi_path = path + "\\Client.exe"
    acc = auto_filler.accounts[0].acc
    args = [
        mabi_path,
        "code:1622",
        "ver:343",
        "logip:210.208.80.6",
        "logport:11000",
        "chatip:210.208.80.10",
        "chatport:8004",
        "setting:\"file://data/features.xml=Regular, Taiwan\"",
        f"/N:{acc}",
        f"/V:{password}",
        "/T:gamania"
    ]
    print(" ".join(args))
    p = subprocess.Popen(args=" ".join(args), cwd=path, start_new_session=True)
    # print("pid is", p.pid)
    return p


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def setWindow(pid, x, y, size_x, size_y):
    hwnd = get_hwnds_for_pid(pid)[0]
    win32gui.SetWindowPos(hwnd, 1, x, y, size_x, size_y, 0x2000)


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

    procs = []
    with open(filename, newline='') as csvfile:
        rows = list(csv.reader(csvfile))
        for row in rows[start:end + 1]:
            proc = open_mabi(row[0], row[1], p)
            procs.append(proc)
            time.sleep(delay_s)

    print(procs)
    x = 0
    y = 0
    for proc in procs:
        setWindow(proc.pid, x, y, 1090, 764)
        x = x + 50
        y = y + 50


if __name__ == '__main__':
    main()
