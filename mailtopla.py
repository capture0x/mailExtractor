import requests
from bs4 import BeautifulSoup
import re
import enteryyy


def mailExtractor(searchh, pageNumber):
    try:
        sayac = 0
        while sayac < int(pageNumber):
            url = f"https://yandex.com.tr/search/?lr=11501&text={searchh}&p={sayac}"
            sayac += 1
            istek = requests.get(url)
            s = BeautifulSoup(istek.text, "lxml")
            text = s.text
            result = re.findall(r'[\w.-]+@[\w.-]+', text)
            with open("mail.txt", "a+") as f:
                for i in result:
                    f.writelines(i + "\n")
                    print(i)
        print("\n--> Results saved in 'mail.txt' file..")
        print("--> Happy Hacking...")
    except:
        print(" incorrect Entry!!!")
        mailExtractor(searchh=input("(ex:business newyork '@gmail.com' site:instagram.com)\nEnter \t:"),
                      pageNumber=input("Enter the number of pages :"))


mailExtractor(searchh=input("(ex:business newyork '@gmail.com' site:instagram.com)\nEnter \t:"),
              pageNumber=input("Enter the number of pages :"))
