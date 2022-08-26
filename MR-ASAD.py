import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Ali import asad
    asad()
    print(f'{green}[•] Join Over Facebook Id For Any Help{white}')
    os.system('xdg-open https://www.facebook.com/okiew.you')
elif bit == '32bit':
    from Kami import asad
    asad()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
