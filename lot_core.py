champions = ['Annie',
	'Ashe',
	'Garen',
	'Teemo',
	]

top_champions = ['Aatrox', 'Camille', 'Cho\'Gath', 'Darius', 'Dr. Mundo', 'Fiora', 'Galio', 'Garen', 'Gnar', 'Gragas', 'Illaoi', 'Irelia', 'Jarvan IV', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Malphite', 'Mordekaiser', 'Nasus', 'Nunu', 'Olaf', 'Pantheon', 'Poppy', 'Renekton', 'Riven', 'Rumble', 'Shen', 'Singed', 'Sion', 'Swain', 'Teemo', 'Tryndamere', 'Urgot', 'Yorick']
mid_champions = ['Ahri', 'Akali', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Brand', 'Cassiopeia', 'Corki', 'Diana', 'Ekko', 'Fizz', 'Gangplank', 'Heimerdinger', 'Karthus', 'Kassadin', 'LeBlanc', 'Lissandra', 'Lux', 'Orianna', 'Quinn', 'Ryze', 'Syndra', 'Taliyah', 'Talon', 'Twisted Fate', 'Veigar', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Zed', 'Ziggs', 'Zilean']
bot_champions = ['Ashe', 'Caitlyn', 'Draven', 'Ezreal', 'Jhin', 'Jinx', 'Kalista', 'Katarina', 'Kog\'Maw', 'Lucian', 'Miss Fortune', 'Sivir', 'Tristana', 'Twitch', 'Varus', 'Vayne', 'Xayah']
sup_champions = ['Alistar', 'Blitzcrank', 'Braum', 'Janna', 'Karma', 'Leona', 'Lulu', 'Malzahar', 'Maokai', 'Morgana', 'Nami', 'Nautilus', 'Rakan', 'Sona', 'Soraka', 'Tahm Kench', 'Taric', 'Thresh', 'Trundle', 'Volibear', 'Zyra']
jng_champions = ['Amumu', 'Elise', 'Evelynn', 'Fiddlesticks', 'Graves', 'Hecarim', 'Ivern', 'Kha\'Zix', 'Kindred', 'Lee Sin', 'Master Yi', 'Nidalee', 'Nocturne', 'Rammus', 'Rek\'Sai', 'Rengar', 'Sejuani', 'Shaco', 'Shyvana', 'Skarner', 'Udyr', 'Vel\'Koz', 'Vi', 'Warwick', 'Wukong', 'Xin Zhao', 'Zac']

'''
	champions = ['Aatrox',
	'Ahri',
	'Akali',
	'Alistar',
	'Amumu',
	'Anivia',
	'Annie',
	'Ashe',
	'Aurelion Sol',
	'Azir',
	'Bard',
	'Blitzcrank',
	'Brand',
	'Braum',
	'Caitlyn',
	'Camille',
	'Cassiopeia',
	'Cho\'Gath',
	'Corki',
	'Darius',
	'Diana',
	'Dr. Mundo',
	'Draven',
	'Ekko',
	'Elise',
	'Evelynn',
	'Ezreal',
	'Fiddlesticks',
	'Fiora',
	'Fizz',
	'Galio',
	'Gangplank',
	'Garen',
	'Gnar',
	'Gragas',
	'Graves',
	'Hecarim',
	'Heimerdinger',
	'Illaoi',
	'Irelia',
	'Ivern',
	'Janna',
	'Jarvan IV',
	'Jax',
	'Jayce',
	'Jhin',
	'Jinx',
	'Kalista',
	'Karma',
	'Karthus',
	'Kassadin',
	'Katarina',
	'Kayle',
	'Kennen',
	'Kha\'Zix',
	'Kindred',
	'Kled',
	'Kog\'Maw',
	'LeBlanc',
	'Lee Sin',
	'Leona',
	'Lissandra',
	'Lucian',
	'Lulu',
	'Lux',
	'Malphite',
	'Malzahar',
	'Maokai',
	'Master Yi',
	'Miss Fortune',
	'Mordekaiser',
	'Morgana',
	'Nami',
	'Nasus',
	'Nautilus',
	'Nidalee',
	'Nocturne',
	'Nunu',
	'Olaf',
	'Orianna',
	'Pantheon',
	'Poppy',
	'Quinn',
	'Rakan',
	'Rammus',
	'Rek\'Sai',
	'Renekton',
	'Rengar',
	'Riven',
	'Rumble',
	'Ryze',
	'Sejuani',
	'Shaco',
	'Shen',
	'Shyvana',
	'Singed',
	'Sion',
	'Sivir',
	'Skarner',
	'Sona',
	'Soraka',
	'Swain',
	'Syndra',
	'Tahm Kench',
	'Taliyah',
	'Talon',
	'Taric',
	'Teemo',
	'Thresh',
	'Tristana',
	'Trundle',
	'Tryndamere',
	'Twisted Fate',
	'Twitch',
	'Udyr',
	'Urgot',
	'Varus',
	'Vayne',
	'Veigar',
	'Vel\'Koz',
	'Vi',
	'Viktor',
	'Vladimir',
	'Volibear',
	'Warwick',
	'Wukong',
	'Xayah',
	'Xerath',
	'Xin Zhao',
	'Yasuo',
	'Yorick',
	'Zac',
	'Zed',
	'Ziggs',
	'Zilean',
	'Zyra'
	]
'''

def number_test(game_type, min_value, max_value):
	while True:
		try:
			user_input = int(input('> '))
		except ValueError:
			print('Thats not a number!')
		else:
			if user_input < min_value or user_input > max_value:
				print('That ' + game_type + ' doesn\'t exist!')
			else:
				return user_input
				break

def luck(chance):
	number = math.ceil(chance/2)
	value = random.randint(0,chance)
	if value == number:
		return 1
	else:
		return 0

def champion_list(*banned_champions):
	banned = list(banned_champions)
	print(banned)
	for a,b,c in zip(champions[::3],champions[1::3],champions[2::3]):
		print('{:<30}{:<30}{:<}'.format(a,b,c))

def get_champion_data(champion, level):
	level -= 1
	filename = 'champions/' + champion.lower() + '.txt'
	f = list(open(filename))
	data = [s.replace('\n','') for s in f]
	epithet = data[0]
	attack_type = int(data[1])
	resource_type = int(data[2])
	health = int(data[3].split()[level])
	health_regen = float(data[4].split()[level])
	resource = int(data[5].split()[level])
	resource_regen = float(data[6].split()[level])
	attack_damage = float(data[7].split()[level])
	base_attack_speed = float(data[8])
	bonus_attack_speed = float(data[9].split()[level])
	armor = float(data[10].split()[level])
	magic_resist = float(data[11].split()[level])
	attack_range = int(data[12])
	movement_speed = int(data[13])
	return epithet, attack_type, resource_type, health, health_regen, resource, resource_regen, attack_damage, base_attack_speed, bonus_attack_speed, armor, magic_resist, attack_range, movement_speed
		
