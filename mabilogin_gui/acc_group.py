from mabilogin_gui.ui.ui_acc_setting_wgt import Ui_accSettingWgt
from mabilogin_gui.ui.ui_acc_wgt import Ui_accWgt

from PySide6.QtWidgets import QWidget, QVBoxLayout

from jsoncomment import JsonComment

import typing
import csv
import os


class AccGroup():

    class Account():
        def __init__(self, name, username, password, lastlogin='',
                     window_cfg=0, x=0, y=0, size_x=1920, size_y=1080,
                     note=''
                     ) -> None:
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

        def toCsvRow(self) -> typing.List[str]:
            return [self.name,
                    self.username,
                    self.password,
                    self.lastlogin,
                    str(self.window_cfg),
                    str(self.x),
                    str(self.y),
                    str(self.size_x),
                    str(self.size_y),
                    self.note
                    ]

        def __str__(self):
            return f"Name:{self.name}"

    def __init__(self, wgt, config_file) -> None:
        self.base_widget = wgt  # which widget to layout
        self.config_file = config_file
        self.load_cfg()
        self.ui_setup()
        self.get_accounts()

    def load_cfg(self) -> None:
        fp = f"acc/{self.config_file}"
        if os.path.exists(fp) is False:
            # TODO do error msg
            print(f"ERROR: {fp} not found")
            return

        with open(fp, mode='r', encoding="utf8") as f:
            text = f.read()
            print(text)
            parser = JsonComment()
            self.cfg = parser.loads(text)
            print(self.cfg)

    def ui_setup(self):
        self.mainLyt = QVBoxLayout(self.base_widget)
        self.mainLyt.setSpacing(0)
        self.mainLyt.setObjectName(u"mainLyt")
        self.mainLyt.setContentsMargins(0, 0, 0, 0)

        self.ui_accSetting = Ui_accSettingWgt()
        self.accSettingWgt = QWidget()
        self.mainLyt.addWidget(self.accSettingWgt)
        self.ui_accSetting.setupUi(self.accSettingWgt)
        self.ui_accSetting.mabiFolderLineEdit.setText(self.cfg['mabi_path'])

        self.ui_acc = Ui_accWgt()
        self.accWgt = QWidget()
        self.mainLyt.addWidget(self.accWgt)
        self.ui_acc.setupUi(self.accWgt)
        self.ui_acc.detailWgt.hide()

    def get_accounts(self):
        fp = f"acc/{self.cfg['acc_csv']}"
        if os.path.exists(fp) is False:
            # TODO do error msg
            print(f"ERROR: {fp} not found")
            return

        with open(fp, mode='r', newline='', encoding='utf8') as csvfile:
            rows = list(csv.reader(csvfile))
            print(rows)
            acc = AccGroup.Account(*rows[1])
            print(acc)

        with open(fp, mode='w', newline='', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["名稱", "帳號", "密碼", "最後登入時間", "視窗設定",
                            "視窗x位置", "視窗y位置", "視窗x大小", "視窗y大小", "註記"])
            writer.writerow(acc.toCsvRow())
