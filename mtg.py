from bs4 import BeautifulSoup
import string
import requests
import warnings
warnings.filterwarnings("ignore")

def magicmadhouse(card):
    a = card.replace(' ', '-').lower()
    c = "".join(z for z in a if z not in ('!','.',':',",","'"))

    r  = requests.get("http://www.magicmadhouse.co.uk/search/magic-the-gathering-c1/" + c)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    test = soup.findAll("div", { "class" : "product_details" })

    for n in range(len(test)):
        x = str(test[n].find({ "a" : "product_title"})).lower()[:-4]
        for k in range(3):
            x = x[x.index(">")+2:]
        if (x == card.lower() or x[:len(card)+2] == card.lower() + " ("):
            print x, ",", str(test[n].find("span",{ "class" : "GBP" }))[20:-7], ",", str(test[n].find("div",{ "class" : "product_stock_status" }))[35:-6]

def magicsingles(card):
    a = card.replace(',','%2C').replace(' ','+').lower()

    r  = requests.get("http://www.magicsingles.co.uk/index.php?subcats=N&status=A&pshort=N&pfull=N&pname=Y&pkeywords=N&search_performed=Y&match=all&q=" + a + "&dispatch[products.search]=Search")
    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    test = soup.findAll("div", { "class" : "prod-info" })

    for n in range(len(test)):
        x = str(test[n].findAll("span", {"class" : "price-num"})[1])
        y = str(test[n].find("span",{ "class" : "qty-in-stock"}))
        z = str(test[n].find("a",{ "class" : "product-title"}))
        z = z[z.index(">")+1:-4].lower()
        if y != "None":
            y = y[y.index(">")+39:-40]
        if y[0] == "�":
            y = "1" + y[1:]
        if(z == card.lower() or z[:len(card)+2] == card.lower() + " (" or z[:len(card)+2] == card.lower() + " /"):
            print z, ",", "�" + x[x.index(">")+1:-7] , ",", y.replace("�","")

def trolltrader(card):
    a = card.replace(',','%2C').replace(' ','+').lower()

    r  = requests.get("http://www.trolltradercards.com/products/search?q=" + a)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    test = soup.findAll("li", { "class" : "product"})

    for n in range(len(test)):
        x = str(test[n].find("span", {"class" : "price"}, {"itemprop" : "price"}))
        y = str(test[n].find("span",{ "class" : "qty"}))
        z = str(test[n].find("h4", {"class" :"name"}))
        z = z[z.index(">")+1:-5].lower()
        if y != "None":
            y = "".join(y[y.index(">")+1:-7].split())
        else:
            y = "0instock"
        if(z == card.lower() or z[:len(card)+2] == card.lower() + " -" or z[:len(card)+2] == card.lower() + " /"):           
            print z, ",", "".join(x[x.index(">")+1:-7].split())[1:], ",", y[:-7], "in stock"

def manaleak(card):
    a = card.replace(',','%2C').replace(' ','+').lower()

    r  = requests.get("http://www.manaleak.com/magic-the-gathering/advanced_search_result.php?keywords=" + a)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")    

    test = soup.findAll("div", { "class" : "product_info_wrapper"})
    test = test[:-8]

    for n in range(len(test)):
        x = str(test[n].find("span", {"class" : "productSpecialPrice"}))[35:-7]
        y = str(test[n].find("button", {"class" : "pull-left qty_change qty_minus"}))[61]
        z = str(test[n].find("h3", {"class" : "product_name_wrapper name equal-height_listing_name"}))[70:-16]
        z = z[z.index(">")+1:].lower()

        if(z == card.lower() or z[:len(card)+2] == card.lower() + " -" or z[:len(card)+2] == card.lower() + " /" or z[:len(card)+2] == card.lower() + " ("): 
            print z, ",", x,",", y, "in stock"
    
    
a = raw_input("Enter a card name: ")

def magiccardtrader(card):
    a = card.replace(',','%2C').replace(' ','+').lower()

    r  = requests.get("http://www.themagiccardtrader.com/products/search?query=" + a + "&x=0&y=0")
    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    test = soup.findAll("tr", { "class" : "product_row"})

    for n in range(len(test)):
        print str(test[n].find("td", {"class" : "qty"}))
        print str(test[n].find("a href"))
    
print "\nMagicSingles:\n"   
#magicsingles(a)

print "\nTrollTraders:\n"
#trolltrader(a)

print "\nManaLeak:\n"
#manaleak(a)

print "\nMagicMadhouse:\n"
#magicmadhouse(a)

print "\nTheMagicCardTrader:\n"
magiccardtrader(a)
