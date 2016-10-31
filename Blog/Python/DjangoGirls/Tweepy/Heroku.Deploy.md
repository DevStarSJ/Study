git init
git add .
git commit -m "Init Commit"

heroku login
heroku create [APP_NAME]

git push heroku master
