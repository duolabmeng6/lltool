# -*- coding: utf-8 -*-
import rumps
from pyefun import *
from pyefun.人工智能.通用文字识别 import *  # 提供通用的中文文字识别功能
from pyefun.模块.剪切板操作 import *  # 剪切板操作
from pyefun.模块.苹果系统操作 import *
from pyefun.模块.终端类 import *

__version__ = "2022.06.30"


class Pine(rumps.App):

    def __init__(self):
        icon_color = "white"
        super(Pine, self).__init__(name="Pine",
                                   icon=f"icons/{icon_color}_logo.ico")
        截图识别文字 = rumps.MenuItem("截图识别文字",
                                icon=f"icons/{icon_color}_select.png")
        启动微信 = rumps.MenuItem("启动微信",
                              icon=f"icons/{icon_color}_select.png")
        关于 = rumps.MenuItem("关于")

        self.menu = [截图识别文字, 启动微信, 关于]

    @rumps.clicked("启动微信")
    def _启动微信(self, _):
        print("启动微信")
        # cmd = 'echo {} | sudo -S open -n /Applications/WeChat.app/Contents/MacOS/WeChat'.format("密码")
        # ok = subprocess.call(cmd, shell=True)

        cmd = 'open -n /Applications/WeChat.app/Contents/MacOS/WeChat'
        终端类().运行(cmd)

    @rumps.clicked("截图识别文字")
    def _截图识别文字(self, _):
        image_captured, file_path = 系统截图()
        if not image_captured:
            return
        print('图片路径', file_path)
        text = 通用文字识别获取文字(file_path)
        if len(text) != 0:
            print(text)
            置剪辑板文本(text)
            删除文件(file_path)
            提示框("Pine", "已经复制到剪切板")

    @rumps.clicked("关于")
    def _关于(self, _):
        rumps.alert(
            title="Pine",
            message=f"龙龙自用 版本号{__version__}"
        )


if __name__ == "__main__":
    Pine().run()
