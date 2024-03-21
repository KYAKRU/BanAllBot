import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "17542849"))
    API_HASH = os.getenv("API_HASH", "8f392dfdc2d0d9ca7a6201f373986fb4")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5347650592:AAFJBqPCOWfqSr1J5MvPvZwGO8g3G99pn6g")
    sudo = os.getenv("SUDO", "5498943520")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
