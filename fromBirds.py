from toSQL import *


	 
location = Create_Table('location', ['LocationName','City','County','State'])
location.add_record(['North Seattle College', 'Seattle', 'King', 'WA'])
location.print_items()