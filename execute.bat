gcc -o a emax.c
a < datasets\iris.woz > output
python score.py
gcc -o a k-means.c
a < datasets\iris.woz > output
python score.py