import csv
import json
data=[]
with open('C:/Users/Nidhisha Shetty/Desktop/test.csv','rt', encoding='utf8') as f:
  reader = csv.reader(f, skipinitialspace=True)
  data.append(tuple(next(reader)))
  for year, company, revenue in reader:
        data.append((int(year), company, int(revenue)))
res=[]
for x in range(16):
	a=list(data[x])
	res.append(a)

eka=res[13]
dvi=res[14]
tri=res[15]
chatur=res[12]

di={eka[1]:eka[2], dvi[1]:dvi[2],tri[1]:tri[2],chatur[1]:chatur[2]}
di_1={'eka':5, 'dvi':6, 'tri':3, 'chatur':4}

def projected_revenue(company_name, year):
	if year<2031:
		year_dif=year-2019
		if company_name in di:
			amount_2019=di[company_name]
			if company_name in di_1:
				growth_percent=di_1[company_name]
				for x in range(year_dif):
					interest=((amount_2019*growth_percent)/100)
					new_amount=amount_2019+interest
					amount_2019=new_amount
				return(round(amount_2019,2))
	else: 
		return("not available beyond 2030")
revenue=projected_revenue('tri', 2031) 
print("The future revenue of the company, "+str(revenue))

#   for row in data:
#   	print(type(row[0]))
#   	res=row
#   	year=(res[0])
#   	company=(res[1])
#   	revenue=(res[2])
#   	li_year=list(year)
#   print(type(row))



# def projected_revenue(company_name, year):
# 	for x in company:
# 		if x==company_name:
# 			print("yay")
# 		else:
# 			break






# res=projected_revenue('eka', 2021)