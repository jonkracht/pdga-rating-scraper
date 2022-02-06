import requests
from bs4 import BeautifulSoup

def print_banner(text, character='*', width=100, gap=3):
    '''Standardized banner printing.'''

    leftFill = int((width - len(text) - 2 * gap)/2)
    rightFill = width - leftFill - len(text) - 2 * gap

    print('\n' + width * character)
    print(leftFill * character + ' ' * gap + text + ' ' * gap + rightFill * character)
    print(width * character)

    return


def save_info(info_dict, input_file):
    '''Function to save player information into a text file.'''

    import datetime

    print_banner('Saving Ratings')

    date = datetime.date.today().strftime('%m-%d-%Y')

    # Use name of file containing player info and date to create new filename
    default_name = input_file + '-ratings-' + date

    name = input(f'\nEnter file name or type \'ENTER\' to use the default (\'{default_name}.txt\'):\n> ')

    if name == '':
        name = default_name

    info = 'Ratings as of ' + date + '\n'

    for keys, vals in info_dict.items():
        info += f"\n{keys:<25} {vals['PDGA']:<15} {vals['rating']}"

    with open(name + '.txt', 'w') as open_file:
        open_file.write(info)

    print('\nData saved to \'' + name + '.txt\'')

    return


def print_nest_dict(info):
    '''Function to print a nested dictionary.'''

    print('\n')
    print(f"{'Name':<25} {'PDGA #':<15} {'Rating'}")  # print header row

    for key, vals in info.items():
        print(f"{key:<25} {vals['PDGA']:<15} {vals['rating']}")

    return None


def get_player_rating(url):
    '''Function to scrape a player rating from pdga.com'''

    r = requests.get(url)  # pull html from website
    soup = BeautifulSoup(r.text, 'html.parser')  # format html

    # Use try/except to handle expired accounts
    try:
        rating = soup.find(class_='current-rating').get_text().split()[2]
    except:
        rating = 'EXPIRED'

    return rating


def get_player_info():
    '''
    Return a dictionary whose key/value pairs are player names and numbers.
    '''

    defaultFile = 'sample-players'
    filename = input(f'\nEnter text file containing player info or hit \'ENTER\' to use the default (\'{defaultFile}.txt\'):\n> ')

    # Handle various forms of input
    if filename == '':
        filename = defaultFile

    print(f'\nUsing contents of \'{filename}.txt\'')

    with open(filename + '.txt', 'r') as open_file:
        newList = open_file.read().split('\n')

    # Create dictionary
    player_info = {}
    for line in newList:
        info = line.split(':')
        if len(info) == 2:
            player_info[info[0].strip()] = info[1].strip()

    return player_info, filename


if __name__ == '__main__':
    '''A few functions calls to test their operation'''

    player_info = get_player_info()

    print('Finished.')