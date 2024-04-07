<!-----



Conversion time: 0.593 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Sun Apr 07 2024 09:39:30 GMT-0700 (PDT)
* Source doc: CMSC 388J Final Project Proposal_Writeup Template
* Tables are currently converted to HTML tables.
----->



## CMSC 388J Final Project Proposal/Writeup Template

**Group Members (1-4 members):**


```

```


**Directions:**

Read the project specifications and fill out all the boxes.


## Logistics

There are 3 things you will submit for the final project (only 1 group member has to submit):



1. Proposal
2. Project code
3. Writeup (submit when you submit your project’s code)

Both the Proposal and Writeup use this document as a template (your writeup will likely be the same or similar to your proposal depending on how much has changed since your proposal document).

**Due dates (unless specified elsewhere):**

Proposal: November 17 



* We **highly recommend** you complete this as early as possible so you have more time to work on the project. We will review your proposal within 1-2 days of submission.

Project Code and Writeup: December 8th for 10% extra credit, December 19th otherwise


## Overview

The final project for this class is to create a Flask app in a group of 1-4. You have a lot of freedom for this project as long as you meet the requirements. 

**You’re welcome to use Project 4 (or any other project from this course) as a base **(though you’re not required to–in fact, we encourage you to try creating something from scratch)**. **If you choose to use a course project, you need to make a “substantial” change. Examples of “substantial” changes include:



* Using a different API (instead of the OMDB API) + minor feature to demonstrate knowledge of Flask
* It’s no longer a “review site” but something else
* It’s still a “review site” but you add a major feature
    * Examples: ability to reply to reviews

Use your best judgment here but reach out to course instructors if you’re unsure. 

If you submit the final project by December 8th, you get **10% extra credit** on the assignment. You can submit up to December 19th. 


```
Description of your final project idea:

```



## Requirements

Note that some of these requirements overlap with each other so some features may satisfy multiple requirements.  

**Registration and Login:**



* There needs to be some sort of user control: logging in, registering, logging out.
* Certain features should only be available to logged-in users.

    ```
Describe what functionality will only be available to logged-in users:

```



**Forms:**



* At least 4 forms (can include registration and login forms)
* Must be CSRF protected

    ```
List and describe at least 4 forms:

```



**Blueprints:**



* Must have at least 2 blueprints 
* Each blueprint should have at least 3 visible and accessible routes

    ```
List and describe your routes/blueprints (don't need to list all routes/blueprints you may have–just enough for the requirement):

```



**Database:**



* Must use MongoDB

    ```
Describe what will be stored/retrieved from MongoDB:

```



**Another Python Package or API:**



* Find and use another Python package or API.
* Must be a package/API we haven’t used in any of the projects (though anything mentioned in lecture material that wasn’t used in a project is fair game).
    * You can use a package/API we’ve already used if you’re using it in a way that’s _very_ different from how we used it in the projects.
* Must affect the user experience in some way.

Examples (feel free to use these or come up with your own):



* Flask-Mail to send emails to users
* CalorieNinjas API with Requests package to access the API
* Spotify API
* Requests package to display data retrieved from an HTTP request
* BeautifulSoup4 to display data parsed from a website
* SciPy, NumPy, SymPy, etc
* Plotly  
* Discord OAuth

    ```
Describe what Python package or API you will use and how it will affect the user experience:

```



**Presentation:**



* Use something like CSS and/or Bootstrap to make your app look presentable.
* Doesn’t need to be a work of art but shouldn’t be raw HTML (use your best judgment here).

**Security:**



* Forms should be CSRF-protected.
* Site protected with Flask-Talisman
* Proper CSP: should only allow content/resources from trusted sources (i.e. sources needed for your app to run as intended)
    * If you’re using external JavaScript sources, make sure to add them in script-src (likewise for external CSS sources and style-src)


## Grading

**10% extra credit** for submitting by December 8th. Can submit up to December 19th.


<table>
  <tr>
   <td>Requirement
   </td>
   <td>Points
   </td>
  </tr>
  <tr>
   <td>Proposal submitted
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Writeup submitted (same format as the proposal) 
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Registration and Login
   </td>
   <td>75
   </td>
  </tr>
  <tr>
   <td>Forms
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Blueprints
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Database
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Another Python package or API
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Security
   </td>
   <td>25
   </td>
  </tr>
</table>


Total: 500 points
