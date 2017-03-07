
### Question1 Analysis1: 
Using the Enron files, analyze the Inbox and Calendar items to find a pattern in the mailbox activity by date.

- Read all the Inbox and Calendar items for each and every user to extract the date in the mm/yyyy format, and create a dictionary to analyze the pattern in the volume of emails and calendar items by date and year.

- Plot a bar-chart to analyze the pattern in the volume of data

![Q1A1_1](https://github.com/dhavalbhinde/bhinde_dhaval_spring2017/blob/master/midterm/images/Q1A1_1.PNG)


```python
from IPython.display import Image
Image("images\Q1A1_1.png")
```




![png](output_2_0.png)




```python
Image("images\Q1A1_2.png")
```




![png](output_3_0.png)



Analysis1 Conclusion:

- As can be seen from the graphs, the mailbox activity started to get high in the start of 2001 and is at it's peak at October, 2001. It is well known that Jeffrey Skilling and Kenneth Lay, then CEO and Chairman of Enron respectively at the time of the scandal, were holding regular meeting with their top executives in order to pressure them into finding new ways to hide Enron’s debt. 
- Since the scandal was only made known to the public in Oct 2001, it could well be the case that this abnormal rise in meetings was an indicatorof Enron’s executives trying to cover up their accounting fraud.

### Question1 Analysis2:
Using the Enron files, analyze the count of inbox, sent and deleted items by User to find a pattern in the mailbox activity. And, to narrow down on the Top 25 users with highest activity. (All 3 data points considered Inbox,Sent and Deleted items)

- Step1: Get the count of all the emails under inbox/notes_inbox + deleted_items + sent/sent_items/sent_mail for all users
- Step2: Create a dictionary and keep a count of all the items with key = user
- Step3: Sort and Plot the data to analyze the pattern within the data for high volume users
- Step4: Find an intersection of all 3 categories to view the common users with high volume activity


```python
Image("images\Q1A2_2.png")
```




![png](output_6_0.png)




```python
Image("images\Q1A2_1.png")
```




![png](output_7_0.png)



From the graph above, we can narrow down to the top 25 users who have unusually high voulume of sent emails.


```python
Image("images\Q1A2_3.png")
```




![png](output_9_0.png)




```python
Image("images\Q1A2_4.png")
```




![png](output_10_0.png)



Analysis2 Conclusion:

- The above scatter plot activity of sent emails shows the distribution of the sent emails.
  The x-axis represents the number of email messages and the y-axis represents the number of Enron employees in log scale.
  The graph clearly shows that the messages are not evenly distributed between the users. A small number of users have sent a     large number of messages. 
  
- Also, if we refer the Inbox, Sent and Deleted items of all the users, it can be inferred that a small amount of users have       high volume of activity. To narrow down the culprits this data can be used for human intervention and further investigation.   

### Question1 Analysis3:

Using the Enron files, and the output from previos analysis, we dig further to analyze the the Top 15 users Inbox Data and to find the sentiment of their Inbox emails using NLTK. Here, we have used words like sell,short,inflate,kill and have created a custom made negative and positive words business dictionary. 

Step1: Read the content from the Inbox mails of the Top 15 high volume users
Step2: Perform data cleaning operations and remove stop words from the raw corpus
Step3: Lemmatize the word corpus and filter the data for sentiment analysis
Step4: Use the custom made positive, negative words business dictionary and analyse the corpus
Step5: Make a pir-chart to show the analysis


```python
Image("images\Q1A3_1.png")
```




![png](output_13_0.png)



Analysis3 Conclusion:
    
- From the pie-chart above it can be inferred that almost 60% of the data points to negative inferences and terms like sell,       short, inflate and other negative sentiments.    

#### Question2 Analysis1:

Search the NYT API - Article Search, for articles related to President Trump, and perform a Sentiment Analysis on his articles.

Step1: Fetch the data in the form of JSON files from the NYT API
Step2: Read the JSON data and merge all the files, since most of the files ~30kb
Step3: Read the snippet and the leading paragraph to build the data for analysis
Step4: Clean and tokenize the data to remove the stop words and unwanted characters
Step5: Import a positive, negative word dictionary from unc and perform sentiment analysis on the corpus


```python
Image("images\Q2A1_1.png")
```




![png](output_16_0.png)



Analysis1 Conclusion: 
- From the above pie chart it can be conculded that the NYT articles are almost neutral, while making news which includes         President Trump

#### Question2 Analysis2:

Search the NYT API - Article Search, for articles related to Restaurants & Food, and perform an analysis to find the most reviewed cuisines. Also, find the frequency of food-reviews as per year.

Step1: Fetch the data in the form of JSON files from the NYT API
Step2: Read the JSON data and merge all the files, since most of the files ~30kb
Step3: Read the leading paragraph to build the data for analysis
Step4: Build a dictionary to keep a track of the volume of articles by date (mm/yyyy)
Step5: Clean the data and remove unwanted characters and punctuations
Step6: Run the corpus against the cuisine dictionary to find the most cited cuisine
Step7: Plot the data for the most famous cuisine and the no.of food articles written by year


```python
Image("images\Q2A2_1.png")
```




![png](output_19_0.png)



Analysis2 Conclusion:

- As can be seen from the above graph, French cuisine is the most cited one followed by Chinese.
- And, the below graph shows the no. of food articles written every year. It can be inferred that during the market bull phase     more no.of food and leisure articles were printed. 


```python
Image("images\Q2A2_2.png")
```




![png](output_21_0.png)



#### Question2 Analysis3:

Search the NYT API - Most Popular Segment, for articles related to Travel & Tourism, and perform an analysis to find the top 25 most reviewed cities in the world.

Step1: Fetch the data in the form of JSON files from the NYT API
Step2: Read the JSON data and merge all the files, since most of the files ~30kb
Step3: Read the leading paragraph to build the data for analysis
Step4: Clean, tokenize and lemmatize the data to build a dictionary of the word corpus
Step5: Run the corpus dictionary against the cities list to get the most cited city.


```python
Image("images\Q2A3_1.png")
```




![png](output_23_0.png)



Analysis3 Conclusion:

- As can be seen from the above graph, New York is the most cited city in the Travel articles followed by London and Paris.    
