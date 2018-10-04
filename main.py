import os;

os.system('gcc -o a emax.c');
os.system('a < datasets\\iris.woz > output');
os.system('python score.py');