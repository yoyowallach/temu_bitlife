First, identify the branch your changes are on.
If you are alone, use your branch, `Yotam` or `Odelia`. If you are together, use the `Both` branch.
Never EVER use the `main` branch.

Then go to the git menu. Make sure you are signed into your Github Account
At the top, there will be a branch selector, click the branch your code is on and make sure your changes are in the `Review Changes` box.

Write a sumarry of your changes.

**NOTE TO ODELIA**: Write a **DETAILED** summary, dont use abbreviations that i wont know like "miskilik"

Then stage and commit your changes

Then you need to push your commits with the push button

Now you need to make a pull request (merge request)

Go to the shell and copy and paste this
```
gh pr create --base main --head [BRANCH] --title "Your PR title" --body "Description of the changes"
```
make sure to replace [BRANCH] with the actual branch **MATCH CASE**

`Your PR title` and `Description of the changes` dont need to be all that deatailed.

Execute the command and wait for approval!

# **MAKE SURE TO TALK WITH YOTAM BEFORE MAKING YOUR FIRST PR. YOU NEED SPECIAL REQUIREMENTS THAT REQUIRE SETUP**