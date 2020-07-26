# The Medical Term Dictionary

Deployed app: https://milestone-3-dictionary.herokuapp.com/

#### The brief for this project was –

*Create a jargon glossary/dictionary for a particular domain:
Create a web application that allows users to store and easily access definitions for terms in a particular domain, 
such as web development. You may want to use Wiktionary or Urban Dictionary (potentially NSFW content) for ideas.
Create the backend code and frontend form(s) to allow users to add new definitions to the site, edit them and delete them.
Create the backend and frontend functionality for users to search for definitions. You may choose to also provide an 
alphabetical display of all definitions.*

With this in mind, I created an app that allowed the user to find the definition of a medical term in the linked database 
and add, edit or delete a definition of a medical term already in the linked database.

### UX

This app is for users who want to find definitions of medical terms and add to the database in order to look up terms 
in the future, or to aid or share with when training members of the medical profession.

##### The user stories are -

###### Users searching for definitions within the Medical Term Dictionary:
* 	I want to be able to find definitions of medical terminology.
*	I want the definition to be clear and easily understandable.
*	I want to know the medical speciality that each term would be associated with.

###### Users modifying the Medical Term Dictionary:
*	I want to be able to add definitions to the database.
*	I want to search for these definitions in the future. 
*	I want to be able to edit and delete definitions on the site.
*	I want to be able to add or modify specialities within the database. 

### Wireframes

Please refer to the wireframes directory for individual page wireframes. 

### Features

##### Existing Features

*	###### Homepage – The homepage welcomes users to the medical term dictionary. There is a nav bar, 
    a button to enter the dictionary and a footer on this page.
*	###### Nav bars – There are two navigation bars – one main fixed nav bar on larger screens which compresses 
    down into a side nav bar on smaller screens. Both nav bars contain the homepage link, browse, add definition 
    and manage specialities. These links take the user to specific pages to view or modify entries in the dictionary.
*	###### Enter button – The enter button on the homepage takes users to the main browse page where there is a list of 
    all the entries in the dictionary. There is also the ability to filter the entries by letter at the top of the page. 
*	###### Letter filtering – Letters are found on the main browse page and on individual letter search pages. The letters 
    are highlighted when hovered over to show the user which link they are pressing. The user is then taken to a page which 
    shows all words beginning with the specific letter that they have clicked. The user can modify or delete entries on this 
    page. 
*	###### Card – The card shows the medical term definitions. The user will see the term, a description of what the term 
    means and the hospital speciality the term relates to. On the card there are floating action buttons. The definition 
    cards are listed in alphabetical order.
*	###### Floating Action Buttons – The floating action buttons contained on the cards allow users to edit a definition or 
    delete a definition. There are also floating action cards on the add a definition, edit a definition, add a speciality 
    and edit a speciality. These buttons allow the user to save or delete the form they have filled in. Another floating 
    action button can be found on the list of speciality page which allows users to add a new speciality. 
*	###### Forms  – Forms can be found on all the edit, mofidy or add pages. These pages allow users to input information 
    into the forms which will then be added to the database.  
*	###### Footer – The Footer shows copyrighted information. 

##### Features Left to Implement
*	Adding the ability for users to create profiles, log in and save specific definitions. This will also allow there 
    to be a section in the database stating who added the definition.
*	Adding the ability to search or group definitions by speciality. This will allow users who only work within one 
    speciality in the medical field, to pinpoint definitions that are most relevant to them. 
*	Adding an alert box when users are deleting an item. This will safeguard against definitions being deleted in error.
*	Adding a feature to stop the same definition being added multiple times. 

### Technologies Used

##### Languages Used:

###### HTML – used to structure the site.
###### CSS – used to style the site.
###### Javascript - used for the interactive elements on the site.
###### Materialize – this framework was used to style, structure and create a responsive site.
###### Python
###### Flask
###### MongoDB – the noSQL database that was used for the project’s data.
###### Jinja2
###### GitHub - used to store the project’s code while it is being worked on.
###### Gitpod - used to write the project code.
###### Heroku – used to deploy the project.
###### Microsoft Word – used to create the wireframes for the project.

### Testing

*	###### Welcome Page
    *	Title link found to be directing user back to welcome home page.  
    *	The links in the navbar go to the relevant pages. On smaller screens, the side navbar tested and found to be 
    working and sending users to the correct pages. 
    *	The links in the navbars highlight when hovered over to show where the user is pointing their mouse. 
    *   The enter button directs the user to the browse page.

*	###### Browse Page and Letter Search Pages
    *   Letter filters tested numerous times to ensure the links take the user to the correct pages. 
    *   Edit buttons on cards take the user to the edit definition page.
    *   Delete buttons on cards found to delete the entry.

*	###### Edit Definition Page
    *   Loads the definition from the database to the correct fields on the form.
    *   Changing the text and pressing the green tick button saves the entry and returns the user back to the main browse 
    words page. The amended entry can be seen here.
    *   Changing the text and pressing the red cancel button resets the modifications back to the original entry. 

*	###### Add Definition Page
    *   Completing the form and pressing the green tick button saves the entry and returns the user back to the main browse 
    words page. The amended entry can be seen here. 
    *   Completing the form and pressing the red cancel button resets the page to show a blank form.

*	###### Manage Speciality Page
    *   Add button takes user to add a speciality page.
    *   Edit buttons on cards take the user to the edit speciality page.
    *   Delete buttons on cards found to delete the entry.

*	###### Add a Speciality Page
    *   Completing the form and pressing the green tick button saves the entry and returns the user back to the 
    manage speciality page. The added entry can be seen here. 
    *   Completing the form and pressing the red cancel button resets the page to show a blank form.

*	###### Edit Speciality Page
    *   Loads the speciality from the database to the correct field on the form.
    *   Changing the text and pressing the green tick button saves the entry and returns the user back to the 
    manage speciality page. The amended entry can be seen here.
    *   Changing the text and pressing the red cancel button resets the modifications back to the original entry. 

### Responsiveness of site:

To aid in creating a responsive site, I used Materialize’s Grid System. Through the process of creating this app, 
I checked the various break points to see if the page layouts worked on various device screen sizes, using Chrome 
Developer Tools.

###### Navbar: For mobile views for the project, users will see that the full desktop navbar is reduced to just the 
logo and a burger button, which activates the side nav containing the navbar elements. 
###### Page layout and Cards: I experimented with various column sizes, layouts and card types to achieve a site which 
was visually appealing and appropriate to the screen size it would be viewed on.

### Debugging:

###### Issue: Letter filtering only showing entries starting with an upper case letter.
###### Solution: Used the $regex query method to target specific entries with “$options” : “i” added to the function. 

###### Issue: Letter filtering showing entries containing the selected letter anywhere in the definition term
###### Solution:  letter = ‘^A’ added to the link for each letter within the html coding. 

###### Issue: Add / edit forms displayed the specialities in the order they had been entered into the database.
###### Solution: Added sort attribute by speciality name to each html speciality div to order the specialities 
in alphabetical order to aid in filling out the form. 

### Deployment

I created a repository on GitHub using the GitPod template supplied by Code Institute and linked GitPod to my 
project. I created an app on Heroku. I added the requirements.txt and procfile elements on GitPod and specified 
the IP and Port on Heroku to link my project up.
I committed the content at various stages throughout the creation of my project. 
Having completed my project, I pushed to Heroku as the final stage of deployment. 

### Credits

##### Content

*	This project was based on the task manager project in the Data Centric Module, with various functionality added. 
*	Guidance on the layout and filter functions were obtained from queries on Slack.
*	This README file is based on the Code Institute template.

##### Media

*	All photos used in this site are from Google Images.

##### Acknowledgements

*	This project was inspired by the task manager project within the Data Centric Development Module.
