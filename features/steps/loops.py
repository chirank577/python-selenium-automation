from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


click_colour_of_product= (By.CSS_SELECTOR, "div[aria-label='Carousel'] ul li img")
# color_word= (By.XPATH,"//div[@class='sc-40df79dd-0 facmsK sc-41939763-1 efecen h-padding-a-none h-padding-b-tiny']//div[@class='sc-40df79dd-1 kda-dqB']")
color_words= (By.CSS_SELECTOR, 'div[data-test="@web/VariationComponent"]:nth-of-type(2)')
color_word= (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
search_product= (By.CSS_SELECTOR,"input[data-test='@web/Search/SearchInput']")
click_search= (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
product_availability= (By.XPATH, "//div[@data-test='@web/site-top-of-funnel/ProductCardWrapper']")
product_title= (By.CSS_SELECTOR, "a[data-test='product-title']")

@given('Open Target product {Product_id} page')
def open_product_page(context, Product_id):
    context.driver.get(f'https://www.target.com/p/{Product_id}')
    sleep(8)

@then('Verify user can click through colours')
def click_colors(context):
    expected_colors= ['grey', 'black/gum','dark khaki','navy/tan','stone/grey', 'white/gum','white/navy/red', 'white/sand/tan']
    # expected_cls= ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors= []
    cls= context.driver.find_elements(*click_colour_of_product)

    for color in cls:
        color.click()
        sleep(3)
        selected_color = context.driver.find_element(*color_words).text
        # selected_color = selected_color[1]
        print(selected_color)

        selected_color=selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected{expected_colors} did not match {actual_colors}.'

@given('Open Target product {product_2} pages two')
def open_product_page(context, product_2):
    context.driver.get(f'https://www.target.com/p/{product_2}')
    sleep(8)

@then ('verify user can click through colours of pants')
def click_each_color(context):
    result=['Blue Tint', 'Denim Blue','Marine','Raven']

    expexted=[]
    cls_2=context.driver.find_elements(*click_colour_of_product)

    for color in cls_2:
        color.click()

        slected=context.driver.find_element(*color_word).text
        slected=slected.split('\n')[1]
        expexted.append(slected)
        print(expexted)

    assert expexted==result, f' did not match to result{expexted} {result}'


@then('Verify that every product on Target has a product name and product image')
def verify_product_shown(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    product_visible=context.driver.find_elements(*product_availability)
    # product_visible = context.driver.wait.until(EC.presence_of_all_elements_located(product_availability))
    for product in product_visible:
        title = product.find_element(*product_title).text
        assert title, f' product title now shown'
        print(title)
        product.find_element(By.CSS_SELECTOR, 'img')



