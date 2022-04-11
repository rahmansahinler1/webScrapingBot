from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random

# start web browse
browser = webdriver.Chrome()

# putting url into a variable
URL =("https://www.youtube.com/live_chat?is_popout=1&v=gh-IsBGAUCY")

# creating keywords
keyword1 = "hello"
keyword2 = "Hello"

# creating winners set
winners = set()

def getHTML(url):        
    # get source code, opens it in chromedriver
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    return html

def parseHTML(html_source):
    # parse HTML         
    return BeautifulSoup(html_source, 'html5lib')
    
def getMessages(soup):
    # get youtube messages
    return soup.find_all("yt-live-chat-text-message-renderer")
    
def updateWinners(messages):
    # updating winners    
    for message in messages:
        content = message.find("div", {"id": "content"}).text
        author = message.find("span", {"id": "author-name"}).text
        message_content = message.find("span", {"id": "message"}).text
        if (keyword1 in message_content or keyword2 in message_content):
            winners.add(author)

def startDrawing(winnersList):
    
    print("Toplam katilimci sayisi = {}".format(len(winners))) 
    time.sleep(5)  
    
    for i in range(1,5):
        noktalar = "." * i
        print("Drawing starts!" + noktalar)
        time.sleep(1.5)
        
    if len(winners) != 0:
        print("AND THE WINNER IS!!!!:",random.choice(winnersList))
    else:
        print("no winner")
        
def main():
    for i in range(0,5):
        html_source = getHTML(URL)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateWinners(messages)
        print("{} amount of person has assigned to drawing."
              .format(len(winners)))
        time.sleep((10))

    winnersList = list(winners)
    startDrawing(winnersList)
    browser.close()
    
main()

            
    
        
        
        
        