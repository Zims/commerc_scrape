<h1>commerc_scrape</h1>
Development is ongoing.<br>
I pick even harder to scrape sites and scrape them for more data<br><br>

commerc_scrape is a personal project to use my knowledge in scraping the web. It was made using scrapy, but during development I looked at other scraping methods.<br> 
I took 2 e-commerce sites at random and chose a category to scrape.
After I created a custom spider for each site it was able to scrape trough the category and return the required data. No matter the page count. The output was csv, json or xml.<br>
Added scraping the details page of each item.
<h2>What I learned</h2>
<br> 1. Scraping basics and the tool comparison
<br> 2. Gained a deeper understanding of web site build elements an the ability to selec them using Xpath and css selectors.
<br> 3. Ability to navigate multiple pages of a site and scrape the content of each.
<br> 4. Designig the output files and structurung the data so it is easy to read/work with.
<br> 5. Exporting data to external files. In different formats

<h2>Usage</h2>
<br>Install python, VS code+extensions
<br>Clone the project
<br>Open folder in VS code
<br>Run command in terminal: 
<br><pre>
<br>pip install pipenv
<br>pipenv shell
<br>pipenv install
 </pre>
<br>This installs pipenv virtual enviroment. Activates it and install all modules I did use in this project.
<br>To run the scraping spiders cd into the comerc folder which contains the output files csv, json and the cfg file.
<br>In terminal type:
<br> <pre>pipenv run scrapy crawl ***  </pre><br(*** - substitute for a spider name without the .py at the end. Example xnet)
<br>This will only print the result to terminal. Better is to output it to a file.
<br> <pre>pipenv run scrapy crawl *** -o csv  </pre><br>(csv can change to json or xml)
<br>If spider doesn't run check you are in the right directory. 
<br>Type  <pre>ls </pre> in terminal - lists all files. Search if the cfg is in there.
<br> The project works without a virtal enviroment too.
<br><br>
<h2>Issues</h2>
<br>I had a proble on a new windows system while installing scrapy. 
<br>I needed to install Visual Studio(not VSCode!!!) to get some dependancies.
<br><br><br><br>
That's it no other issues
