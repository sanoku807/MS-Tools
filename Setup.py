try:
    import sys
    import os

    def OpenWebsite():
        try:
            import webbrowser
            from Program.Config.Config import telegram
            webbrowser.open(f'https://{website}')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the MS-Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        OpenWebsite()
        os.system("python MS-Tools.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the MS-Tool:\n")
        os.system("pip install --upgrade pip")
        os.system("pip install -r requirements.txt")
        OpenWebsite()
        os.system("python MS-Tools.py")

except Exception as e:
    input(e)