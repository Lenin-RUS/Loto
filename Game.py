import numpy as np


class meshok():
    def __init__(self):
        numbers = np.arange(1,91)
        np.random.shuffle(numbers)
        self.numbers=numbers
        self.current_barrel=0
    def get_barrel(self, next_barrel):
        self.current_barrel=self.numbers[next_barrel]   #<---- Чет перебор

class card():
    def __init__(self, user):
        numbers = np.arange(1,91)
        np.random.shuffle(numbers)
        z=np.sort(numbers[:15])
        while len(z)<27:
            z=np.insert(z, np.random.randint(0,len(z)), 0)
        self.numbers=z
        self.state=1
        self.user=user

    def show_card(self):
        numbers_with_zerros=list(map(lambda x:str(x) if x>0 else '--', self.numbers))
        print(f'------карточка {self.user}------')
        for i,j in enumerate(numbers_with_zerros):
            if i%9==0 and i!=0 or i==27: print('')
            print('', j, end=' ') if len(j)==1 else print (j , end =' ')
        print()
        print('--------------------------')

    def check_number(self, number, Player):
        self.show_card()
        if Player.player_type == 1:
            if number in self.numbers:
                index_of_number = np.where(self.numbers == number)
                self.numbers[index_of_number]=0
                print(f'{Player.name} зачеркнул свою цифру')
            else:
                print(f'У {Player.name} нет такой цифры')
        else:
            answer=(input(f'{Player.name}, зачеркнуть цифру {number} ? (y/n): ')=='y')
            if answer and number in self.numbers:
                index_of_number = np.where(self.numbers == number)
                self.numbers[index_of_number]=0
            elif not answer and number not in self.numbers:
                pass
            else:
                print(f'{Player.name}, ты слепой? Ты проиграл кароч.')
                Player.player_status=0

class user():
    def __init__(self, name, player_type):
        self.name = name
        self.player_type=player_type
        self.player_status=1




print('__________________ (((СУПЕР ИГРА ЛОТО )))_______________________')
max_players=int(input('Введите количество игроков: '))
Players=[]
cards=[]
winners=[]
#заводим игроков и для них карточки

for i in range(max_players):
    Player_name=input(f'Введите имя игрока #{i+1}: ')
    Player_type=int(input(f'Введите тип игрока {Player_name} (1-комп, 0-юзер): '))
    while Player_type not in (0,1):
        print('Тип пользователя неверный. Попробуйте еще раз')
        Player_type=int(input(f'Введите тип игрока {Player_name} (1-комп, 0-юзер): '))
    Players.append(user(Player_name, Player_type))
    cards.append(card(Player_name))
    cards[i].show_card()

#мутим мешок

our_bag=meshok()

print('__________________ ((((НАЧАЛО ЗАМЕСА))))_______________________')
winner_defined=False
turn=0
while not winner_defined:
    our_bag.get_barrel(turn)
    barrel=our_bag.current_barrel
    print('Мешаем мешок и достаем бочонок с номером', barrel)

    # сперва идем по игрокам юзерам
    for Player_Card, Player in enumerate(Players):
        if Player.player_type==0 and Player.player_status==1:
            print(f'----------------------------------Ход игрока {Player.name}')
            cards[Player_Card].check_number(barrel, Player)

    # потом идем по игрокам компам
    for Player_Card, Player in enumerate(Players):
        if Player.player_type==1 and Player.player_status==1:
            print(f'--------------------------------- Ход компа {Player.name}')
            cards[Player_Card].check_number(barrel, Player)

    print(f'Итоги {turn+1} тура:')

    for j, loto_card in enumerate(cards):
        print(f'Игорок {loto_card.user} - осталось {len(loto_card.numbers.nonzero()[0])} незакрытых позиций')
        if len(loto_card.numbers.nonzero()[0])==0:
            Players[j].player_status=2
            winners.append(loto_card.user)
    if len(winners)==1:
        print(f'У нас победитель - Игорок {winners[0]}!!! \n Игра окончена!!!')
        winner_defined=True
    if len(winners)>1:
        print(f'У нас победители - Игороки {list(winners)}!!! \n Игра окончена!!!')
        winner_defined=True
    turn+=1




