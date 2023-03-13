# How to make a local repository on your computer and then push it to a blank repository on the Github.

Open a folder (or create a folder if you dont have one already), in my case I made a folder in VS code and then i added a .py file.
Login to your GitHub account and make a "Blank" respository.(dont add any file in it, just add a name for it)
Open your folder in the VS code and go to the command line.
Add a command , "git init"
This will initiate an empty repository. 
Now go to your GitHub repository and copy the path. in my case the path was https://github.com/ayesha-python2023/Blank.git
Within the VS code enter this command in the command line, "git remote add origin https://github.com/ayesha-python2023/Blank.git"
Make sure to save all your changes in the files.
Then enter this commands "git branch -M main"
Then enter another command "git push -u origin main"
Now go to your GitHub page , refresh it and find your files there.
