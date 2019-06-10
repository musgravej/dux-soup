import os
import csv
import sqlite3


def import_file(fle):
    with open(fle, 'r', encoding='UTF-8', newline="") as r:

        fields = ["id", "VisitTime", "Profile", "Picture", 
        "Degree", "First Name", "Middle Name", "Last Name", 
        "Summary", "From", "Title", "Company", "CompanyProfile", 
        "CompanyWebsite", "PersonalWebsite", "Email", "Phone", "IM", 
        "Twitter", "Location", "Industry", "My Tags", "My Notes"]

        csvr = csv.DictReader(r)
        for line in csvr:
            print("\t".join([line['First Name'],
                             line['Last Name'],
                             line['Title'],
                             line['Company'],
                             line['Email'],
                             '', '', '', '', '', '','',
                             line['Phone'], 'dux-soup 2019-06-10',
                             line['Profile'], line['CompanyWebsite']
                            ]))

def main():
    import_file(os.path.join(os.curdir, 
                             'orig','dux-soup-visit-data 1st marketing list.csv'))


if __name__ == '__main__':
    main()