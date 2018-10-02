# TODO LIST:
'''
• Gamemode (Summoner's Rift)
• Champ Select
• Lane Select (No JG)
• Laning Phase (Attack champ or minion)
• Teamfight Phase
• End Game
• Win
'''
from lot_core import champion_list, champions, number_test, get_champion_data

print('You have selected: Summoner\'s Rift')
print('Now let\'s choose a gamemode number!\n'
	'1) Blind Pick\n'
	'2) Ranked Solo [CLOSED]')
gamemode = number_test('gamemode', 1, 2)


if gamemode == 1:
	print('You have selected: Blind Pick')

	print('Select a champion:')
	champion_list()
	while True:
		user_champion = input('> ')
		if user_champion.capitalize() in champions:
			break
		else:
			print('That\'s not a valid champion!')

	print('Select a lane:\n'
		'1) TOP\n'
		'2) MID\n'
		'3) BOT\n'
		'4) SUP\n'
		'5) JNG')
	lane = number_test('lane', 1, 5)

	champion_data = get_champion_data(user_champion.lower(), 1)
