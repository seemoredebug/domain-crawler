import openai as openai

map_prompt = """
你是一款专业的语义搜索引擎，你的主要任务是进行高度相关的内容检索，你不需要直接解答问题。你需要从我给出的内容中抽取[商品信息]并通过[json]的形式进行展示。接下来你需要抽取的内容是
准确性：如实返回上下文中的内容，在无法找到相关文本的情况下，无需返回任意结果，只需简单回复“null”即可，不要编造任何信息。
一致性：json格式禁止新增字段或减少字段，必按照此格式[{"price":"","image":[],"title":"","description":"","service":{"cash on delivery":false,"free shipping":false},"contact":{"whatsapp":"","email":""},"SKU":[],"quantity":"","full_name":"","phone_number":"","shipping_address":"","shipping_fee":false,"payment_method":""}]。
============
内容：
The most fashionable bags
عربي
EN
New-Wehomeshop8
SAR
319
SAR
319.00
40% OFF
The most fashionable bags
🔥😍Bags carried by women all over the world, classic Chanel style, suitable for shopping and gatherings
Service
Cash on Delivery
Free Shipping
Genuine Guarantee
After-sales Service
Precautions
1. Click the Shop Now button and Choose your color and size (if so)
2. Fill in your name, phone number, delivery address, zip code
3. Click the Confirm button
PS: If there is no submission of order success page, please re-perfect your information, Click the confirm button again.
Any inquiry please
contact WhatsApp
8619032206570
or
email service@xplender.com with your full name and phone number,so we can help you in time.
Expected delivery time: about 10-20 days.
We are always committed to providing you with a better shopping experience. In order to make your store the first choice, we have collected the most popular and latest products from all over the world. If you want to know more about us, please click here
Placed the order means you agree to receive order status update and exclusive offers by SMS, Whatsapp or Email.
319
SAR
319.00
40% OFF
color
black
White
Brown
Red
Pink
Quantity
Full Name
*
Phone Number
*
966
Backup phone number (if available)
966
Shipping address
*
Street&Building(PACI NO)
*
Shipping Fee
Free Shipping
Payment Method
Cash on Delivery
Shipment
Returns
About Us
Privacy
Contact
Shop Now
提取结果:{"price":"319 SAR","image":[],"title":"The most fashionable bags","description":"🔥😍Bags carried by women all over the world, classic Chanel style, suitable for shopping and gatherings","service":{"cash on delivery":true,"free shipping":true},"contact":{"whatsapp":"8619032206570","email":"service@xplender.com"},"SKU":["black","White","Brown","Red","Pink"],"quantity":"","full_name":"","phone_number":"","shipping_address":"*","shipping_fee":true,"payment_method":"Cash on Delivery"}
"""


message="""
Little Green Citrus Dried Tangerine Peel Ferment Pu-erh – sinootea Skip to content Free shipping on orders over $99 🤩10% off on orders over $120🤩 HOME Tab 1 Image title Image title Image title Image title Heading Menu item 1 Heading Menu item 1 Heading Menu item 1 Heading Menu item 1 Tab 2 Tab 3 Shop Teas Pu-Erh Tea Herbals Black Tea Green Tea Wares Tea Filters & Strainers Tea Cups & Trays Tea Accessories & Tools Spring Blooms Hot Sale Tea Gifts New In Blog About Our Story Brand Intro
Log in
Facebook HOME Tab 1 Tab 2 Tab 3 Image title Image title Image title Image title Heading Menu item 1 Heading Menu item 1 Heading Menu item 1 Heading Menu item 1 Shop Teas Pu-Erh Tea Herbals Black Tea Green Tea Wares Tea Filters & Strainers Tea Cups & Trays Tea Accessories & Tools Spring Blooms Hot Sale Tea Gifts New In Blog About Our Story Brand Intro
Search
Log in
Cart
US DollarEuroBritish Pound SterlingCanadian DollarAustralian Dollar USD US Dollar Euro British Pound Sterling Canadian Dollar Australian Dollar Item added to your cart
Check out
Continue shopping Skip to product information Open media 1 in modal Open media 2 in modal Open media 3 in modal Open media 4 in modal Open media 5 in modal 1 / of
5 Little Green Citrus Dried Tangerine Peel Ferment Pu-erh Regular price
$164.99 USD
Regular price
$214.99 USD
Sale price
$164.99 USD
Unit price
/ per Sale Sold out Unit 500g Product variants 500g - $164.99 Quantity Decrease quantity for Little Green Citrus Dried Tangerine Peel Ferment Pu-erh
Increase quantity for Little Green Citrus Dried Tangerine Peel Ferment Pu-erh
Add to cart
Buy it nowMore payment options
Description：
Preferred authentic Xinhui citrus fruit and court-grade Pu'er tea materials, a blend of citrus fruit aroma and Yunnan Pu'er mellow aging aroma. Insist on using semi-raw tanning process to lock the citrus peel nutrition and ripe Pu-erh tea properties. The soup color is red and transparent, and the taste is crisp and sweet, with strong sweetness in the mouth, bringing soothing good mood. Share Share Link
Close share
Copy link
Subscribe to our emailsBe the first to know about new collections and exclusive offers. Email SHOP Search Pu'er tea Teaware ABOUT Our story Brand Intro Blog Payment Methods Privacy Policy Returns & Exchanges Terms & Conditions Contact
Email：app@myantdiy.com
Subscribe to our emails Email Facebook
Payment methods
© 2023, sinootea
Powered by Shopify
Choosing a selection results in a full page refresh.
"""


def ask_question(message):
    openai.api_key = "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"
    # chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    #                                                messages=[{"role": "user", "content": "Hello world"}])


    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo-16k",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": map_prompt},
            {"role": "user", "content": message},
        ]
    )

    # 获取模型的回复
    model_response =response['choices'][0]['message']['content']

    return model_response

if __name__ == '__main__':

    response = ask_question(map_prompt, message)
    print(response)