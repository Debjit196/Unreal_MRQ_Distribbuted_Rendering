import os
import shutil
x=os.getcwd()
y=x[x.find('UE_4'):]
z=y[:y.find(os.sep)]
g=r"{}".format(x[:x.find('UE_4')])+z+r"\Engine\Binaries\ThirdParty\Python3\Win64"
shutil.copy(x+"//requirements.txt",g)
os.chdir(g)
os.system('cmd /k "python.exe -m pip install -r requirements.txt"')
os.remove(g+"//requirements.txt")
