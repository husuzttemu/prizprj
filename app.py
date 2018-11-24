#import libraries

from search_engine.engine import Engine


from locators import page_locators

import re
#print(pagecontent)

#test
#print(simple_soup)

'''
def parse_products(e):
    #xyz = BeautifulSoup(text, "html.parser")
    text = e.select_one("input.product_id")
    id = text.attrs['value']
    text = e.select_one("form.basket-process")
    name = text.attrs['data-product-name']
    price = text.attrs['data-price']
    unit = text.attrs['data-unit']
    print(f'id={id} name={name} price={price}')
'''




#Ana sayfadan ürün kategorilerini parse ederek gideceği sayfaları bulur.


    #page_list = list(set([e.select_one('a').attrs['href'] for e in pages]))
    #print(page_list)





#print(page_locators.PageLocators.CONTAINER)
#print(simple_soup.find('div.container'))

#find_product_list()
#find_pages('https://www.sanalmarket.com.tr/arama?q=komili')


myEngine = Engine()
#print(myEngine.__doc__)
myEngine.find_products_from_all_categories()
#myEngine.find_pages_from_categories("https://www.sanalmarket.com.tr/gunes-bakim-c-94")


#myEngine.find_pages('https://www.sanalmarket.com.tr/arama?q=komili')

#client = MongoClient()
#client = MongoClient('mongodb://localhost:5500/')


#data = dict({"name":"Meral","age":39})



#db.products.insert_one(data)




"""
mylist = '''<li class="active"><a data-page="1">
        1 <span class="sr-only">(current)</span></a></li>, <li class=""><a data-page="2">
        2 <span class="sr-only">(current)</span></a></li>, <li class=""><a data-page="3">
        3 <span class="sr-only">(current)</span></a></li>, <li>...</li>, <li><a data-page="14"> 14</a></li>, <li class="pag-next"><a aria-label="Next" data-page="2"><i class="icon page-r-arrow"></i></a></li>'''
"""
#print(mylist)
