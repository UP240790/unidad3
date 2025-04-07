for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

for i in range(1, 8):
    print('#' * i)

for i in range(8):
    print('# ' * 8)

for i in range(11):
    print(f'{i} x {i} = {i*i}')

languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

for i in range(0, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)

sum_all = sum(range(101))
print(f'The sum of all numbers is {sum_all}.')

sum_evens = sum(range(0, 101, 2))
sum_odds = sum(range(1, 101, 2))
print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.')

fruits = ['banana', 'naranja', 'mango', 'limón']
fruits_reversed = []
for fruit in fruits:
    fruits_reversed.insert(0, fruit)
print(fruits_reversed)

languages_data = {
    'USA': ['English', 'Spanish'],
    'India': ['Hindi', 'English'],
    'China': ['Chinese'],
    # ... otros países y sus idiomas
}

total_languages = set()  # Usamos un conjunto para evitar duplicados
for country, langs in languages_data.items():
    total_languages.update(langs)

print(f'Total number of languages: {len(total_languages)}')


from collections import Counter

language_count = Counter(lang for langs in languages_data.values() for lang in langs)
most_common_languages = language_count.most_common(10)
print(f'The 10 most spoken languages are: {most_common_languages}')


countries_population = {
    'China': 1402112000,
    'India': 1366400000,
    'USA': 331002651,
    'Indonesia': 273523615,
    'Pakistan': 220892340,
    'Brazil': 212559417,
    'Nigeria': 206139589,
    'Bangladesh': 164689383,
    'Russia': 145934462,
    'Mexico': 128933000,
}

top_10_populous_countries = sorted(countries_population.items(), key=lambda x: x[1], reverse=True)[:10]
print(f'The 10 most populous countries are: {top_10_populous_countries}')