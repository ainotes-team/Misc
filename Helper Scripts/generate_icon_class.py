import os

for x in os.listdir():
	if x.startswith("icons8-"):
		cs_name = x.replace("icons8-", "")[:-7]

		itms = []
		for itm in cs_name.split("-"):
			itms.append(itm[0].upper() + itm[1:])

		cs_name = ''.join(itms)
		res = """public static string {} => AddPrefix("{}");""".format(cs_name, x)
		print(res)