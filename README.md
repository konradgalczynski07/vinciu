# Vinciu - my own implementation of Vinted, a web app for selling clothes

This is web application that allows its users to sell, buy, and swap secondhand clothing items.

## Features:

-   registering and logging to user account
-   ability to check other users profiles and items
-   leaving comments to other users
-   user settings which manage all CRUD operations
-   adding new items
-   search form

#### TO DO:

-   implementing all CRUD operations for managing items
-   adding items to favourites
-   sending messages to other users
-   unit tests

## Technology Stack:

-   Python/Django
-   PostgreSQL
-   HTML/CSS/Bootstrap

## Default urls:

-   localhost:8000
-   localhost:8000/women OR /men OR /kids
-   localhost:8000/search/?q={query}
-   localhost:8000/signup
-   localhost:8000/login
-   localhost:8000/logout
-   localhost:8000/profile/{username}
-   localhost:8000/profile/{username}/opinions/
-   localhost:8000/profile/{username}/opinions/new-opinion
-   localhost:8000/sell
-   localhost:8000/item/{id}
-   localhost:8000/settings
-   localhost:8000/settings/email
-   localhost:8000/settings/password
-   localhost:8000/settings/delete
-   localhost:8000/about/
-   localhost:8000/admin/

This website can be seen [here](https://vinciu.herokuapp.com)

Please note that images are not displayed properly on Heroku Free Plan and website sleeps after 30 mins of inactivity (which also means loading can take a while)

Screenshots below

![screen1](https://scontent-frt3-1.xx.fbcdn.net/v/t1.15752-0/p480x480/50138671_1425790017554010_238614793689235456_n.png?_nc_cat=108&_nc_ht=scontent-frt3-1.xx&oh=2dcbebf195dd05cd496824bd6f80ced7&oe=5CD259F6)
![screen2](https://scontent-frt3-1.xx.fbcdn.net/v/t1.15752-9/50022339_298588604334572_3730544959070142464_n.png?_nc_cat=108&_nc_ht=scontent-frt3-1.xx&oh=96b2bed2797088cee072635f8c785b8b&oe=5D3F927F)
![screen3](https://scontent-frt3-1.xx.fbcdn.net/v/t1.15752-0/p480x480/50095649_366283554162422_3535359534648262656_n.png?_nc_cat=107&_nc_ht=scontent-frt3-1.xx&oh=8f68c82d8b971ef0e8f58117693e3d54&oe=5CCC138B)
