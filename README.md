# LittleLemon

### **Model**
![erd](https://res.cloudinary.com/dedalryr3/image/upload/v1676050385/meta/model_dhwnqb.png)

### **Home page and Menu item endpoints**
| Endpoint | Method | Purpose |
| --- | --- | --- |
| ```/restaurant/``` | ```GET``` |Home Page|
| ```/restaurant/about/```  | ```GET``` | About Page |
| ```/restaurant/menu/``` | ```GET``` | List of menu items |
| ```/restaurant/menu/{menuitem_id}/``` | ```GET``` | Single menu item view |
| ```/restaurant/menu/``` | ```POST```| Create menu item |

### **Booking endpoints**
| Endpoint | Method | Purpose |
| --- | --- | --- |
| ```/restaurant/booking/tables/``` | ```GET``` | List bookings |
| ```/restaurant/booking/tables/{booking_id}/``` | ```GET``` | Single booking view |
| ```/restaurant/booking/tables/``` | ```POST``` | Create booking |
| ```/restaurant/booking/tables/{booking_id}``` | ```UPDATE/PATCH``` | Update/patch booking |
| ```/restaurant/booking/tables/{booking_id}``` | ```DELETE``` | Delete booking |

## Sample Screenshots

### **Home Page**
![home_page](https://res.cloudinary.com/dedalryr3/image/upload/v1676051931/meta/homepage_cvdx7k.png)

### **About Page**
![about_page](https://res.cloudinary.com/dedalryr3/image/upload/v1676051931/meta/about_e5tcyq.png)

### **List Menu**
![list_menu](https://res.cloudinary.com/dedalryr3/image/upload/v1676051930/meta/list_menu_nszfjn.png)

### **List Bookings**
![list_bookings](https://res.cloudinary.com/dedalryr3/image/upload/v1676051930/meta/list_bookings_dhwn16.png)