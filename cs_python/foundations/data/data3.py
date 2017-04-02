contact = ('first_name','last_name','mobile_phone','home_phone','zip_code')

FIRST_NAME = 0 
LAST_NAME = 1
MOBILE_PHONE = 2
HOME_PHONE = 3
ZIP_CODE = 4

def create_contact(first_name,last_name,mobile_phone,home_phone=None,zip_code=None):
    return (first_name,
            last_name,
            mobile_phone,
            home_phone,
            zip_code
            )


contacts = []

contacts_by_first_name = {}
contacts_by_last_name = {}
contacts_by_phone = {}
contacts_by_zip = {}


def add_contact(contact):
    index = len(contacts)
    contacts.append(contact)
    first_name = contact[FIRST_NAME]
    
    if first_name in contacts_by_first_name.keys():
        contacts_by_first_name[first_name].append(index)
    else:
        contacts_by_first_name[first_name] = [index]

    last_name = contact[LAST_NAME]
    if last_name in contacts_by_last_name.keys():
        contacts_by_last_name[last_name].append(index)
    else:
        contacts_by_last_name[last_name] = [index]

    mobile = contact[MOBILE_PHONE]
    if mobile in contacts_by_phone.keys():
        contacts_by_phone[mobile].append(index)
    else:
        contacts_by_phone[mobile] = [index]

    home = contact[HOME_PHONE]
    if home in contacts_by_phone.keys():
        contacts_by_phone[home].append(index)
    else:
        contacts_by_phone[home] = [index]

    zip = contact[ZIP_CODE]
    if zip in contacts_by_zip.keys():
        contacts_by_zip[zip].append(index)
    else:
        contacts_by_zip[zip] = [index]

 
add_contact(create_contact("Sue","Simmons","804-555-1234"))
add_contact(create_contact("John","Doe","804-555-1235","804-555-1236"))
add_contact(create_contact("Pat","Petri","804-555-1237","804-555-1238","23117"))
add_contact(create_contact("John","Smith","804-555-4321","804-555-4322"))
add_contact(create_contact("Steve","Simmons","804-555-4323","804-555-4323","23117"))

"""Showing the data."""

print
print "A dictionary of indexes that stores the list location of the records with the given key."
print "\nBy First Name:"
print contacts_by_first_name
print "\nBy Last Name:"
print contacts_by_last_name
print "\nBy Phone Number:"
print contacts_by_phone
print "\nBy Zip Code:"
print contacts_by_zip
print

print "\nAnd the list we are indexing:"
print contacts
print

indexes = contacts_by_first_name["Sue"]
contact = contacts[indexes[0]]
print "Contact with first name Sue:"
print contact
print

print "Results for search by last name Simmons;"
for index in contacts_by_last_name["Simmons"]:
    print contacts[index]

print "\nResults for search by certain phone number"
for index in contacts_by_phone["804-555-1238"]:
    print contacts[index]
    
    
    
