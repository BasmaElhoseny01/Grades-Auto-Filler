# Grades Auto Filler
 Image Processing Grades Auto filler Project 😉😉


## <img  align= center width=50px height=50px src="https://thumbs.gfycat.com/HeftyDescriptiveChimneyswift-max-1mb.gif">Table of Content

- <a href ="#overview">Overview</a>
- <a href ="#started">Get Started</a>
- <a href ="#graded_sheet">Graded Sheet Model</a>
  - <a href ="#graded_sheet_overview">Overview</a>
  - <a href ="#graded_sheet_flow">Flow Diagram</a>
  - <a href ="#graded_sheet_results">Results</a>
- <a href ="#bubble_sheet">Bubble Sheet Model</a>
  - <a href ="#bubble_sheet_overview">Overview</a>
  - <a href ="#bubble_sheet_flow">Demo Video</a>
- <a href ="#contributors">Contributors</a>
- <a href ="#license">License</a>


## <img  align= center width=50px height=50px src="https://media3.giphy.com/media/psneItdLMpWy36ejfA/source.gif"> Overview<a id = "overview"></a>
- Project Based on Image Processing Techniques
- We have 2 models
  - Graded Sheet Model
  - Bubble Sheet Model
- <a href="https://github.com/BasmaElhoseny01/Grades-Auto-Filler/blob/main/Grades%20autofiller%20%5BOptional%20Idea%5D.pdf">Project Description</a>

## <img  align= center width=50px height=50px src="https://user-images.githubusercontent.com/72309546/215230425-03645465-e762-42ae-9772-947ca1b01401.png">Technology <a id = "Technolgies"></a>

<div>
<img height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" />

<img height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" />

<img height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/800px-OpenCV_Logo_with_text_svg_version.svg.png" />
<img height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png" />
<img height="40" src="https://miro.medium.com/max/490/1*9Gbo-HOvajpbya5RsLN1uw.png" />
<img height="40" src="https://i0.wp.com/iot4beginners.com/wp-content/uploads/2020/04/65dc5834-de21-4e2e-bd4d-5e0c3c6994dd.jpg?fit=375%2C422&ssl=1" alt="GUI tool for python"/>
</div>

## <img  align= center width=50px height=50px src="https://cdn.pixabay.com/animation/2022/07/31/06/27/06-27-17-124_512.gif">Get Started <a id = "started"></a>

<ol>
<li>Clone the repository

<br>

```
git clone https://github.com/BasmaElhoseny01/Grades-Auto-Filler.git
```

</li>

<li>Install Packages

<br>

```
pip install -r requirements.txt
```

</li>

<li>Run the app

<br>

```
python app.py
```

</li>
</ol>

<h2 align=center > <img  align=center width=50px height=50px src="https://user-images.githubusercontent.com/72309546/214907431-b4e250f1-9b3a-4149-b7b4-bbd17b833b97.png">Graded Sheet Model <a id = "graded_sheet"></a>
</h2>


### <img  align= center width=50px height=50px src="https://media1.giphy.com/media/3ohzdWYbITsO2Y5rbi/giphy.gif?cid=6c09b9523ys3hxe1y9ueyo5ab7nzkbhv9oev797jvb5bz6rt&rid=giphy.gif&ct=s"> OverView<a id = "graded_sheet_overview"></a>

- It allows you to fill the grades electronically
- It handles Skewing and orientation
- Printed Student ID is detected using OCR and Feature and execration
- Written Symbols like ✓ & x are detect using HOG feature extractor and predicted using SVM
- Handwritten Code Values are detected using OCR and Feature and execration

***

### <img  align= center width=50px src="https://i2.wp.com/www.rankred.com/wp-content/uploads/2019/07/AI-solves-Rubik-Cube.gif?fit=800%2C433&ssl=1">Flow Diagram<a id = "graded_sheet_flow"></a>
<br>
<img  align=center width=500px src="https://user-images.githubusercontent.com/72309546/214973165-b164f1f5-1220-425b-b27a-c39ed6bb6422.jpg">

<br>

***

### <img  align= center width=50px height=50px src="https://cdn-icons-png.flaticon.com/512/1589/1589689.png"> Results<a id = "graded_sheet_results"></a>

<h4 align=center> <img  align= center width=50px height=50px src="https://media1.giphy.com/media/ZecwzuvmRrjOHsXNcI/giphy.gif?cid=6c09b9523btueuk8qe6usw2cnpb7qn8ki6evjwp62n2xiyi7&rid=giphy.gif&ct=s"> Grade Sheet (1)<a id = "results"></a>
</h4>


<table>
  <tr>
    <td width=40% valign="center"><img src="https://user-images.githubusercontent.com/72309546/214974224-78a989df-7c81-4493-ad32-78d708ab7128.jpg"/></td>
    <td width=40% valign="center"><img src="https://user-images.githubusercontent.com/72309546/214975386-6cea9197-86ae-4ddb-a560-5cb6e892744b.png"/></td>
  </tr>
</table>

<img width="855" alt="s8" src="https://user-images.githubusercontent.com/72309546/214975379-f8e21411-357c-4315-99b9-b4bdaab58f35.png">

<h4 align=center> <img  align= center width=50px height=50px src="https://media1.giphy.com/media/ZecwzuvmRrjOHsXNcI/giphy.gif?cid=6c09b9523btueuk8qe6usw2cnpb7qn8ki6evjwp62n2xiyi7&rid=giphy.gif&ct=s"> Grade Sheet (2)<a id = "results"></a>
</h4>

<table>
  <tr>
    <td width=40% valign="center"><img src="https://user-images.githubusercontent.com/72309546/214974691-2800aa3c-9118-4828-95d6-86c021faf902.jpg"/></td>
    <td width=40% valign="center"><img src="https://user-images.githubusercontent.com/72309546/214975080-ca47d906-f7ef-472c-ae91-098fd46b0525.png"/></td>
  </tr>
</table>

<img width="836" alt="s1" src="https://user-images.githubusercontent.com/72309546/214975070-ab030140-ba6a-4965-a3ae-82b31ed4d174.png">

***

<h2 align=center > <img  align=center width=50px height=50px src="https://user-images.githubusercontent.com/72309546/214907431-b4e250f1-9b3a-4149-b7b4-bbd17b833b97.png">Bubble Sheet Model <a id = "bubble_sheet"></a>
</h2>

### <img  align= center width=50px height=50px src="https://media1.giphy.com/media/3ohzdWYbITsO2Y5rbi/giphy.gif?cid=6c09b9523ys3hxe1y9ueyo5ab7nzkbhv9oev797jvb5bz6rt&rid=giphy.gif&ct=s"> OverView<a id = "bubble_sheet_overview"></a>

- It handles different ink colors
- It allows different formats for the sheet ( but bubbles must be vertically aligned in all formats )
- Differnet number of questions
- Differnet number of choices
- It handles Skewing and orientation
- Printed Student ID is detected using OCR ( ID must be in a box )

***

### <img  align= center width=50px src="https://i2.wp.com/www.rankred.com/wp-content/uploads/2019/07/AI-solves-Rubik-Cube.gif?fit=800%2C433&ssl=1">Demo Video<a id = "bubble_sheet_flow"></a>
<br>

[bubble sheet demo video.webm](https://user-images.githubusercontent.com/72188665/215342210-81379189-88bc-4f78-a35a-191e8a0ddcb1.webm)

<br>
Backup link : <a href="https://www.youtube.com/watch?v=WZZoWZTEEj0"> Demo </a>

***
 
## <img  align= center width=50px height=50px src="https://media1.giphy.com/media/WFZvB7VIXBgiz3oDXE/giphy.gif?cid=6c09b952tmewuarqtlyfot8t8i0kh6ov6vrypnwdrihlsshb&rid=giphy.gif&ct=s"> Contributors <a id = "contributors"></a>

<table>
  <tr>
    <td align="center">
    <a href="https://github.com/BasmaElhoseny01" target="_black">
    <img src="https://avatars.githubusercontent.com/u/72309546?s=400&u=1aee927020f5bd13f5020273aea97f676a175502&v=4" width="150px;" alt="Basma Elhoseny"/>
    <br />
    <sub><b>Basma Elhoseny</b></sub></a>
    </td>
    <td align="center">
    <a href="https://github.com/zeinabmoawad" target="_black">
    <img src="https://avatars.githubusercontent.com/u/92188433?v=4" width="150px;" alt="Zeinab Moawad"/>
    <br />
    <sub><b>Zeinab Moawad</b></sub></a>
    </td>
        </td>
    <td align="center">
    <a href="https://github.com/emanshahda" target="_black">
    <img src="https://avatars.githubusercontent.com/u/89708797?v=4" width="150px;" alt="Eman Shahda"/>
    <br />
    <sub><b>Eman Shahda</b></sub></a>
    </td>
        </td>
    <td align="center">
    <a href="https://github.com/MUSTAFA-Hamzawy" target="_black">
    <img src="https://avatars.githubusercontent.com/u/72188665?v=4" width="150px;" alt="Mustafa Hamzawy"/>
    <br />
    <sub><b>Mustafa Hamzawy</b></sub></a>
    </td>
  </tr>
 </table>


## <img  align= center width=50px height=50px src="https://media1.giphy.com/media/ggoKD4cFbqd4nyugH2/giphy.gif?cid=6c09b9527jpi8kfxsj6eswuvb7ay2p0rgv57b7wg0jkihhhv&rid=giphy.gif&ct=s"> License <a id = "license"></a>
This software is licensed under MIT License, See [License](https://github.com/BasmaElhoseny01/Grades-Auto-Filler/blob/main/LICENSE) for more information ©Basma Elhoseny.
