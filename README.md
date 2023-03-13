# UserManager

In order to login with Github and using it as oauth provider please follow the steps mentioned [here](https://idp.miniorange.com/login-using-github-as-oauth-server/) and update the follwing client/secrent keys in a .env file locally. 

```
SOCIAL_AUTH_GITHUB_KEY=
SOCIAL_AUTH_GITHUB_SECRET=
```

### Install Requirements

Activate a virtual env 

```
source venv/bin/activate
```

inside the virtual environment, Run this 

`pip install -r requirements.txt`

### Run Server
```
./manage.py runserver
```

Attached the following screenshots to get basic idea. 



<img width="347" alt="Screenshot 2023-03-13 at 20 50 02" src="https://user-images.githubusercontent.com/7334669/224816676-771295ca-cfe7-4c30-8993-7e3e9860e0dd.png">


<img width="340" alt="Screenshot 2023-03-13 at 20 50 16" src="https://user-images.githubusercontent.com/7334669/224816737-fbc019f5-cfdb-4a11-8bcb-5eaf3fc94d28.png">
<img width="369" alt="Screenshot 2023-03-13 at 20 50 27" src="https://user-images.githubusercontent.com/7334669/224816785-ddfce936-129b-402a-81a2-cc416a9066dd.png">
<img width="388" alt="Screenshot 2023-03-13 at 20 52 17" src="https://user-images.githubusercontent.com/7334669/224817127-970cd5d2-7b7d-40c7-8671-1f6adf2014c6.png">
<img width="445" alt="Screenshot 2023-03-13 at 20 50 46" src="https://user-images.githubusercontent.com/7334669/224816839-7de28b7e-e2f6-4ccd-9028-c329b3d1787f.png">

<img width="395" alt="Screenshot 2023-03-13 at 20 52 47" src="https://user-images.githubusercontent.com/7334669/224817205-2df558b0-4da3-477d-90f5-c8fc05b40310.png">
