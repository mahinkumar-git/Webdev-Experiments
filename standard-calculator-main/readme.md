# Design of a Standard Calculator

## AIM:

To design a web application for a standard calculator.

## DESIGN STEPS:

### Step 1:
Clone the template repository and Create a new django project named calculator using
```django-admin startproject calculator```. 

### Step 2:
Get to the calculator directory in the terminal using ```cd calculator``` and create
a folder name static.

### Step 3:
In settings.py import os and add the line ```STATICFILE_DIRS = [os.path.join(BASE_DIR,'static')]```

### Step 4:
Next inside static folder place your Html files and CSS file and other required assets.

### Step 5:
Validate the HTML and CSS code.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
### File: index.html
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Calculator</title>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        <form name="form1" onload="result.value=''">
            <h1 class="name">Simple Calculator</h1>
        <table id="calc">
            <tr>
                <td colspan="4">
                    <input type="text" id="result">
                </td>
            </tr>
            <tr>
                <td><input type="button" value="1" onclick="result.value+='1'"/></td>
                <td><input type="button" value="2" onclick="result.value+='2'"/></td>
                <td><input type="button" value="3" onclick="result.value+='3'"/></td>
                <td><input type="button" value="+" onclick="result.value+='+'"/></td>
            </tr>
            <tr>
                <td><input type="button" value="4" onclick="result.value+='4'"/></td>
                <td><input type="button" value="5" onclick="result.value+='5'"/></td>
                <td><input type="button" value="6" onclick="result.value+='6'"/></td>
                <td><input type="button" value="-" onclick="result.value+='-'"/></td>
            </tr>
            <tr>
                <td><input type="button" value="7" onclick="result.value+='7'"/></td>
                <td><input type="button" value="8" onclick="result.value+='8'"/></td>
                <td><input type="button" value="9" onclick="result.value+='9'"/></td>
                <td><input type="button" value="*" onclick="result.value+='*'"/></td>
            </tr>
            <tr>
                <td><input type="button" value="/" onclick="result.value+='/'"/></td>
                <td><input type="button" value="0" onclick="result.value+='0'"/></td>
                <td><input type="button" value="." onclick="result.value+='.'"/></td>
                <td><input type="button" value="=" onclick="result.value=eval(result.value)"/></td>
            </tr>
            <tr>
                <td colspan="4">
                    <input type="button" value="Clear all" id="clear" onclick="result.value=''">
                </td>
            </tr>
        </table>
        </form>
    </body>
</html>
```

### File: index.css
```css
table{
    border: 1px solid orange(17, 16, 16);
    margin-left: auto;
    margin-right: auto;
}
input[type="text"]{
    border: 1px solid orange(15, 13, 13);
    padding: 50px 50px;
    font-size: 32px;
    font-weight: bold;
    border-radius: 2px;
}
input[type="button"]{
    width: 100%;
    padding: 50px 50px;
    background-color:rgb(32, 51, 178);
    border-radius: 2px;
    font-size: 24px;
    color: white;
}
.name{
    margin:0;
    margin: 0% 33.7% 0% 33.7%;
    background-color:rgb(32, 51, 178) ;
    color: white;
    text-align: center;
    float:center;
}
```

## OUTPUT:
![Screenshot 2023-01-26 at 09-54-36 Calculator](https://user-images.githubusercontent.com/73975593/214758298-bdeaaa86-dc62-4457-8919-0fa3c3f59db5.png)

## Result:
Hence a web application is designed for a standard calculator.
