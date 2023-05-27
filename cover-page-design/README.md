# Book CoverPage Design

## AIM:

To design a static web site for a book cover page.

## DESIGN STEPS:

### Step 1:
  Start a django server
  
### Step 2:
  Add static Html templates and files required in Templates and static folders respectively.

### Step 3:
  Inside the Html file place the Html code.

### Step 4:
  Inside the CSS file, place in the CSS code and link the file to html using link tag.

### Step 5:
  Link the required images in Html file adding their respective paths.

### Step 6:

Validate the HTML and CSS code.

### Step 6:

Publish the website in the given URL.

## PROGRAM :

Html File:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'index.css' %}">
    <title>Document</title>
</head>
<body>
    <div class="cover">
        <br>
        <h2 class="Header">SEC INSIGHTS</h2>
        <hr class="short">
        <br>
        <h1 class="BookTitle">
            Fundamentals of web application development
        </h1>
        <h3>
            With Html, CSS, Python and Javascript.
        </h3>
        <div class="space"></div>
        <img class="right" src="{% static 'logo_r.png' %}" >
        <h2 class="footed"> Fifth Edition </h2> 
        <hr class="long">
        <h2 class="footsmall"> Mahinkumar </h2>
    </div>
</body>
</html>

```

CSS File:
```css
*{
    margin: 0;
    margin-left: 16%;
    margin-right: 16%;
    font-family: monospace;
    color: white
}

.cover{
    background-image: -moz-linear-gradient(rgb(35, 35, 88) 0 0);
    margin: 0;
    position: relative;
}

.Header{
    margin: 4%;
    font-size: 28px;
}

.BookTitle{
    margin: 4%;
    font-size: 48px;
    font-weight: 1500;
}

.short{
    margin:0;
    width:40%;
    color: rgb(0, 251, 255);
}

h3{
    font-size: 28px;
    margin: 4%;
}

.long{
    margin:0;
    width:47%;
    color: rgb(0, 251, 255);
}

.space{
    padding-bottom: 40%;
}

.footsmall{
    margin: 0%;
    font-size: 28px;
    padding-top: 2%;
    padding-left: 4%;
    padding-bottom: 2%;
}
.footed{
    margin: 4%;
    font-size: 28px;
    width: 40%;
}
.right{
    float: right;
    width: 20%;
}
```

## OUTPUT:

![Screenshot 2023-01-24 at 09-42-43 Document](https://user-images.githubusercontent.com/73975593/214210907-3ade7cbd-396a-4e0a-a92d-c31bfb8294f1.png)

## Result:
Hence a static web site for a book cover page has been designed.
