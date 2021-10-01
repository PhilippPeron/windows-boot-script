"""Script that runs after every boot of windows.
Functionality:
- Check Updates on "ZHS Webpage"
- Check for new Cinema timeslots
"""

import urllib.request
from win10toast import ToastNotifier
import time


def check_word_in_website(website_name, url, words):
    """Checks if the word is in the url's html-text."""
    try:
        site = str(urllib.request.urlopen(url).read())
    except Exception:
        notify(f"Problem! Could not get html text of {website_name}!", " ")
        return

    for word in words:
        if word in site:
            print(f"'{word}' found on {website_name}")
            notify(f"'{word}' found on {website_name}", " ")
        else:
            print(f"'{word}' not found on {website_name}")


def notify(message_line_1, message_line_2):
    """Lets a notification pop up in Windows 10."""
    toaster = ToastNotifier()
    toaster.show_toast(message_line_1, message_line_2)


if __name__ == '__main__':
    # ZHS
    check_word_in_website(
        "ZHS",
        r"https://www.buchung.zhs-muenchen.de/angebote/aktueller_zeitraum_0/index.html",
        ['Wintersemester']
    )

    # Cinema Kinoprogramm
    check_word_in_website(
        "Cinema",
        r"https://www.cinema-muenchen.de/filme.html",
        ['16.09.21', 'James Bond', 'Top Gun', 'Maverick']
    )

