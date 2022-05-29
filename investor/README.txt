
What is it?
A stock recommending website implementing stock search, filter, comparison, account, and watchlist.

How do we use it?
You will need to run 2 scripts - screen.py (recommending algorithms) and main.py (the website under flask)
1, Run screen.py ahead of time (1.5 h), I know it's slow! But that's how the algorithms work. The good news is as long as you don't terminate it, you will get renewed data every 2 hours automatically. That means every time after waiting the first 1.5 hours you will get up-to-date recommendation list instantaneously!
2, Run main.py. (You don't need to wait for completion of step one. We have a recommending list stored for you, probably from yesterday) Then you will get a website, open it and here is our stock recommending website.

What can it do?
1, On the top right, register an account to unlock watchlist. Sign in if you already have an account.
2, Everything start from a simple search. Search to stock name on search bar located top right. For example, search AAPL for Apple stock.
3, Before stock search, you can see 8 sector performance index on the dashboard, see Sector performance section in Readme for more information. After stock search, you will receive a list of 8 index and a plot for that stock.
4, There's a filter above the dashboard. Enter an expected lower bound and upper bound price to get a recommended stock list within your expectation. We are not recommending GOOGL for people aiming at penny stocks! If there's no stock recommended with in your expected price range, try some other numbers.
5, You can add a stock into watchlist if you already signed in. Click the bottom again to remove from watchlist. You can view all stocks and their information in the watchlist tab.
6, You can compare two stock in the compare tab. Enter two stock names to make the comparison.

More technical detail?
See README- tech.txt.

Sector performance (appear on dashboard before any search)
Each number denotes the last percentage change in the market-value weighted index of the sector compared to last day's closing price
Written in decimal number (i.e. 1% is written as 0.01)

Recommending algorithms (screen.py)

Debug:
For those got certificate_verify_failed error, try add 
"import ssl
ssl._create_default_https_context = ssl._create_unverified_context"
To the file.