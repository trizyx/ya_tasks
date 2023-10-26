first_str = input()
second_str = input()
with open('recipe.txt', 'w') as file:
    print(f'Рецепт\n'
          f'Выписан {first_str}\n'
          f'Прописано: по {second_str} касторки 3 раза в день.\n'
          f'Подпись: доктор Пилюлькин.', file=file)
