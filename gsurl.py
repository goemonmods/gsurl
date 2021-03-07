import bitly_api
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

Acc_Token = '0ba72e24b4370859c9fa12ebb4e738e63e3f4116'  # DON'T CHANGE THIS TOCKEN
connection = bitly_api.Connection(access_token=Acc_Token)
print(Fore.RED + Style.BRIGHT +'\n\n ████████████████████████████████')
print(Fore.RED + Style.BRIGHT +' █─▄▄▄▄█─▄▄▄▄█▄─██─▄█▄─▄▄▀█▄─▄███')
print(Fore.BLUE + Style.BRIGHT +' █─██▄─█▄▄▄▄─██─██─███─▄─▄██─██▀█')
print(Fore.BLUE + Style.BRIGHT +' █▄▄▄▄▄█▄▄▄▄▄██▄▄▄▄██▄▄█▄▄█▄▄▄▄▄█\n')
print(Fore.RED + Style.BRIGHT +' ████████████████████████████████')
print(Style.BRIGHT +
      '\n GSURL Tool is a URL Shortner.\n INTERNET CONNECTION NEEDED.\n ©GOEMON MODS Copyrights Reserved\n Tool '
      'Developed '
      'By : @iamgoemon\n')
print(Fore.RED + Style.BRIGHT +' ████████████████████████████████\n')
link = input(Fore.BLUE + Style.BRIGHT + ' ENTER YOUR LINK : ' + Fore.RESET)
shorten_url = connection.shorten(link)
print(Fore.BLUE + Style.BRIGHT +'\n YOUR SHORTEN URL IS : ' + Fore.RESET + shorten_url.get('url'))
print(Fore.RED + Style.BRIGHT +'\n\n ████████████████████████████████\n')
print(Fore.BLUE + Style.BRIGHT +' THANKS FOR USING OUR TOOL :)\n' + Fore.RESET)
print(Fore.RED + Style.BRIGHT +' ████████████████████████████████\n' + Fore.RESET)
