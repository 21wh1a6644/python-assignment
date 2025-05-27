''''
inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

calculate the TotalRevenue
List Low stock item if stock is less than 5
calculte the categorywise Revenue

'''




l = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
#total revenue
t=0
for i in l:
    up=i[2]
    us=i[3]
    t=t+(up*us)
print("total revenue",t)
#low stock item stock is less than 5
l1=[]
for i in l:
    if i[-1]<5:
        l1.append(i[-1])
print("the low stock item",l1)

#calculate category wise revenue
c={}
tr=0
for i in l:
    category=i[1]
    up=i[2]
    us=i[3]
    tr=(up*us)
    if category in c:
        c[category]+=tr
    else:
        c[category]=tr
for category,tr in c.items():
    print(f'{category} : {tr:.2f}')



# with open('the-zen-of-python.txt') as f:
#     while True: 
#         lin