from django.core.management.base import BaseCommand
import requests as rq
from datetime import datetime
from bs4 import BeautifulSoup as bsoup
import lxml

#test command, see if I can pull in new data sourcee
class Command(BaseCommand):
    """custom commandline command that scrapes
        info from a website 
        """
    help = "collect incidents"

    def add_arguments(self, parser):
        
        # Named (optional) arguments
        parser.add_argument(
            '-u',
            action='store',
            dest='url',
            #change 'default' to hardcode another webpage
            default='https://m.livep2000.nl/',
            help='add url of page to be scraped',
        )
       

    # define logic of command
    def handle(self, *args, **options):
        
        #get data
        URL = options.get("url")

        xml_data = rq.get(URL).content
        # print(xml_data)
        # convert to soup
        soup = bsoup(xml_data,"xml")
        print(soup)
    
        # print(soup)

        incident_data = soup.find_all("id='datacontainer'")

        
        # # grab all incidents, met toebehoren
        # incident_messages = soup.find_all("item")

        # # start dataframe
        # incidents_data = pd.DataFrame() 


#binnentrekken
# in df zetten. 
# print