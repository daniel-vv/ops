__auther__ = 'Victor'
# 1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )

import sys
result = None
list_info = []


def replace(info):#split
   global list_info
   if '＋' in info:
     info = info.replace('＋',' ＋ ')
   if '-' in info:
     info = info.replace('-',' - ')
   if '*' in info:
     info = info.replace('*',' * ')
   if '/' in info:
     info = info.replace('/',' / ')
   if '(' in info:
     info = info.replace('(',' ( ')
   if ')' in info:
     info = info.replace(')',' ) ')
   list_info =info.split()

def compute(list_info):#计算加减乘除
   global result
   while '/' in list_info:
        a = float(list_info[list_info.index('/')-1]) / float(list_info[list_info.index('/')+1])
        list_info.insert(list_info.index('/')-1,a)
        list_info.pop(list_info.index('/')-1)
        list_info.pop(list_info.index('/')+1)
        list_info.pop(list_info.index('/'))
   while '*' in list_info:
        a = float(list_info[list_info.index('*')-1]) * float(list_info[list_info.index('*')+1])
        list_info.insert(list_info.index('*')-1,a)
        list_info.pop(list_info.index('*')-1)
        list_info.pop(list_info.index('*')+1)
        list_info.pop(list_info.index('*'))
   while '-' in list_info:
        a = float(list_info[list_info.index('-')-1]) - float(list_info[list_info.index('-')+1])
        list_info.insert(list_info.index('-')-1,a)
        list_info.pop(list_info.index('-')-1)
        list_info.pop(list_info.index('-')+1)
        list_info.pop(list_info.index('-'))
   while '＋' in list_info:
        a = float(list_info[list_info.index('＋')-1]) + float(list_info[list_info.index('＋')+1])
        list_info.insert(list_info.index('＋')-1,a)
        list_info.pop(list_info.index('＋')-1)
        list_info.pop(list_info.index('＋')+1)
        list_info.pop(list_info.index('＋'))
#   result=float(list_info[0])
   result = list_info[0]

def run_main(list_info):#提取括号内的内容
   list_end = []
   if '(' in list_info:
        list_info.reverse()
        last_bracket = len(list_info) - list_info.index('(') -1
        list_info.reverse()
        first_bracket = list_info[last_bracket:].index(')')
        list1 = list_info[last_bracket + 1:last_bracket + first_bracket]
        if list1[0] == '-': #处理负数
             i = '%s%s' %(list1[0],list1[1])
             negative_num = float(i)
             list_end.append(negative_num)
        else:
             compute(list1)
             list_end.append(result)
             new_list = list_info[:last_bracket] + list_end + list_info[last_bracket + first_bracket + 1:]
        if '(' in new_list:
            run_main(new_list)
        else:
            compute(new_list)
            print (result)
   elif ')' not in list_info:
        compute(list_info)
        print (result)
   else:
        print ("Sorry,invalid syntax!")

if __name__ == '__main__':
  while True:
    info = input('Please input fomula:').replace(' ', '')
    if info.isalpha() or info == "":
        print('Sorry input error...')
        continue
  replace(info)
  run_main(list_info)
   #print ("Sorry,invalid syntax!")
