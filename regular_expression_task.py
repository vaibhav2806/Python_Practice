# Given a string with lots of indian phone numbers starting from +91

import re

string = '''Were you to make up a random India phone number yourself, 
there is a high chance of your number ending up being valid. However, 
with Fake Numbers free and ethical service, 
you can have full confidence that all generated India telephone numbers are indeed 100% non-working. 
If you're still not convinced about how we can help.
+91-855-5324-100 +91-995-5572-297 +91-935-5552-613 +91-855-5578-112 +91-995-5588-033
+91-755-5570-308 +91-855-5325-056 +91-955-5563-250 +91-755-5484-844 +91-755-5610-072
+91-925-5586-208 +91-855-5740-885 +91-855-5364-577 +91-855-5576-369 +91-755-5395-174
+91-855-5804-967 +91-915-5550-493 +91-755-5543-790 +91-855-5334-913 +91-755-5753-968
+91-975-5589-768 +91-855-5529-767 +91-995-5543-446 +91-755-5783-462 +91-855-5707-145
+91-955-5573-838 +91-755-5441-774 +91-755-5184-225 +91-855-5559-730 +91-905-5517-204
+91-755-5927-801 +91-925-5579-344 +91-755-5882-915 +91-855-5146-483 +91-755-5700-364
+91-905-5523-335 +91-755-5424-722 +91-755-5800-790 +91-755-5716-319 +91-855-5576-133
'''

list = []
patt = re.compile(r'[+]\d{2}-\d{3}-\d{4}-\d{3}')

matches = patt.finditer(string)
for match in matches:
    list.append(match)
    print(list)