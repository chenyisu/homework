import math
def toRead():
    with open('C:\software\C\python\huffman\press.txt', mode="r") as file:   #開啟文字檔(英文歌詞)
        data = file.read()
    dic = {}    #創建空dictonary
    for i in range(26):  
        tmp = (chr(i+97))
        dic[tmp] = 0    #加入26字母 並初始化為0
    dic['space'] = 0    #加入space  並初始化為0
    dic['carriage return'] = 0       #加入CR     並初始化為0

    for i in data:      #計算符號出現次數
        if(i==' '):
            dic['space']+= 1
        elif(i=='\n'):
            dic['carriage return']+= 1
        else:
            dic[i] += 1
    return dic

def mathLog(dic,totalSymbol):   #計算Entropy
    summ = 0
    temp =[]
    for i in dic:
        if(dic[i] != 0):
            tmpa = dic[i]/totalSymbol
            tmpb = totalSymbol / dic[i]
            summ += tmpa*(math.log2(tmpb))
        elif(dic[i]==0):
            temp.append(i)
    for i in temp:
        del dic[i]
    print('%.3f' %summ)     #印出Entropy (小數點3位)

def huffman(p):
    # 只有2個符號 則分配0..1
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):    #找出頻率最少的2 symbol
    assert(len(p) >= 2)
    sorted_p = sorted(p.items(), key=lambda d:d[1])

    return sorted_p[0][0], sorted_p[1][0]


def main():
    dic = toRead()                      #開啟文字檔並計算出現頻率
    totalSymbol = sum(dic.values())     #計算總長度
    mathLog(dic,totalSymbol)            #計算Entropy 
    c = huffman(dic)                    #編碼
    
    temp = sorted(c.items(), key=lambda d:d[0])
    temp.sort(key=lambda x:len(x[0]))               #排序(字母順序)
    print(temp)         #編碼結果

main()


