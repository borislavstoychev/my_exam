# Python Web Framework
## Individual Project Assignment
This is the Individual Project Assignment for the Python Web Framework Course @ SoftUni. 
You could choose to develop one of the following projects – Django Template Project or Django REST Project.
##    1. Template Project (Django project) 
Mandatory requirements/Must haves
### Your project must have all this functionality to pass the final examination.

#### <li>The application must be implemented using Django Framework - [link](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/requirements.txt) :heavy_check_mark: </li>
#### <li>The application must have at least 10 endpoints - [account urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/accounts/urls.py), [common urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/common/urls.py), [sonq`s nails urls](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/sonq_nails/urls.py) :heavy_check_mark: </li>
#### <li> The application must have login/register functionality - [account views](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/accounts/views.py) </li>
![image](https://user-images.githubusercontent.com/67734870/128869148-f9d17dcd-1b81-4f43-87f7-d252bef241a4.png)
![image](https://user-images.githubusercontent.com/67734870/128867254-6a2cba25-991d-45a6-bbf2-2c128964b8cf.png)
#### <li> The application must have public part (A part of the website, which is accessible by everyone – un/authenticated users and admins) :heavy_check_mark: </li>
    - The public part is home page, all feedback and details about them. CRUD operations is not available.
![image](https://user-images.githubusercontent.com/67734870/128709089-b89dbf27-d059-4338-a2ef-7c2e3c57fecd.png)
#### <li> The application must have private part (accessible only by authenticated user and admins) . :heavy_check_mark: </li>
    - The private part is creating feedback, commenting, liking, account details and all CRUD operations on them. 
![image](https://user-images.githubusercontent.com/67734870/128710479-d281c5aa-ed42-42df-864e-3a569f07b2ba.png)
#### <li> The application must have admin part (accessible only to admins) :heavy_check_mark: </li>
    - My project is used build in admin part with all aplications included and full CRUD functionalities.
![image](https://user-images.githubusercontent.com/67734870/128862191-d15c81ec-012f-4a55-a56f-15fbc7a387c6.png)
#### <li> Form validations [link](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/common/forms.py) :heavy_check_mark: </li>
#### <li> To avoid crashes, implement Error Handling and Data Validations  :heavy_check_mark: </li>
#### <li> Use PostgreSQL as a database. :heavy_check_mark: </li>
#### <li> Write tests for at least 60% coverage on your business logic :heavy_check_mark: </li>
![image](https://user-images.githubusercontent.com/67734870/128865139-2ad475bc-7a5e-4d78-a27f-9b9ce88b8ece.png)
#### <li> Templates (your controllers/views must return HTML files) – one and the same template could be re-used/used multiple times (with the according adjustments, if such needed) :heavy_check_mark: </li>
#### <li> Use a source control system by choice – Github or Gitlab. You must have at least 5 commits + README :heavy_check_mark: </li>
### Optional/Bonuses
#### <li> Responsive web design :heavy_check_mark: </li>
#### <li> Class-based views :heavy_check_mark: </li>
#### <li> Extended Django user. [account models](https://github.com/borislavstoychev/my_exam/blob/main/nails_project/nails_project/accounts/models.py) :heavy_check_mark: </li>
#### <li> Documentation/ Swagger :x: </li>
#### <li> Use a file storage cloud API e.g., Cloudinary :heavy_check_mark:, Dropbox, Google Drive or other for storing the files </li>
#### <li> Implement Microservice architecture in your application. :x: </li>
#### <li> Additional functionality, not explicitly described in this section, will be counted as a bonus if it has practical usage. :heavy_check_mark: </li>