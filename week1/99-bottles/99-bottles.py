def take_one_down(beer_num):
    beer_count = beer_num

    while beer_count > 1:
        print(f'\n{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.\nTake one down and pass it around, {beer_count - 1} bottles of beer on the wall.\n')
        beer_count -= 1
    print(f'{beer_count} bottle of beer on the wall, {beer_count} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n')
    beer_count = 99
    run_again = input('More beer? ')
    if run_again == 'yes' or run_again == 'y' or run_again == 'YES':
        take_one_down(beer_num = int(input('\nHow many beers?')))
    else:
        print('\nGo home you\'re drunk!\n')

take_one_down(beer_num = int(input('\nHow many beers? ')))