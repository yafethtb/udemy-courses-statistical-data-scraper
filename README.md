The data you can get from Udemy courses are abundant and useful. As a student you can see which courses in subcategories you want to learn that are updated. You can also see how much hours you might spend, the ratings, the students who already took the courses, etc. As an instructor, you might want to see which courses are your competitors by price and ratings. 

**-- THIS PROJECT CANNOT BE USED TO SEARCH COUPON OR COURSES WITH DISCOUNT PRICE! --**

What you will get are:
1. Course id.
2. Course title.
3. Course url.
4. Course base price.
5. Currency symbol.
6. Course rating.
7. Course reviews.
8. How much students taking the course.
9. Total lectures in the course.
10. Total time of the course.
11. The published date of the course.
12. The last update date
13. The course level
14. The course category
15. The course label.

# Example 
By using ISO 3166-1 alpha-2 code, you can change the price to be in your own country currency (or other countries currency, if you curious).
```python
# You can see the subcategories from Udemy. 

etl_process(subcategory = 'PR', country = 'us', start = 1, stop = 3)
```
The code will return a JSON file consist of all data above from page 1 to 3 of subcategory PR in Udemy with price in USD.

# DISCLAIMER
**Use this with your own risk!** The code might be broken if Udemy change their API. They might blocking your IP if you abuse their API, so use it wisely. I put sleep function to make gap in each iteration to make it not overloading the server. But this cannot guarantee that the server will not block you. So it's better to use it **OCCASIONALLY**.
