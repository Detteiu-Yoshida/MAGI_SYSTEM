#MAGI_SYS.py Ver.1.3 Copyright ©️2021 Chutoro Detteiu(@ctr_exe) All Rights Reserved.
import random
loop_key = 1

priority_class = ['AAA','AA_','A__']
class Color:#文字色指定
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

print('MAGI booting...')
print('MAGI SYSTEM Ver.1.0 Developed by N.Akagi')
while True:
    if loop_key == 1:
        magi_output = ''
        priority = 0
        discussion_num = random.randint(0,9999)#ただの乱数
        priority_num = random.randint(0,2)#Aの数を決める乱数
        start = input('提訴内容を入力してください:')
        print('CODE:' + str(discussion_num))
        print('PRIORITY:' + priority_class[priority_num])
        melchior_output = random.randint(0,1)#メルキオールの回答(0,1の二種)
        balthasar_output = random.randint(0,1)#バルタザールの回答
        casper_output = random.randint(0,1)#カスパーの回答
        magis_yn = [int(melchior_output),int(balthasar_output),int(casper_output)]#それぞれの回答をまとめる
        magis_name = ['MELCHIOR: ','BALTHASAR: ','CASPER: ']#プリント時の名前
        yn = ['否定','承認']
        color_list = [Color.RED,Color.GREEN]#文字色のリスト化(否定時に赤、承認時に緑になるように)
        priority = priority_class[priority_num].count('A')#Aの数(=重要度)の判定(1~3)
        magi_output = melchior_output + balthasar_output + casper_output#マギの回答(1+1+1で最大3)
        for i in range(0,3):#結果の表示
            print(magis_name[i] + color_list[magis_yn[i]] + yn[magis_yn[i]] + Color.END)

        if magi_output >= priority :#承認の数がAの数を超えているか判定
            allover_output = '可決'
        else:
            allover_output = '否決'

        print('提訴 ' + start + ' は ' + allover_output + ' されました')
        if start == '終了' and allover_output == '可決':#終了判定
            break
