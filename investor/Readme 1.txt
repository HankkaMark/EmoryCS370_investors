#### Back-end Technology

Mainly use flask, and then integrated flask-login framework for login authentication operations, flask-sqlachemy for flask's data model operations

Front-end：Mainly uses the boostrap framework, and flask integrated jinja2 template statements

* base.html:the base template for all pages, such as the navigation bar in the head and the recommendation module on the left. Because all pages use the template, so it is extracted for other pages to inherit
* index.html:main page
* watchlist.html:Watchlist page
* contrastlist.html:Compare page
* login.html:Login page (after login, the top right corner shows the username and logout button,)
* signup.html:Register page (after login, the top right corner shows username and logout button,)
* person.html:Personal home page, click on the user name to enter (shows after logging in)

#### Function template



* Left recommendation: base.html, sent an ajax request when refreshing the page, the requested recomendlist function will query csv file and get data.
* Top navigation bar search: send a post request for index function, and then query according to the requirements of the stock conditions. After querying out data, directly jump to index.html page to show the result. If it cannot query the data, then hinted "Not found". If there is a result, then it will query a database at the same time to show whether the currently logged in user has followed the stock. If the user has followed the stock, the stock showed on the page will show "Followed".
* Price range search: this has not changed
* The sector performance should be displayed when enter the main page: The display was done through ajax before. Now it has changed to rendering through the template. The reason is that it is the same page with the top stock search. If it searches after loading as it did before, then the search data will be overwritten because ajax will send a request to obtain the data of the market after the implementation of the stock search and jump into the index.html
* login: the back-end is the login function. The front-end send a post request and the back-end query the database to determine whether the user name and password is correct. If they are correct, then login successfully.
* signup: back-end signup function and the front-end submit data. The back-end determine whether the password is the same and whether the database has his information. If there is no registration before, then sign up successfully and jump to the login page
* personal center: directly display the current registered user information
* Watchlist function: watchlistView function, introduced detailedly in the code. In the returned result, *watchlist* is the watchlist information and data is the details of a stock.
* Watch function: share the interface with cancel watch. Click the button to trigger the watchNow function, and then send an ajax request to the back end by the function to deal with it. The back-end code to write the logic (watchView function)
* contrast function: code is in the contrastlistView function

#### Login system

The login system mainly uses flask_login. Its main use is to maintain the state after login. When execute the login method, there will be login_user method to record the current user so as to achieve the effect of state maintenance. Before the user logs out, the page can show the user's information. It will determine whether to display the watchlist by judging the existence of this information, which is the same as the login name on the right.



#### Database (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

Done by flask_sqlachemy, it is an orm model. This model adapts to sqlite3, mysql and other databases. All the additions, deletions, changes and searches to the database are mapped to python code statements. There is sqlachemy to do the corresponding sql statement conversion.

If you want to use mysql, replace the line 36 of the code with the following code, and modify the relevant parameters

app.config['SQLALCHEMY_DATABASE_URI'] = 


