# Kalopsia Books

_Lisa Feigen Milestone Project 4 (Django Full Stack Framework)_

This is my fourth project studying with The Code Institute.

This project focuses on all major aspects of building and deploying a website, building a responsive interactive front end UI, creating a server side web application and finally performing CRUD operations on a database.

I chose to make an e-commerce website for an author who wants to sell her books and keep her readers informed about new releases. Buying books directly could be a way for authors (especially the ones who self-publish) to connect to her audience on a more personal level. 

The target audience for this website is everyone interested in crime books and novels to buy them for themselves as well as gifts for others.

The goal of the website is to encourage readers to support the author they like directly by buying the books directly from her as well as to inform first time visitors about the author.

For testing the checkout please use the following card number and details:

**Card Number: 4242 4242 4242 4242**

**Month/Year : 04 / 24**

**CVC: 242**

**ZIP: 42424**

[Try the site here](https://lisa1q84-kalopsyabooks.herokuapp.com/)

## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#contents)Contents

-   [**UX**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#UX)
    
    -   [User Stories](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#User-Stories)
-   [**Develoyment**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Development)
    
    -   [Planning](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Planning)
    -   [Ideas](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Ideas)
    -   [CRUD](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#CRUD)
    -   [Adding and Editing Product Form Validation and Image Validation](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Adding-and-Editing-Product-Form-Validation-and-Image-Validation)
    -   [Templating](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Templating)
    -   [Console Logs Prints Debug and Variables](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Console-Logs-Prints-Debug-and-Variables)
    -   [Commit Messages](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Commit-Messages)
    -   [CSS Variables](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#CSS-Variables)
-   [**Features**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Features)
    
    -   [Live Features](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Live-Features)
    -   [Features Left to Implement](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Features-Left-to-Implement)
-   [**Technologies Used**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Technologies-Used)
    
-   [**Testing**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Testing)
    
    -   [Functionality](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Functionality-Testing)
    -   [Issues and Bugs](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Issues-and-Bugs)
-   [**Deployment**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Deployment)
    
    -   [Local Deployment](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Cloning-Local-Development)
    -   [Remote Deployment](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Remote-Development)
-   [**Credits**](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Credits)
    

## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#ux)UX

The Kalopsia Books website allows users to search, filter and sort all books in the store so they can easily find what they're looking for. Firstly, links to the major categories can be found in the main site header along with a link to view all the products. When the user lands on the view products page (filter by a category or not) they will be presented with the option to sort the products in the filter bar. The current filter / sort settings can be easily identified by either; viewing the  **Current**  element that appears under the filter bar when an option is selected (also providing the option to clear the selected option) or in the filter / sort dropdown where the selected option will be highlighted.

Viewing a product's details can be easily achieved by simply clicking any part of the product card taking the user to the product details page. 

Users can then add products to their bag and easily navigate to the checkout page from the view bag button.

At checkout the user is presented with a simple and easy to fill in form which will let them know if they have made an error. The details they fill in can be saved (if they are logged in) so they can checkout quicker next time or the user can pre-fill them in on their profile page.

Once their payment has gone through the user will receive an email notification from  [kalopsiabooks@gmail.com](mailto:kalopsiabooks@gmail.com)  with their order number and the details of the items they have ordered. They will then be presented with the order success page. If the user is logged in and didn't checkout as a guest then they will be able to view all their past orders on their profile page and get a full description of the order by clicking on an order.

Users can create a profile by clicking the profile icon in the site header which if they are not logged in will take them to the sign in page with the option to sign up. On signing up the user will receive an email with a link to verify their email.

The user may wish to continue shopping for more items and then go to view their bag before checking out to make sure they have everything. This can be done at any time by clicking the bag icon on the site header which also displays how many items are in their bag. The user will be taken to the view bag page where they can edit their bag. On this page they can update the quantity of a product or remove the product all together.

Site admins can add, edit and delete products from the product management page, which is only accessible to site admins (superusers).  Products on the product management page can be filtered by category.

Site admins can keep users up to date with everything that's new in the Kalopsia Books Community  by writing and posting to the Kalopsia News Blog. Users can access this page from the site header and is listed in the main site nav. Admins have the option to edit and delete blog posts by clicking the appropriate buttons on the relative post. Users are presented with the posts; the most recent at the top so they get the latest news first.

The user will receive messages from the site as they do certain actions or make errors which are presented to the user just under the site header.

## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#user-stories)User Stories

_User Stories_

As a user of the site:

-   I want to understand the website's purpose
-   I want to be easily able to view a list of all books by category
-   I want to be able to view specific product details
-   I want to be easily able to purchase products

As the site owner:

-   I want the website to provide a platform for users to purchase books
-   I want to be able to add/edit/delete products


### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#ideas)Ideas

When creating this online book shop my goal was to enable users to buy products easily and quickly as possible. With this in mind I planned how to make the process from landing on the site to a successful checkout as easy as possible. 

There should be a wishlist option for products a user does not want to buy immediately.

The author should have the ability to inform users of news about the company and events that are going to build hype around the brand to encourage them to engage more in community events and discussions. Eventually leading to them buying more.

The user should be given feedback for the action they take on the site for example trying to access urls they aren’t allowed to be viewed or reached.

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#crud)CRUD

Site users can add, edit and update their delivery information. Users can also add products to a "Wishlist" .

Users can create profiles by signing up to the site and create orders by going through the checkout.

Site admins have the ability to add, edit and delete products from the product management page. 

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#adding-and-editing-product-form-validation-and-image-validation)Adding and Editing Product Form Validation and Image Validation

The Adding / Editing Product Form has validation for the selection related to the product. The view that handles the form submission will check if the form inputs for the product section are valid so they can be entered into the database. If the form isn't valid then an error message should be displayed to the user telling them to check the data they have entered.


### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#templating)Templating

The webpages for this site have been created using Django templating. A base template has been created including the Doctype, head, site header and footer into which the rest of the templates extend.

Using python in an HTML file allows the ability to show specific elements to a specific user group. For example non-logged in users shouldn’t be shown the  **log out**  button and vice versa; the logged in user shouldn’t be shown the  **log in**  button. Normal users shouldn’t be shown links to pages to which only site admins should have access, such as the product management page.

Templating also reduces the overall amount of code as most elements only need to be coded once. This allows editing of the code to be a lot easier; as again there is only one instance of the code that needs to be updated.

The ability to access variables passed by the view to the template means database objects or attributes of the object can be easily displayed to the user. Groups of objects can be looped through in the code to display the information and that code only needs to be written once.

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#console-logs-prints-debug-and-variables)Console Logs Prints Debug and Variables

When testing the site; I set it to be built automatically and hosted by Heroku everytime I pushed to Github. This was to test the live site against the local preview. In doing this the site was hosted by Heroku containing console logs and print functions.

With the site in this state it was presented only to test users as I didn't want to remove or change any of them just to have to add them or revert them back at a later date.

**There is no console logs or print functions in the live site**

The site is able to adapt to different environments by the use of environment variables.

If a DEVELOPMENT variable is in the environment variables then Django’s debug will be turned on.

** No DEVELOPMENT variable is set in the app of the live site and the debug is turned off**

If a DATABASE_URL variable is in the environment then the app will use that variable to link to the database it points to.

This variable controls which database is used. If not set, the site will use the SQLite3 database. Otherwise the site will use the database the variable is set to.

**The DATABASE_URL is set as the link to the postgres database in the environment of the live site meaning, the live site is using the remote postgres database**

If a USE_AWS variable is present in the site's environment variables then the site will use the remote S3 bucket to store, get and upload media and static files otherwise the local storage will be used.


**There is a USE_AWS variable present in the environment of the live site meaning the live site is using the S3 bucket to load and store static and media files, and images will not be resized on upload**


## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#features)Features

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#live-features)Existing Features

_Existing Features:_

Homepage:

-   The site is styled using bootstrap for responsive design
-   Fixed navbar, incorporating search form and site navigation links
-   Buttons linking to product areas of the site (categories used to show appropriate products)
-   Footer with social media links
-   Toasts used to display info for user on login/logout etc

Products:

-   Crispy forms used to display product info
-   Bootstrap card format to display product image/details

Product Details:

-   Crispy forms used to display product info
-   Quantity selector input form to add products to bag

Bag:

-   Crispy forms used to display product info
-   Grid/table format used to display products

Checkout:

-   Input form to enter details
-   Stripe card details form to facilitate payment

Login/Logout:

-   Input forms for logging in/signing up

Profile:

-   Crispy forms to display user info/order history
-   Input forms for updating user details

Wishlist:

 - Allow users to mark items as they see them and add them later to their bag.

Blog:

 - Allows the user to keep the update date with everything that’s going on with Kalopsia Books and get the latest updates on new releases reviews  and events. The blog is a great feature to which the site admins can post to. However, the formatting is problematic, I want to improve the way the blog entries are displayed in the future. 

Other:

-   The website has been linked to Amazon Web Services to store any static files/images there automatically
-   The website has been linked to Stripe to facilitate payments
-   The website has been linked to a Gmail account to facilitate sending of emails on registering/placing an order


- [Features Left to Implement](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#Features-Left-to-Implement)
_What still should be implemented_

Due to time constraints, I was not able to do half of what I wanted to do and I hope I will be able to the following features in the future:

-   An option to purchase a book with a custom dedication
-   A real functional product carousel
-   More details included in homepage for example a press section
-   More dynamic media on the homepage i.e. videos for better user experience.
-   A contact form
-   A possibility for users to give reviews
-   More product details and the opportunity to review books for users
-   Blog Post Comments
   


## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#technologies-used)Technologies Used

-   [HTML 5](https://en.wikipedia.org/wiki/HTML5): language used to structure and provide content of pages of the website.
    
-   [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): visual language used to style and format the html.
    
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)  &  [JQuery](https://en.wikipedia.org/wiki/JQuery): JavaScript used for frontend functionality as well as dynamically adding, removing and updating elements.
    
-   [Python](https://www.python.org/): Python is used to run the back end of the web application. It is also used to query the databaseand perform CRUD operations on the database.
    
-   [Django](https://www.djangoproject.com/): is a python framework used to set up the web application.
    
-   [Heroku](https://www.heroku.com/): platform used to host the web application.
    
-   [SQLite3](https://www.sqlite.org/index.html): provides the development database the web application uses to store and query data.
    
-   [PostgreSQL](https://www.postgresql.org/): provides the deployment database the web application uses to store and query data.
    
-   [AWS](https://aws.amazon.com/): provides the deployment storage for static and media files.
    
-   [Stripe](https://stripe.com/): provides the payment system for the sites checkout. It also provides the code to receive webhooks which I have adapted to my needs
    
-   [Bootstrap Framework](https://getbootstrap.com/docs/4.1/layout/grid/): provides a grid system to insure a mobile-first design and responsive website which adapts to different screen sizes of devices.
    
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): allows bootstrap and custom classes to be added to django forms.
    
-   [Pillow](https://pillow.readthedocs.io/en/stable/):allows upload of images to the local or remote storage depending on which version of the site is running.
    
-   [Swiper JS API](https://swiperjs.com/swiper-api): provides the image carousel.
    
-   [Gitpod](https://gitpod.io/): the Integrated Development Environment used to write the code for this project. Also provides a preview of the website in a browser which was then used for testing.
    
-   [Gitpod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en): made it easier and faster to open the repository in my IDE directly from Github in a web browser.
    
-   [Git](https://git-scm.com/): used for version control and to push the control to a remote repository to be stored.
    
-   [Github](https://github.com/): used for as a repository to store the versions of the website.
            
-   [Google Font](https://fonts.google.com/): font for website.
    
-   [Font Awesome](https://fontawesome.com/): styles and provides icons.
    
-   [Google Chrome](https://www.google.com/intl/en_uk/chrome/),  [Microsoft Edge](https://www.microsoft.com/en-us/edge),  [Firefox](https://www.mozilla.org/en-GB/firefox/new/)  and  [Opera](https://www.opera.com/): to test browser compatibility.
    
-   [Google Chrome Dev Tool](https://developers.google.com/web/tools/chrome-devtools): main tool for testing. Inspecting elements and troubleshooting.
    
    

## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#testing)Testing

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#html)**HTML**

I used  [W3C Markup Validation Service](https://validator.w3.org/)  to check my html was valid.

**Errors**

No errors produced.

**Warnings**

" The  `type`  attribute is unnecessary for JavaScript resources. " - The type was in the tutorial and therefore I left it in my code. 

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#css)**CSS**

I used  [W3C Jigsaw Validation](https://jigsaw.w3.org/css-validator/)  direct input feature to check if my CSS was valid.

**Errors**

No errors produced

**Warnings**

A warning occurred for all vendor extensions. The following warnings were produced when running my site through validation:

`-webkit-filter`  is a vendor extension

`-webkit-user-select`  is a vendor extension

`-moz-user-select`  is a vendor extension

`-ms-user-select`  is a vendor extension

I have left this code in the site to ensure compatibility with most browsers.

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#js)**JS**

I used  [JS Hints](https://jshint.com/)  to check my JavaScript was valid.

**Errors**

No errors produced

**Warnings**

I got the following Warnings

**template literal syntax' is only available in ES6 (use 'esversion: 6').'**

A warning that old browsers not support the use of template literal

**$ is an undefined variable**

Produced because the validator doesn’t know how to handle JQuery.

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#python)**Python**

I ran all code written by myself through  [pep8online](http://pep8online.com/)  to check if my Python was PEP8 compliant.

All code in the two additional apps (the blog and the wishlist ) passed the PEP8 check and came back as "All right" after I fixed some E501 error. 


### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#functionality-testing)**Functionality Testing**

#### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#links)**Links**

I have manually tested each link and they all work as intended.

#### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#links)**Features**

The following details how the various features of the site have been tested for their intended purpose:

GENERAL

-   Top navbar is fixed at the top for all pages
-   Navbar changes to burger icon on mobile
    -   All navbar links redirect to correct site page
-   Footer appears at bottom of homepage
    -   Footer social links all open in new tabs

HOMEPAGE

-   Button titled MY ACCOUNT folds down and gives you option based on whether you're logged in and a super user.
-   Button titled WISHLIST takes you to your wishlist page
-   Search form brings back appropriate results based on name/description

LOGIN

-   Entering correct username/password takes you to user profile page/displays correct toast
-   Entering incorrect username and/or password displays "Incorrect username and/or password" message. Password can be reset. 

REGISTER

-   Entering username/password in required format completes registration and sends email to confirm registration/displays correct toast
-   Entering username/password not matching required format displays prompts to correct

PROFILE

-   Profile page displays user details/order history
-   Able to update user details

BOOK PAGES

-   Display appropriate products according to filter/ category
-   Displayed in card format with image/name/price/rating (if applicable) showing

PRODUCT DETAIL

-   Shows individual product details
-   Form to select qty/size
-   Button to add to wish list
-   Button to add to bag
-   Checkout button takes you to checkout

BAG

-   Correctly shows all added items/total price
-   Ability to add/remove qty of items

BLOG

 - See blog posts and create/edit/delete them if you are an admin

CHECKOUT

-   Shows form to fill out payment details
-   Error message if details entered incorrectly
-   Order success message shown when order completed

ADMIN

-   Only the admin user profile is able to make add/edit/delete changes to the site products

_Responsiveness_

Specific responsive features included:

-   On mobile the navbar menu items are displayed in dropdown icon
-   The bag view is displayed differently on mobile

I tested the website by changing the screen size on my display, and using the inspect function on developer tools to show how it looks on different devices.

I tested the website on various browsers/devices which were available to me.


#### [](https://github.com/LiamDHall/XRYO/blob/master/README.md#device-compatibility)**Device Compatibility**

I have tested a number of devices in the Google Chrome Developer Tool in the Google Dev Tool.

The site is compatible down to devices with screens that are 319px wide.


### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#issues-and-bugs)Issues and Bugs

The Blog posts are not formatted as they should be and the entire text is cramped together. Due to time constraints I was unable to fix this.

On the wishlist site, in order to add the product to the cart, the user is sent back to the product detail page. This is good if a user wants to select a certain quantity but it might be better to directly add the product to the bag instead of having this detour. 

When adding a product in the admin view, any rating can be entered instead of having the form tell the user that is has to be a number below 5. Also when not adding an image there should ideally be a test image (like a placeholder) displayed instead.

There is "has_variation" in the product model. But it is not relevant as I made changes to my project. 
Due to time constraints I did not remove it because it would have meant that I have to upload all products again.


## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#deployment)Deployment

This web application is hosted on Heroku.  [View Live Site](https://lisa1q84-kalopsyabooks.herokuapp.com/)

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#cloning-local-development)Cloning Local Development

1.  Open the Github repository -  [https://github.com/lisa1Q84/kalopsia_lens](https://github.com/lisa1Q84/kalopsia_lens)
    
2.  Click the green drop down that says  **Code**,  **Download**  or  **Clone**.
    
  
3.  To clone with HTTPS copy the URL in the box.  [https://github.com/lisa1Q84/kalopsia_lens.git](https://github.com/lisa1Q84/kalopsia_lens.git)
    
4.  Open up your Integrated Development Environment (IDE).
    
5.  Open your Command Line or equivalent if not already.
    
6.  Type  **git clone**  and paste the copied URL from step 3. (Should look like  **[https://github.com/lisa1Q84/kalopsia_lens.git](https://github.com/lisa1Q84/kalopsia_lens.git)**)
    
7.  If you then wanted to copy it to a specific folder add the folder name to the end. (Should look like  **git clone  [https://github.com/lisa1Q84/kalopsia_lens.git](https://github.com/lisa1Q84/kalopsia_lens.git)  folder-name**)
    
8.  Press Enter and a local clone will be created.
    

The following steps are then required to make the clone work as intended using Gitpod. The following steps may vary based on the IDE you use.

9.  Install the required dependencies by running  **pip3 install -r requirements.txt**
    
10.  Create a  [Stripe](https://stripe.com/)  account and follow the steps until you land on the dashboard then under the  **Developers**  tab click on API keys where you will find your stripe publishable key and your stripe secret key
    
11.  Follow the steps in their documentation to setup a test webhook endpoint as your IDE preview checkout webhook url **(your_IDE_preview_address/checkout/wh/)**where you will get your webhook endpoint signing secret
    
12.  In your IDE set the following variables replacing the  **placeholders**  with your correct values
    
    DEVELOPMENT === True (only set/create this variable if you want the debug on) SECRET_KEY ===  **your django secret key**  STRIPE_PUBLIC_KEY ===  **your stripe publishable key**  SECRET_KEY ===  **your stripe secret key**  STRIPE_WH_SECRET ===  **your webhook endpoint signing secret**
    
13.  Create a superuser by running the command line  **$ python manage.py createsuperuser**  And fill in the information it asks for.
    
14.  In command line run  **python3 manage.py runserver**  (I did have an issue after deploying the live site where the static files wouldn’t load when I went back to deployment / local version of the site. If this occurs, run  **python3 manage.py runserver --insecure**)
    
15.  A pop up will appear in the bottom right hand corner.
    
16.  Click on  **Open Browser**  and the website opens in a new tab.
    
17.  Login to the admin of the site by adding  **/admin**  on to the url and verify your email address in the  **Email Address**  section.
    

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#remote-development)Remote Development

This web application is hosted on Heroku.  [View Live Site](https://lisa1q84-kalopsyabooks.herokuapp.com/)

1.  Sign up to  [Heroku](https://www.heroku.com/)  and create a new app.
    
2.  Set a variable in your heroku app:
    
    SECRET_KEY ===  **your django secret key**
    
3.  On the resources tab search for  **postgres**  and click on  **Heroku Postgres**  and set it to the free plan.
    
4.  Set a variable in your IDE as: DATABASE_URL equal to (which you can find in your heroku app variables.)
    
5.  Make sure you have Procfile and a requirements.txt created.
    
6.  Your Procfile file should contain one line of code which is as follows:  **web: gunicorn .wsgi:application**
    
7.  Run the command line  **python3 manage.py migrate**  to set up the database
    
8.  Create a superuser by running the command line  **$ python manage.py createsuperuser**  And fill in the information it asks for.
    
9.  Commit to Github
    
10.  **(If you don’t wish to store the static files in a AWS S3 bucket this step is unnecessary)**  Set a variable in your heroku app as  **DISABLE_COLLECTSTATIC**  equal to 1 to stop heroku collecting static files
    
11.  Add your new app host name to your settings.py file in the ALLOWED_HOSTS list
    
12.  Setup Heroku git by running the command **heroku git:remote -a
    
13.  Commit to heroku by running the command ** git push heroku master**
    
14.  To set up automatic deployment go to your Heroku app and under the deploy tab set the deployment method to Github and then search for your repository, then click connect. Then click the  **Enable Automatic Deploys**
    

**The following steps are then required to make the site work as intended and using AWS to host static files. The following steps may vary based on the IDE you use.**

15.  Create a AWS account and create a new S3 bucket and make sure your bucket has public access turned on, static website hosting turned on, CORS is configured correctly, a correct security policy with all actions allowed on all resources in the bucket and contains your arn number and finally have the List Objects checked on everyone on the Access Control Tab.
    
16.  Create an Amazon IAM user in a group that has a policy that allows them to access all resources in the new bucket. Through the creation of this user you will be given the option to download a .csv file which will contain the user API keys.
    
17.  Set these new keys as variables in Heroku App:
    

AWS_ACCESS_KEY_ID ===  **your Access key ID**  AWS_SECRET_ACCESS_KEY ===  **your Secret access key**  USE_AWS === True

18.  Remove  **DISABLE_COLLECTSTATIC**  variable from your Heroku App
    
19.  In setting.py set:
    
    AWS_STORAGE_BUCKET_NAME ===  **your bucket name**  AWS_S3_REGION_NAME ==  **your bucket’s region**
    
20.  Create a media folder in your bucket
    
21.  Commit and push all files to Github. Your static files should appear in your S3 bucket
    
22.  Login to the admin of the site by adding adding  **/admin**  on to the host url and verify your email address in the  **Email Address**  section. This will allow other users to login.
    

**Set up Stripe Payment**

23.  Create a  [Stripe](https://stripe.com/)  account and follow the steps until you land on the dashboard then under the  **Developers**  tab click on API keys where you will find your stripe publishable key and your stripe secret key
    
24.  Follow the steps in their documentation to setup a test webhook endpoint as your heroku app checkout webhook url  **([https://your_app_name.herokuapp.com/checkout/wh/](https://your_app_name.herokuapp.com/checkout/wh/))**  where you will get your webhook endpoint signing secret
    
25.  Set these new keys as variables in Heroku App:
    
    STRIPE_PUBLIC_KEY ===  **your stripe publishable key**  SECRET_KEY ===  **your stripe secret key**  STRIPE_WH_SECRET ===  **your webhook endpoint signing secret**
    

**Sending Real Emails**

26.  Go to your google account security settings and turn on two step verification and follow the steps. A new option under the sign in google heading called  **App passwords**  click it and on the app password screen set the app to  **Mail**  and the device to whatever you want. Click  **Generate**  and you will be present with a password
    
27.  Set these new keys as variables in Heroku App:
    
    GMAIL_PASSCODE ===  **your gmail password**  GMAIL_USER ===  **gmail address set up with the password**
    

## [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#credits)Credits

This project is heavily built on the Code Institute mini project Boutique Ado.

Third parties code has been credited in the code of the website where appropriate.

#### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#images)Images

All images are my my mothers (she is the author) and I have consent from her and the publisher to use the photos for my project.

### [](https://github.com/lisa1Q84/kalopsia_lens/blob/main/README.md#acknowledgements)Acknowledgements

I would like to thank the very patient people from tutor support for their help, without them I would never have finished this project. 

I would also like to thank my mother for providing me with the content and for helping me spell check the site.

I used the following websites in addition to the Boutique Ado tutorial:
[Django Central](https://djangocentral.com/),
[CSS Tricks](https://css-tricks.com/),  
[Stack Overflow](https://stackoverflow.com/),  [Django Documents](https://docs.djangoproject.com/en/3.2/)  and  [Stripe Documents](https://stripe.com/docs)  for this project.

