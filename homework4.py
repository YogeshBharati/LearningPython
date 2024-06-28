Elect_bill = {
   'jan': 100,
   'feb': 200,
   'mar': 300,
   'apr': 400,
   'may': 500,
   'jun': 600,
   'july': 700,
   'aug': 800,
   'sep': 900,
   'oct': 1000,
   'nov': 1100,
   'dec': 1200,
}
total = sum(Elect_bill.values())
print(f"the jan to dec Elect_bill expenses is {total}")
print(f"the jan to dec average Elect_bill expenses is {total/12}")

