# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def cur_ts():
    return int(time.time() * 1000)

def fmt_ts(ts):
    if len(str(ts)) == 13:
        ts = int(ts) / 1000.0
    else:
        ts = int(ts) / 1.0
    time_arr = time.localtime(ts)
    return time.strftime("%Y%m%d%H%M%S", time_arr)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(cur_ts())
    # print(len(str(cur_ts()/1000)))
    print(fmt_ts(cur_ts()))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
