def get_player_info():
    '''Return a dictionary whose key/value pairs are player name/player number.'''

    player_info = {'Blake Atkinson': 82453,
                   'Mike Berg': 91988, 'Kyle Bottmeyer': 74699, 'Steve Braud': 16027, 'Dan Brooks-Wells': 79228,
                   'Ryan Brown': 77244,
                   'Mike Carman': 48559, 'Derek Cassel': 73385, 'Stephen Curry': 109496,
                   'Jamie Detwiler': 87677, 'HC Dewey': 62106, 'Andy DiFronzo': 31029, 'Mike Duerr': 95251,
                   'Ray Ducoat': 56246,
                   'Aaron Fahey': 44665, 'Mike Fonzo': 52199, 'Devin Frederick': 16287,
                   'Bradley Good': 81618, 'Rolph Graf': 55401,
                   'Hank Hendry': 49714, 'Bill Hettel': 54672, 'Elijah Hogan': 72527, 'Seth Hogan': 55386,
                   'Dylan Horst': 32599,
                   'Adam Kotchetovsky': 77856, 'Jon Kracht': 57567,
                   'Kevin Laboski': 9920, 'Dan Lackner': 76413, 'Dustin Leatherman': 45395, 'Hannah Leatherman': 45396,
                   'Justin Madore': 17035, 'Tony Manfra': 99094, 'Kyle McClure': 68213, 'Joe Mela': 2607,
                   'Cooper Michael': 64617, 'Paul Miller': 68214,
                   'Sean Momtahen': 52541, 'Gabe Monck': 75822, 'Tim Moyer': 84632,
                   'Justin Rosak': 98161, 'Cory Rowley': 97008,
                   'Mark Saraceno': 82817, 'Rick Sassaman': 50552, 'Scott Schultz': 56415, 'Adam Spier': 89785,
                   'Chris Villa': 58197,
                   'Jeff Wetherill': 78128, 'Karin Wolset': 66959
                    }

    return player_info


def get_player_rating(url):
    '''Function to return player rating scraped from PDGA website.'''

    import requests
    from bs4 import BeautifulSoup

    r = requests.get(url)  # pull html from website
    soup = BeautifulSoup(r.text, 'html.parser')  # format html

    try:
        rating = soup.find(class_='current-rating').get_text().split()[2]
    except:
        rating = 'EXPIRED'

    return rating


def print_info(info):
    '''Function to print a nested dictionary'''

    print('\n')
    print(f"{'Name':<25} {'PDGA #':<15} {'Rating'}")

    for key, vals in info.items():
        print(f"{key:<25} {vals['PDGA']:<15} {vals['rating']}")

    return None


def save_info(info, basesavename='pdga_ratings_'):
    '''Function to save player information into a text file.'''

    import datetime

    date = datetime.date.today().strftime('%m-%d-%Y')

    savename = basesavename + date + '.txt'

    info_string = 'Ratings as of ' + date + '\n'

    for keys, vals in info.items():
        info_string += f"\n{keys:<25} {vals['PDGA']:<15} {vals['rating']}"

    with open(savename, 'w') as open_file:
        open_file.write(info_string)

    print('Data saved to \'' + savename + '\'')

    return None


def main():
    '''Main function to scrape PDGA ratings.'''

    print('\nWelcome to the PDGA Ratings Grabber.')

    # For players of interest, assemble a dictionary of name and player number
    player_info = get_player_info()

    base_url = 'https://www.pdga.com/player/'

    info = {}
    print('\nScraping information for ...')
    for name, number in player_info.items():
        print(name)

        new_dict = {}
        new_dict['PDGA'] = number
        new_dict['rating'] = get_player_rating(base_url + str(number))

        info[name] = new_dict

    if str(input('\nFinished grabbing ratings.  View them?  (\'y\' for yes)  ')).upper() == 'Y':
        print_info(info)

    if str(input('\nSave data to file?  (\'y\' for yes)  ')).upper() == 'Y':
        save_info(info)

    print('Finished grabbin\'.  Bye!')
    return None


if __name__ == '__main__':
    main()