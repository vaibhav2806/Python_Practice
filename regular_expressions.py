import re

mystr = '''Share Register/Transfer Agent*
TSR Darashaw Limited (TSRDL)

Ph: +91-22-6656 8484

Fax: +91-22-6656 8494

Email: csg-unit@tsrdarashaw.com

Website: www.tsrdarashaw.com

Mailing Address:
6-10, Haji Moosa Patrawala 

Industrial Estate, 20, Dr E Moses Road, 

Mahalaxmi, Mumbai 400 001

*Please cite the folio numbers (if you hold physical shares) or the DP ID and Client ID (if your holdings are dematerialized) in all your correspondence.
Shareholder Grievance Redressal
Email: investor.relations@tcs.com
Mailing Address:
Tata Consultancy Services Limited

9th Floor, Nirmal Building, Nariman Point,

Mumbai  400 021, India

Ph: +91-22-6778 9595

      +91-22-6778 9191

      +91-22-6778 9179

Fax: +91-22-6630 3672

Financial Disclosure And Governance
V Ramakrishnan

Chief Financial Officer

 
Mailing Address:
Tata Consultancy Services Limited

TCS House, Raveline Street, Fort 

Mumbai  400 001, India

Ph: 91-22-6778 9999 

Fax: 91-22-6778 3000

Investor Relations
Kedar Shirali

Head, Global Investor Relations

Email: kedar.shirali@tcs.com
vavaibhav verma is a good booooooy'''

# findall, search, split, sub, finditer

# META CHARACTER

# patt = re.compile(r'vaibhav')
# patt = re.compile(r'.')                 # '.' means any character so it match everything..
# patt = re.compile(r'.good')             # it will return the position of good 
# patt = re.compile(r'^share')            # it will return nothing as string does't start whith share
# patt = re.compile(r'^Share')            # it will return the position of Share 
# patt = re.compile(r'va*')               # all the places where there is 1 'v' and zero and more 'a'
# patt = re.compile(r'oy$')               # if string ends with the particular character
# patt = re.compile(r'bo+')               # One or more occurrences  
# patt = re.compile(r'bo{2}')
# patt = re.compile(r'(va){2}')
patt = re.compile(r'va{2}|bo')            # either va or bo

# SPECIAL SEQUENCES

# patt = re.compile(r'\AShare')
# patt = re.compile(r'\Bva')
# patt = re.compile(r'\bFi')
patt = re.compile(r'\d{3} \d{3}')


matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[1049:1056])