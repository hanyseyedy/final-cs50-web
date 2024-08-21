# FINAL NEWS WEBSITE

#### Video Demo: <URL https://youtu.be/q5wiZfx5smw>

#### Description:

This is a simple news blog. You will be able to see a list of news in different Categories. You can also add Comment in each post.

This is easily done. the site have one or some admins and create post is able only for admins.

#### Program requirements:

To run the program correctly, you not need to install any Python packages. at the moment in the request.txt file not any required packages.

only need to install Django

if you alrady not installed Django, in windows run below command:
`...\> py -m pip install Django`
and in mac or Linux:
`$ python3 -m pip install Django`

Note: in linux you should to use: `$ python3`

#### Run Program:

First you need to run the program. you should to manage your database:
`python manage.py makemigrations final`
then run command below:
`python manage.py migrate`

then to run the program, type the following:
`python manage.py runserver`

#### Add Post in Blog:

To add post first you shoud to login. to this work you must click on the "login" botton on the top of page. then insert username and password.

after login click on the "create post" button on the top of page. Then you will enter the post creation page.

- in "title field" must be insert your post title.
- in "content field" must be insert your post or article content. This field includes an advanced editor where you can insert any type of content such as text, table, video, photo, etc.
- in "Thumbnail field" must be insert primary Image URL your post.
- In the category field, you must choose the category related to your post. Note that different categories must be created through the Django admin section.

#### What’s contained in each file created.

**index.html:** this is a home page of the site. It includes menu, latest posts, categories, post display carousel, header, footer, sidebar, etc.

**listing.html:** this is page of the post. It includes thumbnail, Content of the post and etc.

**createnew.html:** This page is about creating a new post. Only the site admin has access to this page. `127.0.0.1:8000/create`

**category.html:** The page related to posts with the same category.

**login.html:** The page related to admin login.
