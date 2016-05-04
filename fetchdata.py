""" Fetch geocoding data. """

from geocoding import (link, read_file, format_data, update_data,
                       geocoded_data)


if __name__ == '__main__':

    df = read_file(link)
    geodata_ref = format_data(df)
    geodata_ref = update_data(geodata_ref)

    result = geocoded_data(geodata_ref, df)
    result.to_csv('result.csv')

    
