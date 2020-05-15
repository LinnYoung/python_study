#coding=utf-8

while True:
    try:
        x = int(input("请输入一个数字："))
        print("瓜娃子，喊你输一个数，就input 一个数，你是不是憨！")
        break
    except Exception:
        print("您输入的不是一个数字,再给你龟儿一次机会！")
