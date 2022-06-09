fin = open("Words.txt")
fin1 = open('Text.txt')
line1 = fin1.readlines() 
line = fin.readline()  
line = line.split(' ')
line1 = [line.rstrip() for line in line1]
string = ''   
k = 0
for j in range(0, len(line1)):
    if str(line1[j]) != '':
        string += str(line1[j])
string = string.replace(' ', '')
for i in range(0, len(line)):
    if str(line[i]).lower() in string.lower():
        k+=1
        print('{',line[i],'}',' Этого слова здесь -',' [', ((str((line1))).lower()).count((line[i]).lower()), ']', sep='')
if k > 0:
    print('Да есть такие слова, Пользователь!')
else:
    print('Таких слов нет!')