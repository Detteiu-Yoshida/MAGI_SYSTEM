#MAGI_SYS_proba.py Ver.1.3 Copyright ©️2021 Chutoro Detteiu(@ctr_exe) All Rights Reserved.
import random
loop_key = 1


print('MAGI booting...')
print('MAGI SYSTEM Ver.1.0 Developed by N.Akagi')
while True:
    if loop_key == 1:
        magi_output = ''
        discussion_num = random.randint(0,9999)#ただの乱数
        start = input('提訴内容を入力してください:')
        print('CODE:' + str(discussion_num))
        melchior_output = random.randint(0,100)#メルキオールの回答(0,1の二種)
        balthasar_output = random.randint(0,100)#バルタザールの回答
        casper_output = random.randint(0,100)#カスパーの回答
        magis_yn = [int(melchior_output),int(balthasar_output),int(casper_output)]#それぞれの回答をまとめる
        magis_name = ['MELCHIOR: ','BALTHASAR: ','CASPER: ']#プリント時の名前

        magi_output = sum(magis_yn) / len(magis_yn)#マギの回答(1+1+1で最大3)
        for i in range(0,3):#結果の表示
            print(magis_name[i] + str(magis_yn[i]) + "%")

        print('提訴 ' + start + ' の確率は ' + str(magi_output) + ' です')
