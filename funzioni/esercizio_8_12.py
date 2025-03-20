def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredients in ingredients:
        print(f"{ingredients}")
    print("il tuo panino è pronto \n")

make_sandwich('mozzarella ', 'prosciutto ', 'pomodoro')
make_sandwich('salame', 'lattuga')
make_sandwich('nutella', 'burro arachidi')
