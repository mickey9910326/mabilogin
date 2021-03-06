from mabilogin_gui.ui.ui_acc_setting_wgt import Ui_accSettingWgt
from mabilogin_gui.ui.ui_acc_wgt import Ui_accWgt
from mabilogin_gui.account_handler import AccountHandler

from PySide6.QtWidgets import QWidget, QVBoxLayout

from jsoncomment import JsonComment

import typing
import csv
import os


class AccGroup():

    def __init__(self, wgt, config_file) -> None:
        self.base_widget = wgt  # which widget to layout
        self.config_file = config_file
        self.accHdlrs = []
        self.accWgts = []

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

        # self.ui_acc = Ui_accWgt()
        # self.accWgt = QWidget()
        # self.mainLyt.addWidget(self.accWgt)
        # self.ui_acc.setupUi(self.accWgt)
        # self.ui_acc.detailWgt.hide()

    def get_accounts(self):
        fp = f"acc/{self.cfg['acc_csv']}"
        if os.path.exists(fp) is False:
            # TODO do error msg
            print(f"ERROR: {fp} not found")
            return

        with open(fp, mode='r', newline='', encoding='utf8') as csvfile:
            rows = list(csv.reader(csvfile))
            print(rows)
            for idx, row in enumerate(rows[1::]):
                accHdlr = AccountHandler(*row)

                accWgt = QWidget()
                self.mainLyt.addWidget(accWgt)
                accHdlr.setupUi(accWgt, idx + 1)
                # accHdlr.ui.detailWgt.hide()

                self.accHdlrs.append(accHdlr)
                self.accWgts.append(accHdlr)
