"""
INTRODUCTION TO WORKING WITH APIs

For this section, our programs will use
a web application programming interface (API). We'll learn how to write
a self-contained program to generate a visualization based on data it retrieves.
This API will automatically request specific info. from a website rather than
entire pages. The information it gathers will be used to generate a visualization.
The data will always be up to date.

USING A WEB API
a web API is part of a website designed to interact with programs that use
very specific URLs to request certain information.

We call this request an API call.

The requested data will be returned in an easily processed format, either JSON or CSV.
Most apps that rely on external data sources, such as apps that integrate social media
websites, rely on these API calls.

GIT AND GITHUB
We'll base our visualization on information from GitHub, a site that we are already
familar with. GitHub is a site that allows programmers to collaborate on projects.

We will use GitHub's API to request information about Python projects on the site
and then generate an interactive visualization of the relative popularity of these
projects in Pygal.

WHAT IS GITHUB?
GitHub takes its root name in Git. Go figure!
A distributed version control system (VCS) that offers a plane for teams of
programmers to collaborate on projects.

Git helps people manage their individual work......sulum ver ti and so on

"""

### REQUESTING DATA USING AN API CALL

"""
To get an idea of what an API looks like, enter the following into your browser and hit enter:

https://api.github.com/search/repositories?q=language:python&sort=stars

