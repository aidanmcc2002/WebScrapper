from bs4 import BeautifulSoup as soup  # HTML data structure
import urllib.request

page_url = str(input("Please enter the url you would like to scrap: "))
choice = str(input("Type amazon  if its an amazon url or   newegg if its a newegg url: "))
# page_url = "https://www.newegg.com/p/pl?d=rx+5700+xt"
proxy = urllib.request.ProxyHandler({'http': '103.247.23.51:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
uClient = urllib.request.urlopen(page_url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
print(page_soup)
if choice == "newegg":
    containers = page_soup.findAll("div", {"class": "item-container"})
    out_filename = "graphics_cards.csv"
    headers = "brand,product_name,shipping \n"

    f = open(out_filename, "w")
    f.write(headers)
    print('got here')

    for container in containers:
        make_rating_sp = container.div.select("a")
        try:
            brand = make_rating_sp[0].img["title"].title()
            product_name = container.div.select("a")[2].text

            shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

            print("brand: " + brand + "\n")
            print("product_name: " + product_name + "\n")
            print("shipping: " + shipping + "\n")


            f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")
        except: #this stops the adding of data which isn't in the correct format
            continue

    f.close()  # Close the file
elif choice == "amazon":
    print(len(page_soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'})))

