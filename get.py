import requests
import datetime
from functools import cache
from private import sessionToken


@cache
def get_data(day):
    headers = {'Cookie': 'session=' + sessionToken}
    data = requests.get(f'https://adventofcode.com/2022/day/{day}/input',headers=headers)
    return day,data

def write_data():
    d = datetime.datetime.now()
    day = str(d.strftime("%d")).replace("0", "")
    data = get_data(day)
    try:
        with open(f'data/day{day}.txt',"w+") as f:
            f.write(data.content.decode("utf-8"))
        with open(f'day_{day}.py','w+') as f:
            f.write("""def solve_p1(data): 
        return None
    
    
    def solve_p2(data):
        return None""")
        return True
    except Exception as e:
        print(e)
        return False
