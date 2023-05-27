# Event Registration Web Application

## AIM:
To design, develop and deploy a web application for event registration.

## DESIGN STEPS:

### Step 1:
Plan required information to be obtained from the user.

### Step 2:
With the basic requirements in mind, design a prototype for the website using 
a software like figma or Pencilproject.

### Step 3:
Improve the prototype till required form is arrived. Now based on the prototype
design the website using Html and css.

### Step 4:
Start a django project and add the required assets in the static folder of the project.

### Step 5:
Link the html and Css file together and validate the site with the prototype.

### Step 6:
Validate the HTML and CSS code.

### Step 6:
Publish the website in the given URL.

## DESIGN:
Designed in Pencil project.
![eventreg_design](https://user-images.githubusercontent.com/73975593/214781824-a7b70942-a534-4b1e-9e40-43d8b7a85b03.png)


## PROGRAM :
### File: index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="index.css">
</head>

<body>
    <div class="Header">
        <h1>EVENT REGISTRATION<br>CODING COMPETITION</h1>
    </div>
    <form>
        <div class="leftp">
            <h3>First Name: </h3> <input type="text">
            <h3>Phone Number: </h3> <input type="number">
            <h3>Email Id:</h3><input type="email">
        </div>
        <div class="rightp">
            <h3>Last Name: </h3> <input type="text">
            <h3>Preferred coding language: </h3> <input type="text">
            <h3>Experience Level:</h3> <input type="text">
        </div>
        <br>
        <div class="below">
            <h3>Have you participated in a coding event before ? <input type="radio"> Yes <input type="radio"> No</h3>
        </div>
        <br>
        <img src="time.png" class="img" width="96%">
        <br>
        <br>
        <h3 class="below">Select Events to participate: <input type="checkbox">-Hackathon--- <input
                type="checkbox">-Team coding--- <input type="checkbox">-Competitive coding--- <input
                type="checkbox">-Bug fix---</h3>
        <br>
        <h3 class="below">How did you know about coding competition: <input type="checkbox">-Newspaper----<input
                type="checkbox">-Telivision----<input type="checkbox">-Youtube Advertisement----<input
                type="text">-other</h3>
    </form>
    <br>
    <button class="below" type="button">Reset Form</button> <button type="button">Submit</button>
</body>

</html>
```

### File: index.css
```css
* {
    margin: 0%;
}

.Header {
    height: 15%;
    background-color: rgb(186, 186, 186);
    padding: 1% 0 1% 0;
    text-align: center;
}

.leftp {
    padding-top: 5%;
    padding-left: 2%;
    width: 50%;
    float: left;
    font-size: 17px;
}

.leftp>input {
    width: 90%;
    font-size: 14px;
}

.rightp {
    padding-top: 5%;
}

.rightp>input {
    width: 45%;
    font-size: 14px;
}

.below {
    margin-left: 2%;
}

tr {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.img {
    padding-left: 2%;
}
```

## OUTPUT:
![Screenshot 2023-01-26 at 13-09-37 Document](https://user-images.githubusercontent.com/73975593/214781869-983c160c-20c5-410a-973a-d5c3abc627ad.png)


## Result:
Hence a website has been designed, developed and deployed for event registration.
