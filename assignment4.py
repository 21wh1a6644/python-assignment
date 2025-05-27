class OrgUnit:
    count_units = 0 

    def __init__(self, unit_code, unit_name, unit_place, unit_head):
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_place = unit_place
        self.unit_head = unit_head
        OrgUnit.count_units += 1

    def show_details(self):
        print(f"\nUnit Code       : {self.unit_code}")
        print(f"Unit Name       : {self.unit_name}")
        print(f"Location        : {self.unit_place}")
        print(f"Head of Unit    : {self.unit_head}")



unit_list = []


total = int(input("How many organizational units to enter? "))


for index in range(total):
    print(f"\nEnter info for unit {index+1}:")
    code = input("Unit Code: ")
    name = input("Unit Name: ")
    place = input("Location: ")
    head = input("Head of Unit: ")
    unit_obj = OrgUnit(code, name, place, head)
    unit_list.append(unit_obj)


print("\n=== Organization Units ===")
for unit in unit_list:
    unit.show_details()


lookup_code = input("\nEnter Unit Code to search: ")
found_flag = False
for unit in unit_list:
    if unit.unit_code == lookup_code:
        print("\nUnit found:")
        unit.show_details()
        found_flag = True
        break
if not found_flag:
    print("No unit with that code found.")

search_term = input("\nEnter name part to search (startswith/in/endswith): ").lower()
print("\nUnits matching your search:")
matched = 0
for unit in unit_list:
    name_lower = unit.unit_name.lower()
    if (name_lower.startswith(search_term) or
        search_term in name_lower or
        name_lower.endswith(search_term)):
        unit.show_details()
        matched += 1

if matched == 0:
    print("No units match the given name.")
else:
    print(f"\nTotal matching units: {matched}")

print(f"\nTotal Organizational Units: {OrgUnit.count_units}")
