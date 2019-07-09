import os

os.chdir(r'C:\Users\student\TIL\00_Startcamp\02_Day\dummy')

for fliename in os.listdir('.'):
    # os.rename(fliename,f'SAMSUNG_{fliename}')
    os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))
