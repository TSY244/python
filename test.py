s = "hello world"  # !
print("Hello World!")  # ?

# TODO: test
# FIXME: test       

# test
# import abc


# class Pet(object, metaclass=abc.ABCMeta):
#     """鐎圭姷澧�"""

#     def __init__(self, nickname):
#         self._nickname = nickname

#     @abc.abstractmethod
#     def make_voice(self):
#         """閸欐垵鍤�婢逛即鐓�"""
#         pass


# class Person:
#     # 闂勬劕鐣綪erson鐎电�呰杽閸欙拷閼崇晫绮︾€规瓨name, __age閸滃畩_sex鐏炵偞鈧�锟�
#     _slots_ = ("__name", "__age", "__sex")

#     def __init__(self, name, age, sex) -> None:  # 閸氬海鐤嗘潻鏂挎礀閸婏拷
#         self.__name = name
#         self.__age = age
#         self.__sex = sex


# class Student(Person):
#     def __init__(self, name, age, sex, school) -> None:
#         super().__init__(name, age, sex)  # 鐠嬪啰鏁ら悥鍓佽��閻ㄥ嫭鐎�闁�鐘插毐閺侊拷
#         self.__school = school

#     def get_name(self):
#         return super.__name

#     @staticmethod  # 闂堟瑦鈧�浣规煙濞夛拷
#     def get_age():
#         return super.__age

#     @classmethod  # 缁�缁樻煙濞夛拷
#     def getClassName(cls):
#         return cls.__name__


# wx = Student("wx", 19, "w", "cuit")
# print(wx.getClassName())

# class Student:
#     def __init__(self, name, age, sex, school) -> None:
#         # 闁告�佹磻缁楀懘宕氶幒鏂挎疇鐎碉拷妤﹁法娈堕柛娆愶耿閸ｆ椽宕ｅ�炲墽绠介柟韬插€楀▓锟�
#         self._name = name
#         self._age = age
#         self._sex = sex
#         self._school = school

#     # 闁伙拷閻旈潻鎷烽敐鍥ㄧ暠getter
#     @property
#     def name(self):
#         return self._name

#     @property  # 闁告瑱鎷峰ù鐘�鍎版繛鍥�鎮介埡鐜漥ect.name闁兼澘濂旂粭澶愭�侀埀锟介悷鏇氭�掓繛鍥�鎮介敓锟�()
#     def age(self):
#         return self._age

#     @name.setter  # 闁告帗绋戠紓鎾寸�嶉崬鎶畂perty闁归潧绉烽崗妯绘媴鐠恒劍鏆�
#     def name(self, name):
#         self._name = name

#     @age.setter
#     def age(self, age):
#         self._age = age


# wx = Student("wx", 19, "w", "cuit")

# # 闁汇垹褰夌花锟芥繛锝堬拷鎻掞拷鐐寸�嶉崪锟絧roperty闁告瑱鎷峰ù鐘�鍎遍崕姘跺箣閹帮拷閹叉娊宕ｅ�椻偓閸ｇ儤绋夐埀锟介柡宥囨焿閿熻棄娼″Λ鍫曟晬鐏炶偐绋婚柡鍕舵嫹闁哄洦娼欐慨鐐烘儍閸曪拷閻ｃ劑宕楅敓锟�
# print(wx.name)
# wx.name = "wwxx"
# print(wx.name)


# import random


# # 閻犱礁娼″Λ绂穏e缂佸�夌劍濠€渚€宕ｅ�椻偓閸ｏ拷
# print(wx._Student__age)

# passwd_len = 10
# all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# passwd = ""

# for i in range(passwd_len):
#     index = random.randint(0, len(all_chars) - 1)  # 闁跨噦鎷�?闁跨噦鎷�?闁稿繐鍊圭粙澶嬫姜閹碉拷閻�鍡椻槈閺傝法澧曢柛锝囧劋缁嬪�愭晸閿燂拷?闂佽法鍣﹂幏锟�?
#     passwd += str(all_chars[index])

# print(passwd)


# import os
# import time

# string = "闂佹悶鍎茬粙鎴犵玻濞戙垹绠ｉ柟鐗堟緲閸樺瓨绻涢崱鎰�鐏辩紒璇诧拷锟介弫鎾绘晸閿燂拷??!"
# while True:
#     os.system("cls")
#     print(string)
#     time.sleep(0.2)
#     string = string[1:] + string[0]


# de_number = 42
# oct_number = "/52"
# print(chr(de_number))


# list1 = ["hello"]

# list2 = list1 * 3
# print(list2)


# string = """z
# j
# d
# """
# print("a" not in string)
# import hashlib


# salt=moectf2023

# def gethash(*items):
#     c = 0
#     for item in items:
#         if item is None:
#             continue
#         c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big") # it looks so complex! but is it safe enough?
#         # encode闁诲孩鍐婚幏锟�?闁跨喕妫勮灐闂佽法鍣﹂幏锟�?
#         # digest闂佸吋鍎抽崲鑼躲亹閸モ斁鍋撳☉铏�瀚�?闁跨喕妫勮灐闂佽法鍣﹂幏锟�?
#     return hex(c)[2:]

# assert users["admin"] == "admin"

# hashed_users = dict((k,gethash(k,v)) for k,v in users.items())

# # from secrets import users, salt
# import hashlib
# import base64
# import json
# import http.server

# #with open("flag.txt", "r") as f:
# #     FLAG = f.read().strip()


# def gethash(*items):
#     c = 0
#     for item in items:
#         if item is None:
#             continue
#         c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(),
#                             "big")  # it looks so complex! but is it safe enough?
#     return hex(c)[2:]


# hashed_users = dict((k, gethash(k, v)) for k, v in users.items())
# # 闂佸憡甯楃粙鎴犵磽閹惧灈鍋撳☉铏�瀚�?闁跨喕妫勯幃锟�

# eval(int.to_bytes(
#     0x636d616f686e69656e61697563206e6965756e63696165756e6320696175636e206975616e6363616361766573206164 ^ 8651845801355794822748761274382990563137388564728777614331389574821794036657729487047095090696384065814967726980153,
#     160, "big", signed=True).decode().translate({ord(c): None for c in "\x00"}))  # what is it?


# # 14061007122519446164375028329907519263936194248453407309993939260815535517793501514912809786428292624760351565897053
# def decrypt(data: str):
#     for x in range(5):
#         data = base64.b64encode(data).decode()  # ummm...? It looks like it's just base64 encoding it 5 times? truely?
#     return data


# # 5base64

# __page__ = base64.b64encode(
#     "PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICAgIDx0aXRsZT5zaWduaW48L3RpdGxlPgogICAgPHNjcmlwdD4KICAgICAgICBbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoK3t9K1tdKVsrISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXVtbXV0rW10pWytbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoW10rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKVshK1tdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKShbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXSshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyhbXStbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKCFbXStbXSlbIStbXSshIVtdXSsoW10re30pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSkpWyErW10rISFbXSshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0pKCErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKChbXSt7fSlbK1tdXSlbK1tdXSsoIStbXSshIVtdKyEhW10rW10pKyhbXVtbXV0rW10pWyErW10rISFbXV0pKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXSt7fSlbKyEhW11dKygre30rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSkKICAgICAgICB2YXIgXzB4ZGI1ND1bJ3N0cmluZ2lmeScsJ2xvZycsJ3Bhc3N3b3JkJywnL2xvZ2luJywnUE9TVCcsJ2dldEVsZW1lbnRCeUlkJywndGhlbiddO3ZhciBfMHg0ZTVhPWZ1bmN0aW9uKF8weGRiNTRmYSxfMHg0ZTVhOTQpe18weGRiNTRmYT1fMHhkYjU0ZmEtMHgwO3ZhciBfMHg0ZDhhNDQ9XzB4ZGI1NFtfMHhkYjU0ZmFdO3JldHVybiBfMHg0ZDhhNDQ7fTt3aW5kb3dbJ2FwaV9iYXNlJ109Jyc7ZnVuY3Rpb24gbG9naW4oKXtjb25zb2xlW18weDRlNWEoJzB4MScpXSgnbG9naW4nKTt2YXIgXzB4NWYyYmViPWRvY3VtZW50W18weDRlNWEoJzB4NScpXSgndXNlcm5hbWUnKVsndmFsdWUnXTt2YXIgXzB4NGZkMjI2PWRvY3VtZW50W18weDRlNWEoJzB4NScpXShfMHg0ZTVhKCcweDInKSlbJ3ZhbHVlJ107dmFyIF8weDFjNjFkOT1KU09OW18weDRlNWEoJzB4MCcpXSh7J3VzZXJuYW1lJzpfMHg1ZjJiZWIsJ3Bhc3N3b3JkJzpfMHg0ZmQyMjZ9KTt2YXIgXzB4MTBiOThlPXsncGFyYW1zJzphdG9iKGF0b2IoYXRvYihhdG9iKGF0b2IoXzB4MWM2MWQ5KSkpKSl9O2ZldGNoKHdpbmRvd1snYXBpX2Jhc2UnXStfMHg0ZTVhKCcweDMnKSx7J21ldGhvZCc6XzB4NGU1YSgnMHg0JyksJ2JvZHknOkpTT05bXzB4NGU1YSgnMHgwJyldKF8weDEwYjk4ZSl9KVtfMHg0ZTVhKCcweDYnKV0oZnVuY3Rpb24oXzB4Mjk5ZDRkKXtjb25zb2xlW18weDRlNWEoJzB4MScpXShfMHgyOTlkNGQpO30pO30KICAgIDwvc2NyaXB0Pgo8L2hlYWQ+Cjxib2R5PgogICAgPGgxPmV6U2lnbmluPC9oMT4KICAgIDxwPlNpZ24gaW4gdG8geW91ciBhY2NvdW50PC9wPgogICAgPHA+ZGVmYXVsdCB1c2VybmFtZSBhbmQgcGFzc3dvcmQgaXMgYWRtaW4gYWRtaW48L3A+CiAgICA8cD5Hb29kIEx1Y2shPC9wPgoKICAgIDxwPgogICAgICAgIHVzZXJuYW1lIDxpbnB1dCBpZD0idXNlcm5hbWUiPgogICAgPC9wPgogICAgPHA+CiAgICAgICAgcGFzc3dvcmQgPGlucHV0IGlkPSJwYXNzd29yZCIgdHlwZT0icGFzc3dvcmQiPgogICAgPC9wPgogICAgPGJ1dHRvbiBpZCA9ICJsb2dpbiI+CiAgICAgICAgTG9naW4KICAgIDwvYnV0dG9uPgo8L2JvZHk+CjxzY3JpcHQ+CiAgICBjb25zb2xlLmxvZygiaGVsbG8/IikKICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJsb2dpbiIpLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgbG9naW4pOwo8L3NjcmlwdD4KPC9odG1sPg==")

# """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>signin</title>
#     <script>
#         [][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((+{}+[])[+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+([]+{})[!+[]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+([][[]]+[])[+[]]+([][[]]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]))[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]])(!+[]+!![]+!![]+!![])([][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]))[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]])(!+[]+!![]+!![]+!![]+!![]+!![]+!![])(([]+{})[+[]])[+[]]+(!+[]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]])+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+([]+{})[!+[]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(+{}+[])[+!![]])(!+[]+!![]+!![]+!![])
#         var _0xdb54=['stringify','log','password','/login','POST','getElementById','then'];var _0x4e5a=function(_0xdb54fa,_0x4e5a94){_0xdb54fa=_0xdb54fa-0x0;var _0x4d8a44=_0xdb54[_0xdb54fa];return _0x4d8a44;};window['api_base']='';function login(){console[_0x4e5a('0x1')]('login');var _0x5f2beb=document[_0x4e5a('0x5')]('username')['value'];var _0x4fd226=document[_0x4e5a('0x5')](_0x4e5a('0x2'))['value'];var _0x1c61d9=JSON[_0x4e5a('0x0')]({'username':_0x5f2beb,'password':_0x4fd226});var _0x10b98e={'params':atob(atob(atob(atob(atob(_0x1c61d9)))))};fetch(window['api_base']+_0x4e5a('0x3'),{'method':_0x4e5a('0x4'),'body':JSON[_0x4e5a('0x0')](_0x10b98e)})[_0x4e5a('0x6')](function(_0x299d4d){console[_0x4e5a('0x1')](_0x299d4d);});}
#     </script>
# </head>
# <body>
#     <h1>ezSignin</h1>
#     <p>Sign in to your account</p>
#     <p>default username and password is admin admin</p>
#     <p>Good Luck!</p>

#     <p>
#         username <input id="username">
#     </p>
#     <p>
#         password <input id="password" type="password">
#     </p>
#     <button id = "login">
#         Login
#     </button>
# </body>
# <script>
#     console.log("hello?")
#     document.getElementById("login").addEventListener("click", login);
# </script>
# </html>
# """


# class MyHandler(http.server.BaseHTTPRequestHandler):  # 缂傚倷缍€閸曡埖瀚�??
#     def do_GET(self):
#         try:
#             if self.path == "/":
#                 self.send_response(200)
#                 self.end_headers()
#                 self.wfile.write(__page__)
#                 # 闂佽皫宥嗗��?闁跨喓鏅�缁夊潡鏌ｉ敐鍛�鐒搁柨鐕傛嫹?
#             else:
#                 self.send_response(404)
#                 self.end_headers()
#                 self.wfile.write(b"404 Not Found")
#         except Exception as e:
#             print(e)
#             self.send_response(500)
#             self.end_headers()
#             self.wfile.write(b"500 Internal Server Error")

#     def do_POST(self):
#         try:
#             if self.path == "/login":
#                 body = self.rfile.read(int(self.headers.get("Content-Length")))
#                 payload = json.loads(body)
#                 params = json.loads(decrypt(payload["params"]))
#                 print(params)
#                 if params.get("username") == "admin":
#                     self.send_response(403)
#                     self.end_headers()
#                     self.wfile.write(b"YOU CANNOT LOGIN AS ADMIN!")
#                     print("admin")
#                     return
#                 if params.get("username") == params.get("password"):
#                     self.send_response(403)
#                     self.end_headers()
#                     self.wfile.write(b"YOU CANNOT LOGIN WITH SAME USERNAME AND PASSWORD!")
#                     print("same")
#                     return
#                 hashed = gethash(params.get("username"), params.get("password"))
#                 for k, v in hashed_users.items():
#                     if hashed == v:
#                         data = {
#                             "user": k,
#                             "hash": hashed,
#                             "flag": FLAG if k == "admin" else "flag{YOU_HAVE_TO_LOGIN_IN_AS_ADMIN_TO_GET_THE_FLAG}"
#                         }
#                         self.send_response(200)
#                         self.end_headers()
#                         self.wfile.write(json.dumps(data).encode())
#                         print("success")
#                         return
#                 self.send_response(403)
#                 self.end_headers()
#                 self.wfile.write(b"Invalid username or password")
#             else:
#                 self.send_response(404)
#                 self.end_headers()
#                 self.wfile.write(b"404 Not Found")
#         except Exception as e:
#             print(e)
#             self.send_response(500)
#             self.end_headers()
#             self.wfile.write(b"500 Internal Server Error")


# if __name__ == "__main__":
#     server = http.server.HTTPServer(("", 9999), MyHandler)
#     server.serve_forever()


# a=[0x1B, 0x9B, 0xFB, 0x19, 0x06, 0x6A, 0xB5, 0x3B, 0x7C, 0xBA, 0x03, 0xF3, 0x91, 0xB8, 0xB6, 0x3D, 0x8A, 0xC1, 0x48, 0x2E, 0x50, 0x11, 0xE7, 0xC7, 0x4F, 0xB1, 0x27, 0xCF, 0xF3, 0xAE, 0x03, 0x09, 0xB2, 0x08, 0xFB, 0xDC, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00]
#
# temp=""
#
# for i  in a:
#     if len(hex(i)[2:])==1 :
#         temp+='0'
#     temp+=hex(i)[2:]
#
# print(temp)


# import re

# text = '<div id="info"><h2>濠碉拷閿濆棙锟戒胶绮嬪畝瀣�瀚�??闁跨噦鎷�?闁跨噦鎷�?閻庯絽澧庣壕锟�</h2><h3><font color="red">闂佽法鍣﹂幏锟�?闁跨噦鎷�?闁规崘娅曢崐鑽も偓褰掓交鐠侊絿妲愬┑鍥┾攳婵犻潧娲ら惁锟介柡澶嗘櫆閻熴倝鏌屽�婂牊鐒婚柣鏂垮殩閹凤拷??</font></h3></div>'
# pattern = r'闂佽法鍣﹂幏锟�?闂佽法鍣﹂幏锟�?(.*?)(.*?)</font>'

# match = re.search(pattern, text)
# if match:
#     print("闂佽法鍣﹂幏锟�?闁跨噦鎷�?闁规崘娅曢崐鐢告⒒閸�娑樼伄婵炲牊鍨剁粙澶愬Χ閸曪拷閸ゅ��鎮楀☉铏�瀚�?闁跨喓鏅�缁愶拷", match.group(1))
#     print("','闂佸憡鑹鹃柊锝咃拷闂村嵆閹�鍐�鏁撻敓锟�?闁哥偛锟界硶鍋撻崷锟藉▍銏ゆ晸閿燂拷?", match.group(2))
# else:
#     print("濠电偛澶囬崜婵嗭耿娓氣偓楠炲秹骞嗚�嶉悡鍌炴煕閺嵮呯Ш闁告ǜ鍊濋弫鎾绘晸閿燂拷??")
