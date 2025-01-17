import time

def action_1():
    print("First")

def action_2():
    time.sleep(10)
    print("Second")

def action_3():
    print("Third")

def main():
    action_1()
    action_2()
    action_3()

main()
