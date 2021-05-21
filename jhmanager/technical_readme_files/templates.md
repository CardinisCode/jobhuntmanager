# Technical Readme
## Template:

This file will cover all the templates used for this application, which are utilized by the files & functions in the Services directory. These templates can be divided into the following categories: 
-   General
-   Users
-   Applications
-   Interviews
-   Interview Preparation
-   Job offers
-   Address Book
    -   Contacts Directory
    -   Company Directory
-   Notes
    -   Company Notes
    -   Application Notes

### General:
#### layout.html: 
This template is used as the 'reference' template, from which all templates (in this directory) get their structure. Since this template provides the layout & structure for all templates, it includes:
-   All meta data, 
-   Links to all stylesheets, bootstrap libraries & scripts (which can be used by any template), 
-   The navigational links & structure
-   The structural elements: head, body & footer 

By allocating one template to 'hold' all the above (required) elements, I could remove unnecessary duplication & thereby reduce the amount of storage required to store the 'templates' directory. 

##### about_us.html:
This page tells/informs the user:
-   what this application is about, 
-   why I developed this application, 
-   the research I carried out before putting this application together,
-   security, & 
-   how they could contact me if they want to. 

This page can be accessed via the 'About' link in the footer, on every page. 

##### dashboard.html
This page is the landing page for a user once they've logged in.  This page serves as the 'update' center, where the user will see all:
-   Upcoming interviews
-   Interviews the user has today
-   Applications submitted today
-   Job offers received
-   Progress stats:
    -   This shows the user how many applications, interviews and job offers they've submitted up til this point. 


