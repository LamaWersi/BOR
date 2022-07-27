#Библиотеки
import random
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style
print("LOAD")
os.system('TITLE bor')
os.system('cls')
#Иговой мир
#0 - пустое пространство, 1 - заполненое пространство 9 - игрок 3 - блок игрока 4 - ракета вправо 5 - ракета влево
#В каждом слое должно быть одиноковое кол-во символов (13)28
world = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,99,99],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,99,99]];
#Переменные
life = 5
ShowPanelCreator = False #панель разработчика
start_game = False #начало игры
reset = False #Для перезагрузки мира
#координаты игрока
x = 17
y = 0
#Переменные для изменения мира после шага
x1 = x
y1 = y
world[y][x] = 9
#Инвентарь
invent = [1,2,3]#1 - кирка, 2 - установка блоков, 3 - рпг
invent_on = 1
#Логика РПГ
kol_rpg = False #Для движения ракет
all_k_rpg = [0,0,0,0,0,0,0,0]#Максимум 8 ракет или же (7)
min_rpg_place = 0 #Для масива с ракетами
kol_rpg_sc = 0 #Для подсчёта ракет
#Переменные для физики игрока. False - игрок не летит True - игрок летит
yf = False
yp = False
jump = False
on_grav = True #Переменная для вкл/выкл гравитации
#игровой цикл
while(1==1):
    while(start_game == False):#Игровое меню
        for i in range(0,5):
            print('')
        print("                                                       NEW GAME(1)")
        print("                                                       LOAD GAME(2)")
        vbr = input()
        if(vbr == "1"):
            print("Новый мир(1)")
            vbr3 = input()
            if(vbr3 == "1"):
                print("Простой мир(1)")
                print("Случайный мир(2)")
                vbr3 = input()
                if(vbr3 == "1"):
                    start_game = True
                    os.system('cls')
                    reset = False
                elif(vbr3 == "2"):
                    for i in range(0,8):
                        for j in range(1, 42):
                            if(i < 5 and i > 3): #Генерация поверхности
                                irand = random.randint(0,2)
                                world[i - irand][j] = 3
                                irandpov = irand
                                for b in range(i - irand,8):
                                    world[b][j] = 3
                            elif(i > 4 and i < 6 and j > 5 and j < 40):
                                gen = random.randint(0,5)
                                if(gen == 1):
                                    down = 0
                                    dell = 1
                                    i3 = 8
                                    for i2 in range(world[i3][j] != 0):
                                        if(i3 == 8):
                                            i3 = i2
                                            
                                        if(down < 2):
                                            world[i][j-dell] = 0
                                            world[i][j+dell] = 0
                                            down += 1
                                        world[i][j] = 0
                                        i3 -= 1
                                    
                x = 17
                y = 0
                world[y][x] = 9
                reset = False
                start_game = True
                os.system('cls')
        elif(vbr == "2"):
            print("Ввыдите ID мира")
            for i in range(0,9):
                for j in range(0,45):
                    s = int(input()) #Ввод числа мира
                    world[i][j] = s
                                    
                x = 17
                y = 0
                world[y][x] = 9
                reset = False
                start_game = True
                os.system('cls')
                            
            else:
                print("error")
                time.sleep(1)
        os.system('cls')
    while(start_game == True): #------------------------------------------------------------------------------------------------------------------------------------------------
        print('Статистика игрока:                                                                                              v 1.5')
        print('X: ',x)
        print('Y: ',y)
        print('life: ', life)
        if(ShowPanelCreator == True):
            print(kol_rpg >= 0, all_k_rpg)
        print("---------------------------------")
        for i in range(0,6):#Выравнивание экрана 
            print('')
        for i in range(0,9):#Цикл для отрисовки мира
            for j in range(0,45):
                if(world[i][j] == 0):
                    print(' ', end="")
                elif(world[i][j] == 1):
                    print('█', end="")
                elif(world[i][j] == 9):
                    print(Fore.RED+'▼' + Fore.WHITE, end="")
                elif(world[i][j] == 3):
                    print(Fore.GREEN +'█' +Fore.WHITE, end="")
                elif(world[i][j] == 4):
                        print(Fore.RED+">"+ Fore.WHITE, end="")
                elif(world[i][j] == 5):
                    print(Fore.RED+"<"+ Fore.WHITE, end="")
            print('')
        #физика
        if(on_grav == True):
            if(world[y + 1][x] == 0):#Физика игрока 2.0
                y1 = y
                x1 = x
                y+=1
                world[y1][x1] = 0
                yf = False
                jump = True
            else:
                jump = False
        #ФИЗИКА И ЛОГИКА РПГ
        if(kol_rpg == True):
            for i in range(0, 7):#удаление , взрыв ракет
                if(all_k_rpg[i] != 0):
                    if(world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] != 0 and all_k_rpg[i][2] == True):#Для правых ракет
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] - 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] + 1] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] - 1] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] - 1] = 0
                            
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] = 0
                        if(world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] = 0
                        
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 0
                        all_k_rpg[i] = 0
                        kol_rpg_sc -= 1
                    elif(world[all_k_rpg[i][0]][all_k_rpg[i][1] - 1] != 0 and all_k_rpg[i][2] == False):#Для правых ракет
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] - 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] + 1] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1]] = 0
                        
                        if(world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] - 1] != 1):
                            world[all_k_rpg[i][0] + 1][all_k_rpg[i][1] - 1] = 0
                            
                        if(world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0] - 1][all_k_rpg[i][1] + 1] = 0
                        if(world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] != 1):
                            world[all_k_rpg[i][0]][all_k_rpg[i][1] + 1] = 0
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 0
                        all_k_rpg[i] = 0
                        kol_rpg_sc -= 1
            for i in range(0,7):#для движения ракет и обновления min_rpg_place
                if(min_rpg_place > i and all_k_rpg[i] == 0 ):#обновление
                    min_rpg_place = i
                if(all_k_rpg[i] != 0):#Движение
                    if(all_k_rpg[i][2] == True):#Вправо
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 0
                        all_k_rpg[i][1] += 1
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 4
                    else:#Влево
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 0
                        all_k_rpg[i][1] -= 1
                        world[all_k_rpg[i][0]][all_k_rpg[i][1]] = 5
        #Управление игрока3
        x1 = x
        y1 = y
        way = input('> or < or ^ or | or * or i: ')
        if(way == '>' and world[y][x+1] == 0):#Управление
            x+=1
        elif(way == '>>' and world[y][x+2] == 0 and world[y][x+1] == 0):
            x+=2
        elif(way == '<' and world[y][x-1] == 0):
            x-=1
        elif(way == '<<' and world [y][x-2] == 0 and world[y][x-1] == 0):
            x-=2
        elif(way == '^' and yf == False and jump == False and world[y-1][x] == 0):
            y-=1
            yf = True
            jump = True
        elif(way == '^>' and yf == False and world[y-1][x+1] == 0 and jump == False and world[y-1][x] == 0):
            y -= 1
            x += 1
        elif(way == '<^' and yf == False and world[y-1][x-1] == 0 and jump == False and world[y-1][x] == 0):
            y -= 1
            x -= 1
        elif(way == '|>' and world[y][x+1] == 0 and (world[y+1][x+1] != 0 or world[y-1][x+1] != 0 or world[y][x+2] != 0 or world[y+1][x] != 0)and invent_on == 2): #Строительство 
            world[y][x+1] = 3
        elif(way == '||>' and world[y][x+1] == 3 and invent_on == 1):
            world[y][x+1] = 0
        elif(way == '<|' and world[y][x-1] == 0 and (world[y+1][x-1] != 0 or world[y][x-2] != 0 or world[y-1][x-1] != 0 or world[y+1][x+1] != 0 or world[y-1][x+1] != 0 or world[y+1][x] != 0) and invent_on == 2):
            world[y][x-1] = 3
        elif(way == '<||' and world[y][x-1] == 3 and invent_on == 1):
            world[y][x-1] = 0
        elif(way == '^|^' and world[y-1][x] == 0 and (world[y-1][x-1] != 0 or world[y-1][x+1] != 0 or world[y-2][x] != 0) and invent_on == 2):
            world[y-1][x] = 3
        elif(way == '*|>' and world[y+1][x+1] == 0 and(world[y+1][x] != 0 or world[y+1][x+2] != 0 or world[y+1][x+1] != 0)and invent_on == 2):
            world[y+1][x+1] = 3
        elif(way == '<|*' and world[y+1][x - 1] == 0 and (world[y+1][x] != 0 or world[y+1][x-2] != 0 or world[y+1][x-1] != 0)and invent_on == 2):
            world[y+1][x-1] = 3
        elif(way == '|*|' and world[y+1][x] == 3 and invent_on == 1):
            world[y+1][x] = 0
        elif(way == 'r|>' and world[y][x+1] == 0 and invent_on == 3 and  kol_rpg_sc < 8):#Ракеты вправо
            kol_rpg = True
            all_k_rpg[min_rpg_place] = [y,x+1,True]#True and False для направления ракеты. True - вправо, False - влево.
            world[y][x+1] = 4
            min_rpg_place += 1
            kol_rpg_sc += 1
        elif(way == '<|r' and world[y][x-1] == 0 and invent_on == 3 and  kol_rpg_sc < 8):#Ракеты вправо
            kol_rpg = True
            all_k_rpg[min_rpg_place] = [y,x-1,False]#True and False для направления ракеты. True - вправо, False - влево.
            world[y][x-1] = 5
            min_rpg_place += 1
            kol_rpg_sc += 1
        elif(way == '|tp' and ShowPanelCreator == True):#Команды разработчика
            xf = int(input())
            yf = int(input())
            if(world[yf][xf] == 0):
                x = xf
                y = yf
                jump = False
            else:
                print('error')
        elif(way == 'i'):#Инвентарь
            inp = int(input("1 - кирка, 2 - блоки, 3 - рпг: "))
            invent_on = inp
        elif(way == 'ShowPanelCreator'):
            ShowPanelCreator = True
        elif(way == 'res'):#Перезагрузка игры
            for i in range(0,8):#Очистка мира
                for j in range(1, 42):
                    world[i][j] = 0
            world[y][x] = 0
            reset = True
            start_game = False
        elif(way == 'ID'):
            for i in range(0,9):
                for j in range(0,45):
                    if(world[i][j] != 9):
                        print(world[i][j])
                    else:
                        print(0)
            input("Нажмите любую кнопку для продолжения")
        
            
        if(x1 != x or y1 != y):#Удаление игрока с прежнего места
            world[y1][x1] = 0
        
        #установка игрока
        if(reset != True):
            world[y][x] = 9
        #обновление экрана
        time.sleep(0.1)
        os.system('cls')
