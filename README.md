## Group 9: Hector Soledad, Brian Tran, Tyler Cao, John De Dios

## Deals4U website:
Deals4U is a web platform designed to provide users with an extensive collection of the best deals sourced from popular e-commerce websites. By leveraging web scraping techniques, the platform aggregates deals, self-updates regularly (every 6-24 hours), and offers a user-friendly interface for efficient deal exploration.

## Goal:
Create a dynamic website showcasing the hottest deals from various e-commerce platforms.
Implement web scraping to regularly update and display the latest deals.
Provide a seamless user experience with an appealing and intuitive interface.
## Non-goals:
Manually set up deal notifications; the website will update itself regularly.
## Features:
P0
Deal Aggregation and Display:
Fetch and aggregate the hottest deals from a curated list of popular e-commerce websites.
Display deals based on categories, allowing users to easily navigate and find relevant offers.

## User Interface:
Design an appealing and user-friendly interface to enhance the overall user experience.
Implement responsive design for accessibility across various devices.
Database:
Design a database to store all the product information
After deal expiration, database will automatically remove old rows in the table, and insert new rows as new deals are scrapped
P1
Save for Later:
Introduce an option for users to "Save for later" if they want to revisit deals after scrolling through the offers.
User Interface continued:
Implement a timer indicating when deals will expire or refresh.
Implement sorting options based on price, category, and deal expiration time.


P2
User Accounts:
Develop a user account system to allow personalization of deals and preferences.
Monetization
Replace regular deal links with affiliate links to track user engagement and enhance the platform's revenue model.
Themes
Add different color schemes for the user to choose from including but not limited to: dark theme

## Engineering Details:
Stack
Option 1 (preferred): MySQL(Database), Node.js with Express.js (Backend), React (Frontend Framework)
React for front end
MySQL for the back end
Pros
React Native allows for the development of cross-platform applications.
React Native has a vast, supportive, and active community.
Both the backend (Node.js) and frontend (React Native) use JavaScript, allowing for code reuse and a consistent development experience
MySQL is a widely used and reliable relational database system.
Cons
 High learning curve to become proficient with the React Native framework
MySQL may face scalability challenges for extremely large datasets or high-traffic applications compared to some NoSQL databases.
We are inexperienced with implementing the entire stack
Option 2: MongoDB (Database), Express.js (Backend framework), Angular (Frontend framework), Node.js (Runtime environment)


Pros
JavaScript is used both on the client (Angular) and server (Node.js), which can simplify the development process and reduce context switching for developers.
MongoDB is a NoSQL database, offering flexibility in data schema and allowing developers to evolve the data model as the application grows.


Cons
As the application scales, the complexity of managing the entire stack might increase. Proper structuring and modularization are crucial to managing this complexity effectively.


## Other Details:
Our application will allow users to see 2-4 items per scroll.
Essential to add something like “EXPIRING IN:” to create sensation of urgency
Making the feel as if you are scrolling through TikTok, Instagram, Etsy, etc. 
Seamless experience. Nothing overlapping.

