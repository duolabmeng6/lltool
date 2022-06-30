from setuptools import setup

APP = ["lltool.py"]
DATA_FILES = ["logs","icons"]
OPTIONS = {
    "argv_emulation": True,
    #"iconfile": "Wind.icns",
    "packages": ["rumps",],
    "plist": {
        "LSUIElement": True,#隐藏dock栏图标显示
        "CFBundleName": "lltool",#应用名
        "CFBundleDisplayName": "lltool",#应用显示名
        "CFBundleVersion": "0.0.1",#应用版本号
        "CFBundleIdentifier": "lltool_APP",#应用包名、唯一标识
        "NSHumanReadableCopyright": "Copyright © 2022 CHENSUILPONG. All rights reserved." #可读版权
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
