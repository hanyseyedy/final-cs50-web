# FINAL NEWS WEBSITE

#### Video Demo: <URL https://youtu.be/q5wiZfx5smw>

#### summary description:

This is a simple news blog. You will be able to see a list of news in different Categories. You can also add Comment in each post.

#### Distinctiveness and Complexity:

This is a simple news website that can also be used as a blog. At the same time, it is simple, fast, optimized, responsive and has a beautiful user interface.
Among its special features, the following can be mentioned.

- Posting is possible only by the site admin.
- This site can have one or several admins.
- Inserting a post by the admin through a special page is easily possible. also in create post page includes an advanced editor where you can insert any type of content such as text, table, video, photo, etc in your post.
- In each post, it is possible to insert a comment for each visitor.
- Paginator is used in the pages of this site, if the number of posts increases, the older pages are moved to another page, and you can move between different pages using Paginator.
- Each post can be linked to a specific category. The site has posts with different categories, and by selecting each category, you can see only the posts related to a certain category.
- In header of the site, a beautiful carousel is used, which displays three new posts of the site

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
- in "content field" must be insert your post or article content.
- in "Thumbnail field" must be insert primary Image URL your post.
- In the category field, you must choose the category related to your post. Note that different categories must be created through the Django admin section.

#### What’s contained in each file created.

**index.html:** this is a home page of the site. It includes menu, latest posts, categories, post display carousel, header, footer, sidebar, etc.

**listing.html:** this is page of the post. It includes thumbnail, Content of the post and etc.

**createnew.html:** This page is about creating a new post. Only the site admin has access to this page. `127.0.0.1:8000/create`

**category.html:** The page related to posts with the same category.

**login.html:** The page related to admin login. At the beginning of setting up the site, you can use the following username and password.
user: admin
password:admin
