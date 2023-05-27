# Web Design for a Software Product Company

## AIM:

To design a static website for a software product company company.

## DESIGN STEPS:

### Step 1:

Requirement collection.

### Step 2:

Creating the layout using HTML and CSS.

### Step 3:

Updating the sample content.

### Step 4:

Choose the appropriate style and color scheme.

### Step 5:

Validate the layout in various browsers.

### Step 6:

Validate the HTML code.

### Step 6:

Publish the website in the given URL.

## PROGRAM :

### File: index.html 
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soft-protection : Home</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu" />
</head>

<body>
    <div class="Header">
        <h1 class="name">SOFT-PROTECTION</h1>
    </div>
    <div class="Navbar">
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/people">People</a>
        <a href="/contact">Contact us</a>
    </div>
    <div class="Body">
        <h1 class="Welcome">Next generation computer <br> protection software.</h1>
        <br>
        <div class="el_body">
            <a href="/products">Products ></a>
            <a href="/about us">About us ></a>
            <a href="/people">People ></a>
            <a href="/contact us">Contact us ></a>
        </div>
    </div>
    <footer>
        <h2>copyright @ soft-protection.com, Developed by Mahinkumar</h2>
    </footer>
</body>

</html>
```

### File: products.html
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soft-protection : Products</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu" />
</head>

<body>
    <div class="Header">
        <h1 class="name">SOFT-PROTECTION</h1>
    </div>
    <div class="Navbar">
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/people">People</a>
        <a href="/contact">Contact us</a>
    </div>
    <div class="Bodypeople">
        <h1>Check out our products.</h1>
        <div class="peoplecolumn">
            <div class="peoplerow">
                <img src="{% static 'Product_icon/Diamond_protection_personal.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/Diamond_protection_teams.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/Diamond_protection.png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>Diamond - Personal - ₹350<br>Per person for 1 month</h2>
                <h2>Diamond - Teams - ₹330<br>Per person for 1 month</h2>
                <h2>Diamond - Enterprise - ₹300<br>Per person for 1 month</h2>
            </div>
            <div class="peoplerow">
                <img src="{% static 'Product_icon/platinum_protection_personal.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/platinum_protection_teams.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/platinum_protection.png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>Platinum - Personal - ₹150<br>Per person for 1 month</h2>
                <h2>Platinum - Teams - ₹130<br>Per person for 1 month</h2>
                <h2>Platinum - Enterprise - ₹100<br>Per person for 1 month</h2>
            </div>
            <div class="peoplerow">
                <img src="{% static 'Product_icon/gold_protection_personal.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/gold_protection_teams.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/gold_protection.png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>Gold - Personal - ₹250<br>Per person for 1 month</h2>
                <h2>Gold - Teams - ₹230<br>Per person for 1 month</h2>
                <h2>Gold - Enterprise - ₹200<br>Per person for 1 month</h2>
            </div>
            <div class="peoplerow">
                <img src="{% static 'Product_icon/Standard_protection_personal.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/Standard_protection_teams.png'%}" width="250px" height="250px">
                <img src="{% static 'Product_icon/Standard_protection.png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>Standard - Personal - ₹50<br>Per person for 1 month</h2>
                <h2>Standard - Teams - ₹30<br>Per person for 1 month</h2>
                <h2>Standard - Enterprise - ₹10<br>Per person for 1 month</h2>
            </div>
        </div>
    </div>
    <footer>
        <h2>copyright @ soft-protection.com, Developed by Mahinkumar</h2>
    </footer>
</body>

</html>
```

### File: people.html
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soft-protection : People</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu" />
</head>

<body>
    <div class="Header">
        <h1 class="name">SOFT-PROTECTION</h1>
    </div>
    <div class="Navbar">
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/people">People</a>
        <a href="/contact">Contact us</a>
    </div>
    <div class="Bodypeople">
        <h1>Meet the Incredible team...</h1>
        <div class="peoplecolumn">
            <div class="peoplerow">
                <img src="{% static 'Peopleicon(0).png'%}" width="250px" height="250px">
                <img src="{% static 'Peopleicon(1).png'%}" width="250px" height="250px">
                <img src="{% static 'Peopleicon(2).png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>| ----------- JOE ----------- |<br>Senior Developer</h2>
                <h2>| ----------- TIM ----------- |<br>Security Expert</h2>
                <h2>| ----------- BOB ----------- |<br>Security Expert</h2>
            </div>
            <div class="peoplerow">
                <img src="{% static 'Peopleicon(3).png'%}" width="250px" height="250px">
                <img src="{% static 'Peopleicon(4).png'%}" width="250px" height="250px">
                <img src="{% static 'Peopleicon(5).png'%}" width="250px" height="250px">
            </div>
            <div class="peoplerown">
                <h2>| ----------- ALEX ---------- |<br>Frontend Developer</h2>
                <h2>| -------- STEPHEN --------- |<br>Frontend Designer</h2>
                <h2>| ----------- JEB ----------- |<br>Junior Developer</h2>
            </div>
        </div>
    </div>
    <footer>
        <h2>copyright @ soft-protection.com, Developed by Mahinkumar</h2>
    </footer>
</body>

</html>
```

### File: contactus.html
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soft-protection : Contact us</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu" />
</head>

<body>
    <div class="Header">
        <h1 class="name">SOFT-PROTECTION</h1>
    </div>
    <div class="Navbar">
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/people">People</a>
        <a href="/contact">Contact us</a>
    </div>
    <div class="Body">
        <h1>
            Contact us:<br>
            <br>
            Email: <i>contact@Soft-protection.com</i><br>
            Mobile No.: <i>123-456-7890</i><br>
            Address:<br>
            <i>Soft-protection-Building</i>
            <br><i>Chennai, Tamilnadu. </i>
        </h1>
    </div>
    <footer>
        <h2>copyright @ soft-protection.com, Developed by Mahinkumar</h2>
    </footer>
</body>

</html>
```

### File: style.css
```css
* {
    font-family: ubuntu;
    margin: 0;
}

.name {
    color: white;
}

.Header {
    width: 30%;
    float: left;
    padding: 1%;
    text-align: center;
    background-color: rgb(12, 12, 12);
}

.Body {
    background-image: url('index.png');
    padding-top: 16%;
    padding-bottom: 16%;
    padding-left: 5%;
    color: white;
}

.Navbar {
    padding-top: 1%;
    padding-bottom: 1%;
    background-color: rgb(31, 31, 31);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.el_body {
    padding-left: 2%;
    display: flex;
    flex-direction: column;
}

.welcome {
    position: absolute;
}

.Navbar>a {
    text-decoration: none;
    font-size: 28px;
    color: rgb(81, 118, 250);
    transition: all 0.3s;
}

.el_body>a {
    text-decoration: none;
    font-size: 28px;
    padding-left: 2%;
    color: rgb(81, 118, 250);
    transition: all 0.3s;
}

a:hover {
    text-decoration: none;
    font-size: 28px;
    color: violet;
}

.peoplerow {
    display: flex;
    padding-left: 3%;
    padding-right: 3%;
    padding-top: 3%;
    padding-bottom: 1%;
    flex-direction: row;
    justify-content: space-evenly;
}

.peoplecolumn {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}

.Bodypeople {
    padding-top: 2%;
    padding-left: 2%;
    background-color: rgb(26, 26, 26);
    text-align: left;
}

.peoplerown {
    display: flex;
    padding-left: 3%;
    padding-right: 3%;
    padding-bottom: 3%;
    flex-direction: row;
    justify-content: space-evenly;
}

h1 {
    color: white;
}

h2 {
    color: white;
    text-align: center;
}

footer {
    padding-top: 1%;
    padding-bottom: 1%;
    background-color: rgb(31, 31, 31);
    font-size: small;
}
```
## OUTPUT:

### Home Page:
![Screenshot 2023-01-26 at 10-25-02 Soft-protection Home](https://user-images.githubusercontent.com/73975593/214761541-8413e1fe-b51d-46eb-916a-e397b15572c0.png)

### PRODUCT PAGE:
![Screenshot 2023-01-26 at 10-25-10 Soft-protection Products](https://user-images.githubusercontent.com/73975593/214761558-585d7aed-621d-4c8e-a2f0-8d76ffe39da6.png)


### PEOPLE PAGE:
![Screenshot 2023-01-26 at 10-28-07 Soft-protection People](https://user-images.githubusercontent.com/73975593/214761810-fd7f049a-d177-4757-b009-de8690c6ef05.png)


### CONTACT US PAGE:
![Screenshot 2023-01-26 at 10-25-23 Soft-protection Contact us](https://user-images.githubusercontent.com/73975593/214761594-07c0cb7e-65ff-4923-ad50-383b03fecd52.png)


## Result:

Thus a website is designed for the software product company and the HTML,CSS code are validated.
