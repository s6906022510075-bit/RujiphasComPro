heroes = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]
h2 = ['Dr. Strange', 'Black Panther', 'Captain America', 'Ant-Man',]

heroes.insert(0, h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Ant-Man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] = 'Wonder Woman'
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)

#2
#['Dr. Strange', 'Ironman', 'Black Panther', 'Thor', 'Hulk', 'Superman', 'Spiderman']
#['Dr. Strange', 'Ironman', 'Black Panther', 'Thor', 'Hulk', 'Spiderman', 'Ant-Man']
#['Ant-Man', 'Black Panther', 'Dr. Strange', 'Hulk', 'Ironman', 'Spiderman', 'Thor']
#['Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr. Strange', 'Black Panther', 'Ant-Man']
#['Wonder Woman', 'Spiderman', 'Ironman', 'Hulk', 'Dr. Strange', 'Black Panther', 'Ant-Man']
#['Wonder Woman', 'Spiderman', 'Ironman', 'Hulk', 'Dr. Strange', 'Black Panther', 'Ant-Man']
#['Wonder Woman', 'Spiderman', 'Ironman', 'Hulk', 'Dr. Strange', 'Black Panther', 'Ant-Man']
#['Hanuman', 'Spiderman', 'Ironman', 'Hulk', 'Dr. Strange', 'Black Panther', 'Ant-Man']