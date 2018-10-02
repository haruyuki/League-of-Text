# League of Legends - Text Version
import random, math, linecache
from lot_core import number_test

print('Welcome to League of Legends - Text Version\n'
	'Latest patch notes:')
for i in range(1,6):  # Prints out first 5 lines from patches.txt
	print(linecache.getline('patches.txt', i), end='')

print('\nLet\'s begin with a choosing a map!\n'
	'1) 5v5 | Summoner\'s Rift\n'
	'   Crush your lane, dive into epic five-on-five\n'
	'   team fights, and destroy the enemy nexus in\n'
	'   League\'s premier competitive mode.\n\n'
	'2) 3v3 | Twisted Treeline [CLOSED]\n'
	'   NO INFO\n\n'
	'3) 5v5 | ARAM [CLOSED]\n'
	'   Ten randomly-selected champions assemble on a\n'
	'   narrow bridge in a frozen land. Cross to the\n'
	'   other side and destroy everything in your path.')

map_number = number_test('map number', 1, 3)

if map_number == 1:
	import summoners_rift
elif map_number == 2:
	import twisted_treeline
elif map_number == 3:
	import aram
