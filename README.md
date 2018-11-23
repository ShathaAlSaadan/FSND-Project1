
This project is part of full stack nano degree program from udacity, it's about analyzing the logs for newspaper site by building internal reporting tool that will use information from newsdata database to discover what kind of articles the site's readers like.
the newsdata DB contain three tables articles, authors, and log.
the reporting tool answer these three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

in order to run this project you need PostgreSQL Database (which is provided at the end with all required software) and installing Linux virtual machine and vagrant.
After installation you have to run these commad in git bash( if you are using windows):
vagrant up => to bring the VM online
then run vagrant ssh command and inside the directory that contains the newsdata DB use the command psql -d news -f newsdata.sql at the end you can run python log.py to run the python code that contain the results of the three questions.

software required to run this project:
git: https://git-scm.com/download/win
python 3: https://www.python.org/downloads/
VM.: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
Vagrant: https://www.vagrantup.com/downloads.html
news db: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip