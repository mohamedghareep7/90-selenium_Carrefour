from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.carrefouregypt.com/mafegy/en/search?keyword=laptop")

pig_container = driver.find_element(By.XPATH , '//div[@class="flex w-full flex-col pl-xs md:pl-lg"]')
# print(pig_container.get_attribute("outerHTML"))

container = pig_container.find_elements(By.XPATH , './/div[@class="relative flex flex-col gap-xs group mr-xs rounded-lg border border-gray-50 p-xs pb-sm md:mr-md"]')

for items in container :

    description = items.find_element(By.XPATH, './/span[@class="font-medium line-clamp-2 text-left text-sm leading-4 md:text-lg md:leading-[18px]"]').text
    print("description :" , description)

    price = items.find_element(By.XPATH , './/span[@class="text-lg leading-5 font-bold md:text-xl"]').text
    print("price :" , price)

    try:
        price_befor_discount = items.find_element(By.XPATH , './/div[@class="text-sm leading-4 font-medium text-gray-500 text-left self-baseline line-through"]').text
        print("price befor discount :" , price_befor_discount)
    except:
        price_befor_discount = "no discount on item"
        print("price befor discount :" , price_befor_discount)

    products_link = items.find_element(By.XPATH , './/a[@href]').get_attribute("href")
    print("product link :" , products_link)

    product_image = items.find_element(By.XPATH , './/img[@src]').get_attribute("src")
    print("product image :" , product_image)

    print("="*20)
