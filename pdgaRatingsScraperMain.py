import pdgaRatingsScraperFunctions as functs

def main():
    '''Main function to scrape PDGA ratings.'''

    functs.print_banner('Welcome to the PDGA Ratings Sraper')

    # For players of interest, assemble a dictionary whose keys are player names and values are PDGA number
    player_info, input_file = functs.get_player_info()

    base_url = 'https://www.pdga.com/player/'

    info = {}
    functs.print_banner('Scraping information for:')
    print('')

    for name, number in player_info.items():
        print(name)

        new_dict = {}
        new_dict['PDGA'] = number
        new_dict['rating'] = functs.get_player_rating(base_url + str(number))

        info[name] = new_dict

    functs.print_banner('Finished Scraping Ratings')

    if str(input('\nPrint them to debug screen?  (\'y\' for yes)\n> ')).upper() == 'Y':
        functs.print_nest_dict(info)

    if str(input('\nSave data to file?  (\'y\' for yes)\n> ')).upper() == 'Y':
        functs.save_info(info, input_file)

    functs.print_banner('Exiting PDGA Ratings Scraper.  Byeee.')

    return


if __name__ == '__main__':
    main()
