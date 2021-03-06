# First run: python manage.py migrate
# This initializes the schema according to the model in the 'scrape' app

import MySQLdb

db = MySQLdb.connect("localhost", "root", "mypass", "baseball_py")
cursor = db.cursor()

cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('1', 'Yoenis Cespedes', '13110')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('2', 'Alex Rodriguez', '1274')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('3', 'Shin-Soo Choo', '3174')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('4', 'Albert Pujols', '1177')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('5', 'Robinson Cano', '3269')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('6', 'Joey Votto', '4314')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('7', 'Prince Fielder', '4613')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('8', 'Derek Jeter', '826')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('9', 'Joe Mauer', '1857')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('10', 'Mark Teixeira', '1281')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('11', 'Buster Posey', '9166')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('12', 'Matt Kemp', '5631')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('13', 'Troy Tulowitzki', '3531')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('14', 'Adrian Gonzalez', '1908')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('15', 'Miguel Cabrera', '1744')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('16', 'Jacoby Ellsbury', '4727')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('17', 'Carl Crawford', '1201')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('18', 'David Wright', '3787')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('19', 'Alfonso Soriano', '847')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('20', 'Vernon Wells', '1326')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('21', 'Jayson Werth', '1327')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('22', 'Ryan Zimmerman', '4220')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('23', 'Josh Hamilton', '1875')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('24', 'Ryan Howard', '2154')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('25', 'Jason Giambi', '818')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('26', 'Matt Holliday', '1873')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('27', 'Elvis Andrus', '8709')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('28', 'Carlos Beltran', '589')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('29', 'David Ortiz', '745')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('30', 'Dustin Pedroia', '8370')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('31', 'Jose Reyes', '1736')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('32', 'Ryan Braun', '3410')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('33', 'Evan Longoria', '9368')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('34', 'Carlos Lee', '243')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('35', 'Andre Ethier', '6265')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('36', 'Hanley Ramirez', '8001')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('37', 'Mike Trout', '10155')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('38', 'Andrew McCutchen', '9847')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('39', 'Josh Donaldson', '5038')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('40', 'Paul Goldschmidt', '9218')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('41', 'Yasiel Puig', '14225')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('42', 'Chris Davis', '9272')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('43', 'B.J. Upton', '5015')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('44', 'Justin Upton', '5222')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('45', 'Ichiro Suzuki', '1101')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('46', 'Adrian Beltre', '639')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('47', 'Justin Morneau', '1737')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('48', 'Jimmy Rollins', '971')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('49', 'Chase Utley', '1679')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('50', 'Hunter Pence', '8252')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('51', 'Carlos Gonzalez', '7287')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('52', 'Carlos Gomez', '4881')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('53', 'Giancarlo Stanton', '4949')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('54', 'Edwin Encarnacion', '2151')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('55', 'Jay Bruce', '9892')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('56', 'Nelson Cruz', '2434')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('57', 'Jose Bautista', '1887')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('58', 'Curtis Granderson', '4747')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('59', 'Yadier Molina', '7007')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('60', 'Adam Dunn', '319')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('61', 'Mark Reynolds', '7619')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('62', 'Freddie Freeman', '5361')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('63', 'Jason Heyward', '4940')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('64', 'Brian McCann', '4810')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('65', 'Bryce Harper', '11579')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('66', 'Brandon Phillips', '791')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('67', 'Chase Headley', '4720')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('68', 'Pablo Sandoval', '5409')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('69', 'Coco Crisp', '1572')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('70', 'Ian Kinsler', '6195')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('71', 'Jonny Gomes', '1845')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('72', 'Mike Napoli', '3057')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('73', 'Shane Victorino', '1677')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('74', 'Wil Myers', '10047')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('75', 'Ben Zobrist', '7435')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('76', 'James Loney', '4556')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('77', 'Adam Jones', '6368')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('78', 'Nick Markakis', '5930')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('79', 'J.J. Hardy', '3797')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('80', 'Manny Machado', '11493')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('81', 'Matt Wieters', '4298')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('82', 'Melky Cabrera', '4022')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('83', 'Austin Jackson', '9848')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('84', 'Torii Hunter', '731')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('85', 'Jose Iglesias', '10231')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('86', 'Victor Martinez', '393')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('87', 'Billy Butler', '7399')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('88', 'Eric Hosmer', '3516')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('89', 'Yan Gomes', '9627')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('90', 'Michael Brantley', '4106')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('91', 'David Murphey', '6035')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('92', 'Jason Kipnis', '9776')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('93', 'Carlos Santana', '2396')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('94', 'Josh Willingham', '2103')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('95', 'Brian Dozier', '9810')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('96', 'Adam Eaton', '11205')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('97', 'Jose Abreu', '15676')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('98', 'Avisail Garcia', '5760')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('99', 'Gordon Beckham', '9015')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('100', 'Dayan Viciedo', '3917')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('101', 'Alex Rios', '2090')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('102', 'Josh Reddick', '3892')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('103', 'Brandon Moss', '4467')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('104', 'Jed Lowrie', '4418')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('105', 'Derek Norris', '6867')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('106', 'Mike Zunino', '13265')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('107', 'Jose Altuve', '5417')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('108', 'Dan Uggla', '3442')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('109', 'Andrelton Simmons', '10847')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('110', 'Travis D%27Arnaud', '7739')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('111', 'Garrett Jones', '2714')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('112', 'Christian Yelich', '11477')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('113', 'Marlon Byrd', '950')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('114', 'Jhonny Peralta', '1738')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('115', 'Starling Marte', '9241')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('116', 'Pedro Alvarez', '2495')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('117', 'Anthony Rizzo', '3473')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('118', 'Jean Segura', '5933')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('119', 'Rickie Weeks', '1849')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('120', 'Scooter Gennett', '10339')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('121', 'Aramis Ramirez', '1002')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('122', 'Juan Uribe', '454')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('123', 'Michael Morse', '3035')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('124', 'Angel Pagan', '2918')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('125', 'Brandon Belt', '10264')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('126', 'Carlos Quentin', '6274')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('127', 'Jedd Gyorko', '10816')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('128', 'Drew Stubbs', '9328')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('129', 'Nolan Arenado', '9777')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('130', 'Mark Trumbo', '6876')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('131', 'Martin Prado', '3312')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('132', 'Brett Gardner', '9927')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('133', 'Brett Gardner', '9927')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('134', 'Yangervis Solarte', '5352')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('135', 'Seth Smith', '7331')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('136', 'Charlie Blackmon', '7859')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('137', 'Jonathan Lucroy', '7870')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('138', 'Casey McGehee', '6086')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('139', 'Anthony Rendon', '6086')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('140', 'Nick Swisher', '4599')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('141', 'Alcides Escobar', '6310')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('142', 'Alex Gordon', '5209')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('143', 'Kris Davis', '9112')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('144', 'J.D. Martinez', '6184')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('145', 'Rajai Davis', '3708')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('146', 'John Jaso', '5887')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('147', 'Stephen Vogt', '5000')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('148', 'Alberto Callaspo', '3336')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('149', 'Eric Sogard', '7927')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('150', 'Nick Punto', '1429')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('151', 'Craig Gentry', '9571')")
cursor.execute("INSERT INTO scrape_player (ID, NAME, NUMBER) VALUES('152', 'Sam Fuld', '8254')")

db.commit()
db.close()

