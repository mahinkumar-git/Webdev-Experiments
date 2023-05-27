# Places Around Me
## AIM:
To develop a website to display details about the places around my house.

## Design Steps:

### Step 1:
Open up a terminal in your preffered location, and start a django project using ```djang-admin startproject <your-project-name>```
Next setup an app inside the project folder using ```django-admin startapp <your-app-name>``` 

### Step 2:
Once Created ,link your app to the project by adding it in the list of apps in settings.py file located inside the project folder.
Add access to your host in allowed host setting and add static folders path to your settings.py file. 

### Step 3:
Create a static folder and template folder and add all your required files for the project - Images .etc in 
your static folder. In the Template folder add your html files required for the pages.

### Step 4:
Head to the views.py in your app folder and create required functions to render a particular page or template when requested by the
client. Next go to the urls.py and route the correct view functions to each particular request as needed.

### Step 5: 
Next start the server from the projects main directory using ```python3 manage.py runserver 0:<portnumber>```.
Now the pages can be accessed from all the routed addresses in urls.py .

## Code:

### File: index.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width*0.8, initial-scale=0.8">
      <link rel="stylesheet" href="{% static 'index.css' %}">
      <title>Places_around_me</title>
   </head>

   <body>
        <div class="column">
            <h1 class="brush">PLACES AROUND ME</h1>
            </div>
            <div class="column2">
            <h3 class="brush">Click on a location in the map to know about</h3>
            <links>
                <a href="/Anna_Stadium" > Anna Stadium </a><a href="/Cuddalore_post_office" > Cuddalore post office</a><a href="/Gedilam_River_Bridge" > Gedilam River Bridge </a><a href="/Cuddalore_Bus_Stand" > Cuddalore Bus Stand</a><a href="/Cuddalore_railway_station" > Cuddalore Railway Station </a>
            </links>
        </div>
        <div>
            <img id="map" src="{% static 'Map.jpg' %}" width="1536" height="778" orgWidth="1536" orgHeight="778" usemap="#map" alt="" />
            <map name="map" id="map">
                <area shape="rect" coords="1534,776,1536,778" alt="Image Map" style="outline:none;" title="Image Map"  />
                <area  alt="" title="Cuddalore Railway Station" href="/Cuddalore_railway_station" shape="poly" coords="255,547,316,671,378,655,301,524,301,522,260,507" style="outline:none;" target="_self"     />
                <area  alt="" title="Cuddalore Bus stand" href="/Cuddalore_Bus_Stand" shape="poly" coords="382,706,515,697,533,771,406,766" style="outline:none;" target="_self"     />
                <area  alt="" title="Anna Stadium" href="/Anna_Stadium" shape="poly" coords="1207,75,1403,98,1397,270,1198,258" style="outline:none;" target="_self"     />
                <area  alt="" title="Cuddalore post office" href="/Cuddalore_post_office" shape="poly" coords="922,56,985,82,1014,0,942,0" style="outline:none;" target="_self"     />
                <area  alt="" title="Bridge" href="/Gedilam_River_Bridge" shape="poly" coords="655,622,680,685,842,594,801,553" style="outline:none;" target="_self"     />
            </map>
        </div>
    </body>
</html>
```

### File: index.css
```css
* {
	background: rgb(220, 248, 255);
	font-family: monaco, Consolas, Lucida Console, monospace;
}

.column {
	float: left;
	width: 25%;
	padding: Auto;
	background-color: #00ADB5;
}

.column2 {
	float: right;
	width: 75%;
}


h1 {
	color: #222831;
	background-color: #00ADB5;
}

links {
	background-color: #00ADB5;
	font-size: medium;
	display: flex;
	flex-direction: row;
	justify-content: space-evenly;
}

a {
	background-color: #00ADB5;
	color: aliceblue;
	font-size: large;
	text-decoration: none;
	padding: 0.1%;
	padding-left: 2.2%;
	padding-right: 2.2%;
	font-size: medium;
	color: #222831;
	
}

a:hover {
	background-color: #393E46;
	color: #00ADB5;
}
```

### File: bridge.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gedilam River Bridge</title>
    <link rel="stylesheet" href="{% static 'placetemplate.css' %}">
</head>
<body>
    <h1 class="brush">Gedilam River Bridge</h1>
    <div class="column1">
        <img src="{% static 'Bridge.jpg' %}" width="600px" height="400px">
    </div>
    <div class="column2">
        <p>Every day atleast 12000 vehicles pass through the Gedilam river bridge. The older Bridge was constructed on 1864 during the french regime.
           the newer one nearby was very recently constructed. As the intensity of vehicle passing by grew over time. The Bridge now connects the most
        the important parts of the city and remains a very busy spot. </p>
    </div>
</body>
</html>
```

### File: busstand.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuddalore Bus Stand</title>
    <link rel="stylesheet" href="{% static 'placetemplate.css' %}">
</head>
<body>
    <h1 class="brush">Cuddalore Bus Stand</h1>
    <div class="column1">
        <img src="{% static 'bus_stand.png' %}" width="500px" height="400px">
    </div>
    <div class="column2">
        <p>The Cuddalore Bus Stand can host upto a 100 buses. It is always busy with travellers and traders with goods. The bus stand is sorrounded
            by several small and large scale shops which sells variety of products. About 10 buses enter and leave the stand every one minute.  </p>
    </div>
</body>
</html>
```

### File: postoffice.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuddalore Post Office</title>
    <link rel="stylesheet" href="{% static 'placetemplate.css' %}">
</head>
<body>
    <h1 class="brush">Cuddalore Post Office</h1>
    <div class="column1">
        <img src="{% static 'post_office.png' %}" width="500px" height="400px">
    </div>
    <div class="column2">
        <p>The Cuddalore Post Office is the main head office in cuddalore district, It offers all postal services like delivery of mails and parcels, money transfer
            banking, Insurance and retail services. It also provides other services including passport applications, P.O. Box distribution and other 
            delivery services. </p>
    </div>
</body>
</html>
```

### File: railway.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuddalore Railway Station</title>
    <link rel="stylesheet" href="{% static 'placetemplate.css' %}">
</head>
<body>
    <h1 class="brush">Cuddalore Railway Station</h1>
    <div class="column1">
        <img src="{% static 'railways.png' %}" width="600px" height="400px">
    </div>
    <div class="column2">
        <p>Cuddalore has Three major railway stations, namely, Cuddalore Port Junction and Tiruppadirippuliyur Cuddalore Castle, Varakalpattu Cuddalore Moffusil both on the Viluppuram 
            Mayiladuthurai Tiruchirappalli Mainline Section.The Cuddalore railway station, the most important railway station of Cuddalore has
            two platforms and is located close to the Cuddalore bus stand. There are express and passenger trains on either side, connecting various cities with Tamil Nadu. There are
            daily express trains to many cities. </p>
    </div>
</body>
</html>
```

### File: Anna_stadium.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anna stadium</title>
    <link rel="stylesheet" href="{% static 'placetemplate.css' %}">
</head>
<body>
    <h1 class="brush">Anna stadium</h1>
    <div class="column1">
        <img src="{% static 'anna-stadium.avif' %}" width="600px" height="400px">
    </div>
    <div class="column2">
        <p>The Anna Stadium is a stadium at the Anna Sports Complex located in Cuddalore. The main football and athletics stadium, Anna Stadium, has a capacity of 10,000. .The complex also houses a multi-purpose indoor
            stadium and has separate courts for sports such as tennis, badminton, basketball, football, kabaddi, hockey, and volleyball.</p>
    </div>
</body>
</html>
```

### File: placetemplate.css
```css
* {
	background: rgb(220, 248, 255);
	font-family: monaco, Consolas, Lucida Console, monospace;
	text-align: center;
}

.column1 {
	float: left;
	width: 40%;
	padding: Auto;
	background-color: #00ADB5;
}

.column2 {
	float: right;
	width: 60%;
}

p{
	padding: 1%;
	font-size: large;
	text-align: left;
}
h1 {
	color: #222831;
	background-color: #00ADB5;
	padding: 0%;
	font-size: 48px;
}
```

## Output:
![Screenshot 2023-01-14 at 21-27-37 Places_around_me](https://user-images.githubusercontent.com/73975593/212481526-5675a61d-47e9-4d1a-b3b1-1e72adcecc06.png)
![Screenshot 2023-01-14 at 21-27-50 Anna stadium](https://user-images.githubusercontent.com/73975593/212481531-553b682a-4b2f-44fc-9545-0ae223259252.png)
![Screenshot 2023-01-14 at 21-27-57 Cuddalore Post Office](https://user-images.githubusercontent.com/73975593/212481539-57fbf02a-935a-4ce1-9774-5ae210081eb8.png)
![Screenshot 2023-01-14 at 21-28-05 Gedilam River Bridge](https://user-images.githubusercontent.com/73975593/212481555-742f45ed-203a-4827-b70c-7a0ea2a5eb18.png)
![Screenshot 2023-01-14 at 21-28-17 Cuddalore Bus Stand](https://user-images.githubusercontent.com/73975593/212481559-abed6b12-614d-4986-8c49-4c789580ad07.png)
![Screenshot 2023-01-14 at 21-28-25 Cuddalore Railway Station](https://user-images.githubusercontent.com/73975593/212481568-2153cf94-f50a-4824-b471-f148721e9114.png)

##  Result:
Hence a website has been developed to display details about the places around my house.
