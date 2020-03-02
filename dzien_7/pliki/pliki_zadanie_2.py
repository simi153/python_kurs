import sys
from collections import defaultdict
if len(sys.argv) > 1:
    plik = sys.argv[1]
else:
    plik = "dane/logs.txt"

def by_name(item):
    return int(item[0].split("-")[1])
def by_time(item):
    return item[1]
try:
    users = set()
    logi = []
    last_login_time = {}
    user_system_time=defaultdict(int)
    with open(plik) as em:
        for log in em:
            name, action, time = log.split(";")
            time = int(time)
            if action == "LOGIN":
                last_login_time[name] = time
            elif action == "LOGOUT":
                user_system_time[name] += time - last_login_time[name]


    for name,time in sorted(user_system_time.items(), key=by_name):
        print(f"{name}: {time}s")

except FileNotFoundError:
    print("Brak takiego pliku!")
