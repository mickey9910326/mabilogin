from mabilogin.beanfun import BeanfunClient

import subprocess
import os

import win32gui
import win32process


class AccountHandler():

    def __init__(self, name, username, password, lastlogin='',
                 window_cfg=0, x=0, y=0, size_x=1920, size_y=1080,
                 note=''
                 ) -> None:
        # basic info
        self.name = name
        self.username = username
        self.password = password
        self.lastlogin = lastlogin
        self.window_cfg = window_cfg
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.note = note

        # beanfun client info
        self.beanfunClient = BeanfunClient()
        self.logined = False
        self.bf_mabi_usr = ''
        self.bf_mabi_otp = ''

        # process info
        self.opened = False
        self.process = None
        self.pid = 0

    def login(self) -> None:
        try:
            self.beanfunClient.login(self.username, self.password)
            acc = self.beanfunClient.get_accounts()[0]
            otp = self.beanfunClient.get_account_otp(acc)
            self.bf_mabi_usr = acc.acc
            # 有時候DES解好後面會帶 "\x00" ，不知原因
            self.bf_mabi_otp = otp.split(" ")[-1].replace("\x00", "")
            # print(self.bf_mabi_usr)
            # print(self.bf_mabi_otp)
        except:
            print("ERROR: beafun 又在搞鬼")
        self.logined = True

    def open(self, mabi_path: str) -> None:
        client_path = os.path.join(mabi_path, "Client.exe")

        args = [
            client_path,
            "code:1622",
            "ver:343",
            "logip:210.208.80.6",
            "logport:11000",
            "chatip:210.208.80.10",
            "chatport:8004",
            "setting:\"file://data/features.xml=Regular, Taiwan\"",
            f"/N:{self.bf_mabi_usr}",
            f"/V:{self.bf_mabi_otp}",
            "/T:gamania"
        ]
        cmd = " ".join(args)
        self.process = subprocess.Popen(
            cmd, cwd=mabi_path, start_new_session=True)
        self.opened = True
