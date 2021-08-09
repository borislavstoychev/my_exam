# Python Web Framework
## Individual Project Assignment
This is the Individual Project Assignment for the Python Web Framework Course @ SoftUni. 
You could choose to develop one of the following projects – Django Template Project or Django REST Project.
##    1. Template Project (Django project) 
Mandatory requirements/Must haves
### Your project must have all this functionality to pass the final examination.

#### <li>The application must be implemented using Django Framework - [link](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/requirements.txt) </li>
#### <li>The application must have at least 10 endpoints - [account urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/accounts/urls.py), [common urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/common/urls.py), [sonq`s nails urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/sonq_nails/urls.py) </li>
#### <li> The application must have login/register functionality - [account views](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/accounts/views.py) </li>
#### <li> The application must have public part (A part of the website, which is accessible by everyone – un/authenticated users and admins) </li>
    - The public part is home page, all feedback, about me, schedule view. CRUD operations is not available.
![image](https://user-images.githubusercontent.com/67734870/128709089-b89dbf27-d059-4338-a2ef-7c2e3c57fecd.png)
#### <li> The application must have private part (accessible only by authenticated user and admins) . </li>
    - The private part is creating feedback, commenting, liking, account details and all CRUD operations on them. 
![image](https://user-images.githubusercontent.com/67734870/128710479-d281c5aa-ed42-42df-864e-3a569f07b2ba.png)
#### <li> The application must have admin part (accessible only to admins) </li>
    - My project is used build in admin part with all aplications included and full CRUD functionalities.
![image](https://user-images.githubusercontent.com/67734870/128715156-ef7e9043-91b6-4e20-bdbe-b1fa133d09ee.png)    • Unauthenticated users (public part) have only 'get' permissions e.g., landing page, details, about page
    • Authenticated users (private part) have full CRUD for all their created content
    • Admins have full CRUD functionalities
    • Form validations
    • To avoid crashes, implement Error Handling and Data Validations
    • Use PostgreSQL as a database.
    • Write tests for at least 60% coverage on your business logic
    • Templates (your controllers/views must return HTML files) – one and the same template could be re-used/used multiple times (with the according adjustments, if such needed)
    • Use a source control system by choice – Github or Gitlab. You must have at least 5 commits + README
### Optional/Bonuses
    • Responsive web design 
    • Class-based views
    • Extended Django user
    • Documentation/ Swagger
    • Use a file storage cloud API e.g., Cloudinary, Dropbox, Google Drive or other for storing the files
    • Implement Microservice architecture in your application.
    • Additional functionality, not explicitly described in this section, will be counted as a bonus if it has practical usage.