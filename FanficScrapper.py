import urllib
from bs4 import BeautifulSoup

''' Todo:
    add option to configure output directory
    add formatting, either retain HTML or use RTF '''

class FanficScrapper(object):
    def __init__(self, base_url, output_dir = ""):
        ''' Example base_url
            https://www.fanfiction.net/s/8361923/ 
            
            8361923 is the story id '''
            
        self.output_dir = output_dir
        
        if base_url[-1] == '/':
            self.base_url = base_url
        else:
            self.base_url = base_url + '/'
        
    def chapter_scrapper(self, chapterURL, chapterNumber):
        page = urllib.request.urlopen(chapterURL)
        soup = BeautifulSoup(page, 'html.parser')
         
        #storytext_box = soup.find('div', attrs = {'id': 'storytext'})
        #storytext = storytext_box.text
         
        storytext_box = soup.find_all('p')
        storytext = ""
         
        for paragraph in storytext_box:
            storytext += paragraph.text
            storytext += '\n\n'
         
        output = open(f"{chapterNumber}.txt", 'w')
        output.write(storytext)
        output.close()
        
    def scrap_story(self, startChapter, endChapter):
        if startChapter <= endChapter:
            for i in range(startChapter, endChapter + 1):
                self.chapter_scrapper(self.base_url + str(i), i)
        else:
            print("Error: Must start from earlier chapters to later ones!")

cetrus = FanficScrapper("https://www.fanfiction.net/s/8361923/")
cetrus.scrap_story(1,10)