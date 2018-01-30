from django.db import models

# Create your models here.

STATION = (  
    ('156', 'Clark St & Wellington Ave'),
    ('303', 'Broadway & Cornelia Ave'),
    ('295', 'Broadway & Argyle St'),
    ('419', 'Lake Park Ave & 53rd St'),
    ('191', 'Canal St & Monroe St (*)'),
    ('374', 'Western Ave & Walton St'),
    ('148', 'State St & 33rd St'),
    ('30', 'Ashland Ave & Augusta Blvd'),
    ('359', 'Larrabee St & Division St'),
    ('110', 'Dearborn St & Erie St'),
    ('98', 'LaSalle St & Washington St'),
    ('220', 'Hampden Ct & Diversey Pkwy'),
    ('87', 'Racine Ave & Fullerton Ave'),
    ('282', 'Halsted St & Maxwell St'),
    ('293', 'Broadway & Wilson Ave'),
    ('243', 'Lincoln Ave & Leavitt St'),
    ('364', 'Larrabee St & Oak St'),
    ('423', 'University Ave & 57th St'),
    ('120', 'Wentworth Ave & Archer Ave'),
    ('135', 'Halsted St & 21st St'),
    ('131', 'Lincoln Ave & Belmont Ave'),
    ('56', 'Desplaines St & Kinzie St'),
    ('118', 'Sedgwick St & North Ave'),
    ('57', 'Clinton St & Roosevelt Rd'),
    ('198', 'Green St & Madison St'),
    ('321', 'Wabash Ave & 8th St'),
    ('296', 'Broadway & Belmont Ave'),
    ('312', 'Clarendon Ave & Gordon Ter'),
    ('119', 'Ashland Ave & Lake St'),
    ('217', 'May St & Fulton St'),
    ('49', 'Dearborn St & Monroe St'),
    ('376', 'Artesian Ave & Hubbard St'),
    ('127', 'Lincoln Ave & Fullerton Ave'),
    ('133', 'Kingsbury St & Kinzie St'),
    ('458', 'Broadway & Thorndale Ave'),
    ('212', 'Orleans St & Ohio St'),
    ('181', 'LaSalle St & Illinois St'),
    ('190', 'Southport Ave & Wrightwood Ave'),
    ('465', 'Marine Dr & Ainslie St'),
    ('394', 'Clark St & 9th St (AMLI)'),
    ('144', 'Larrabee St & Webster Ave'),
    ('92', 'Carpenter St & Huron St'),
    ('96', 'Desplaines St & Randolph St'),
    ('43', 'Michigan Ave & Washington St'),
    ('350', 'Ashland Ave & Chicago Ave'),
    ('337', 'Clark St & Chicago Ave'),
    ('382', 'Western Ave & Congress Pkwy'),
    ('21', 'Aberdeen St & Jackson Blvd'),
    ('31', 'Franklin St & Chicago Ave'),
    ('242', 'Damen Ave & Leland Ave'),
    ('245', 'Clarendon Ave & Junior Ter'),
    ('192', 'Canal St & Adams St'),
    ('322', 'Kimbark Ave & 53rd St'),
    ('254', 'Pine Grove Ave & Irving Park Rd'),
    ('174', 'Canal St & Madison St'),
    ('71', 'Morgan St & Lake St'),
    ('80', 'Aberdeen St & Monroe St'),
    ('153', 'Southport Ave & Wellington Ave'),
    ('349', 'Halsted St & Wrightwood Ave'),
    ('46', 'Wells St & Walton St'),
    ('152', 'Lincoln Ave & Diversey Pkwy'),
    ('171', 'May St & Cullerton St'),
    ('106', 'State St & Pearson St'),
    ('74', 'Kingsbury St & Erie St'),
    ('68', 'Clinton St & Tilden St'),
    ('290', 'Kedzie Ave & Palmer Ct'),
    ('52', 'Michigan Ave & Lake St'),
    ('214', 'Damen Ave & Grand Ave'),
    ('16', 'Paulina Ave & North Ave'),
    ('114', 'Sheffield Ave & Addison St'),
    ('134', 'Peoria St & Jackson Blvd'),
    ('478', 'Rockwell St & Eastwood Ave'),
    ('66', 'Clinton St & Lake St'),
    ('125', 'Rush St & Hubbard St'),
    ('137', 'Morgan Ave & 14th Pl'),
    ('291', 'Wells St & Evergreen Ave'),
    ('278', 'Wallace St & 35th St'),
    ('36', 'Franklin St & Jackson Blvd'),
    ('26', 'McClurg Ct & Illinois St'),
    ('227', 'Southport Ave & Waveland Ave'),
    ('89', 'Financial Pl & Congress Pkwy'),
    ('142', 'McClurg Ct & Erie St'),
    ('261', 'Hermitage Ave & Polk St'),
    ('460', 'Clark St & Bryn Mawr Ave'),
    ('33', 'State St & Van Buren St'),
    ('91', 'Clinton St & Washington Blvd'),
    ('283', 'LaSalle St & Jackson Blvd'),
    ('252', 'Greenwood Ave & 47th St'),
    ('186', 'Ogden Ave & Race Ave'),
    ('196', 'Cityfront Plaza Dr & Pioneer Ct'),
    ('141', 'Clark St & Lincoln Ave'),
    ('334', 'Lake Shore Dr & Belmont Ave'),
    ('166', 'Ashland Ave & Wrightwood Ave'),
    ('286', 'Franklin St & Quincy St'),
    ('308', 'Seeley Ave & Roscoe St'),
    ('128', 'Damen Ave & Chicago Ave'),
    ('77', 'Clinton St & Madison St'),
    ('50', 'Clark St & Congress Pkwy'),
    ('18', 'Wacker Dr & Washington St'),
    ('307', 'Southport Ave & Clybourn Ave'),
    ('325', 'Clark St & Winnemac Ave'),
    ('146', 'Loomis St & Jackson Blvd'),
    ('251', 'Clarendon Ave & Leland Ave'),
    ('492', 'Leavitt St & Addison St'),
    ('496', 'Avers Ave & Belmont Ave'),
    ('346', 'Ada St & Washington Blvd'),
    ('377', 'Kedzie Ave & Lake St'),
    ('163', 'Damen Ave & Clybourn Ave'),
    ('59', 'Wabash Ave & Roosevelt Rd'),
    ('347', 'Ashland Ave & Grace St'),
    ('111', 'Sedgwick St & Huron St'),
    ('340', 'Clark St & Wrightwood Ave'),
    ('143', 'Sedgwick St & Webster Ave'),
    ('75', 'Canal St & Jackson Blvd'),
    ('344', 'Ravenswood Ave & Lawrence Ave'),
    ('29', 'Noble St & Milwaukee Ave'),
    ('138', 'Clybourn Ave & Division St'),
    ('72', 'Wabash Ave & 16th St'),
    ('273', 'Michigan Ave & 18th St'),
    ('175', 'Wells St & Polk St'),
    ('123', 'California Ave & Milwaukee Ave'),
    ('48', 'Larrabee St & Kingsbury St'),
    ('183', 'Damen Ave & Augusta Blvd'),
    ('224', 'Halsted St & Willow St'),
    ('246', 'Ashland Ave & Belle Plaine Ave'),
    ('55', 'Halsted St & Roosevelt Rd'),
    ('99', 'Lake Shore Dr & Ohio St'),
    ('14', 'Morgan St & 18th St'),
    ('511', 'Albany Ave & Bloomingdale Ave'),
    ('86', 'Eckhart Park'),
    ('168', 'Michigan Ave & 14th St'),
    ('486', 'Oakley Ave & Irving Park Rd'),
    ('54', 'Ogden Ave & Chicago Ave'),
    ('284', 'Michigan Ave & Jackson Blvd'),
    ('327', 'Sheffield Ave & Webster Ave'),
    ('9', 'Leavitt St & Archer Ave'),
    ('67', 'Sheffield Ave & Fullerton Ave'),
    ('182', 'Wells St & Elm St'),
    ('195', 'Columbus Dr & Randolph St'),
    ('232', 'Pine Grove Ave & Waveland Ave'),
    ('255', 'Indiana Ave & Roosevelt Rd'),
    ('219', 'Damen Ave & Cortland St'),
    ('464', 'Damen Ave & Foster Ave'),
    ('319', 'Greenview Ave & Diversey Pkwy'),
    ('165', 'Clark St & Grace St'),
    ('311', 'Leavitt St & Lawrence Ave'),
    ('53', 'Wells St & Huron St'),
    ('426', 'Ellis Ave & 60th St'),
    ('107', 'Desplaines St & Jackson Blvd'),
    ('188', 'Greenview Ave & Fullerton Ave'),
    ('100', 'Orleans St & Merchandise Mart Plaza'),
    ('7', 'Field Blvd & South Water St'),
    ('230', 'Lincoln Ave & Roscoe St'),
    ('61', 'Wood St & Milwaukee Ave'),
    ('259', 'California Ave & Francis Pl'),
    ('264', 'Stetson Ave & South Water St'),
    ('45', 'Michigan Ave & Congress Pkwy'),
    ('292', 'Southport Ave & Clark St'),
    ('233', 'Sangamon St & Washington Blvd (*)'),
    ('69', 'Damen Ave & Pierce Ave'),
    ('47', 'State St & Kinzie St'),
    ('226', 'Racine Ave & Belmont Ave'),
    ('330', 'Lincoln Ave & Addison St'),
    ('199', 'Wabash Ave & Grand Ave'),
    ('289', 'Wells St & Concord Ln'),
    ('413', 'Woodlawn Ave & Lake Park Ave'),
    ('157', 'Lake Shore Dr & Wellington Ave'),
    ('161', 'Rush St & Superior St'),
    ('301', 'Clark St & Schiller St'),
    ('418', 'Ellis Ave & 53rd St'),
    ('342', 'Wolcott Ave & Polk St'),
    ('306', 'Sheridan Rd & Buena Ave'),
    ('211', 'St. Clair St & Erie St'),
    ('24', 'Fairbanks Ct & Grand Ave'),
    ('130', 'Damen Ave & Division St'),
    ('302', 'Sheffield Ave & Wrightwood Ave'),
    ('241', 'Morgan St & Polk St'),
    ('331', 'Halsted St & Blackhawk St (*)'),
    ('231', 'Sheridan Rd & Montrose Ave'),
    ('260', 'Kedzie Ave & Milwaukee Ave'),
    ('201', 'Indiana Ave & 40th St'),
    ('40', 'LaSalle St & Adams St'),
    ('154', 'Southport Ave & Belmont Ave'),
    ('276', 'California Ave & North Ave'),
    ('225', 'Halsted St & Dickens Ave'),
    ('88', 'May St & Randolph St'),
    ('81', 'Daley Center Plaza'),
    ('38', 'Clark St & Lake St'),
    ('116', 'Western Ave & Winnebago Ave'),
    ('93', 'Sheffield Ave & Willow St'),
    ('345', 'Lake Park Ave & 56th St'),
    ('28', 'Larrabee St & Menomonee St'),
    ('320', 'Loomis St & Lexington St'),
    ('44', 'State St & Randolph St'),
    ('94', 'Clark St & Armitage Ave'),
    ('5', 'State St & Harrison St'),
    ('41', 'Federal St & Polk St'),
    ('73', 'Jefferson St & Monroe St'),
    ('300', 'Broadway & Barry Ave'),
    ('177', 'Theater on the Lake'),
    ('149', 'Calumet Ave & 33rd St'),
    ('305', 'Western Ave & Division St'),
    ('468', 'Budlong Woods Library'),
    ('338', 'Calumet Ave & 18th St'),
    ('333', 'Ashland Ave & Blackhawk St'),
    ('140', 'Dearborn Pkwy & Delaware Pl'),
    ('238', 'Ravenswood Ave & Montrose Ave (*)'),
    ('288', 'Larrabee St & Armitage Ave'),
    ('176', 'Clark St & Elm St'),
    ('223', 'Clifton Ave & Armitage Ave'),
    ('13', 'Wilton Ave & Diversey Pkwy'),
    ('462', 'Ravenswood Ave & Balmoral Ave'),
    ('343', 'Racine Ave & Wrightwood Ave'),
    ('304', 'Broadway & Waveland Ave'),
    ('479', 'Drake Ave & Montrose Ave'),
    ('159', 'Claremont Ave & Hirsch St'),
    ('494', 'Kedzie Ave & Bryn Mawr Ave'),
    ('285', 'Wood St & Grand Ave'),
    ('178', 'State St & 19th St'),
    ('365', 'Halsted St & North Branch St'),
    ('500', 'Central Park Ave & Elbridge Ave'),
    ('366', 'Loomis St & Archer Ave'),
    ('213', 'Leavitt St & North Ave'),
    ('129', 'Blue Island Ave & 18th St'),
    ('23', 'Orleans St & Elm St (*)'),
    ('471', 'Francisco Ave & Foster Ave'),
    ('287', 'Franklin St & Monroe St'),
    ('268', 'Lake Shore Dr & North Blvd'),
    ('27', 'Larrabee St & North Ave'),
    ('108', 'Halsted St & Polk St'),
    ('158', 'Milwaukee Ave & Wabansia Ave'),
    ('299', 'Halsted St & Roscoe St'),
    ('313', 'Lakeview Ave & Fullerton Pkwy'),
    ('58', 'Marshfield Ave & Cortland St'),
    ('401', 'Shields Ave & 28th Pl'),
    ('205', 'Paulina St & 18th St'),
    ('25', 'Michigan Ave & Pearson St'),
    ('170', 'Clinton St & 18th St'),
    ('173', 'Mies van der Rohe Way & Chicago Ave'),
    ('339', 'Emerald Ave & 31st St'),
    ('329', 'Lake Shore Dr & Diversey Pkwy'),
    ('35', 'Streeter Dr & Grand Ave'),
    ('403', 'Wentworth Ave & 33rd St'),
    ('202', 'Halsted St & 18th St'),
    ('112', 'Green St & Randolph St'),
    ('463', 'Clark St & Berwyn Ave'),
    ('172', 'Rush St & Cedar St'),
    ('247', 'Shore Dr & 55th St'),
    ('476', 'Kedzie Ave & Leland Ave'),
    ('256', 'Broadway & Sheridan Rd'),
    ('126', 'Clark St & North Ave'),
    ('507', 'Humboldt Blvd & Armitage Ave'),
    ('164', 'Franklin St & Lake St'),
    ('309', 'Leavitt St & Armitage Ave'),
    ('274', 'Racine Ave & 15th St'),
    ('229', 'Southport Ave & Roscoe St'),
    ('39', 'Wabash Ave & Adams St'),
    ('314', 'Ravenswood Ave & Berteau Ave'),
    ('318', 'Southport Ave & Irving Park Rd'),
    ('411', 'Halsted St & 47th Pl'),
    ('420', 'Ellis Ave & 55th St'),
    ('272', 'Indiana Ave & 31st St'),
    ('275', 'Ashland Ave & 13th St'),
    ('204', 'Prairie Ave & Garfield Blvd'),
    ('84', 'Union Ave & Grand Ave'),
    ('210', 'Ashland Ave & Division St'),
    ('132', 'Wentworth Ave & 24th St'),
    ('37', 'Dearborn St & Adams St'),
    ('109', '900 W Harrison St'),
    ('475', 'Washtenaw Ave & Lawrence Ave'),
    ('169', 'Canal St & Harrison St'),
    ('236', 'Sedgwick St & Schiller St'),
    ('147', 'Indiana Ave & 26th St'),
    ('298', 'Lincoln Ave & Belle Plaine Ave'),
    ('234', 'Clark St & Montrose Ave'),
    ('493', 'Western Ave & Roscoe St'),
    ('209', 'Normal Ave & Archer Ave'),
    ('32', 'Racine Ave & Congress Pkwy'),
    ('17', 'Wood St & Division St'),
    ('15', 'Racine Ave & 18th St'),
    ('461', 'Broadway & Ridge Ave'),
    ('417', 'Cornell Ave & Hyde Park Blvd'),
    ('323', 'Sheridan Rd & Lawrence Ave'),
    ('498', 'California Ave & Fletcher St'),
    ('385', 'Princeton Ave & Garfield Blvd'),
    ('316', 'Damen Ave & Sunnyside Ave'),
    ('85', 'Michigan Ave & Oak St'),
    ('200', 'MLK Jr Dr & 47th St'),
    ('324', 'Stockton Dr & Wrightwood Ave'),
    ('414', 'Canal St & Taylor St'),
    ('457', 'Clark St & Elmdale Ave'),
    ('248', 'Woodlawn Ave & 55th St'),
    ('265', 'Cottage Grove Ave & Oakwood Blvd'),
    ('145', 'Mies van der Rohe Way & Chestnut St'),
    ('76', 'Lake Shore Dr & Monroe St'),
    ('326', 'Clark St & Leland Ave'),
    ('504', 'Campbell Ave & Fullerton Ave'),
    ('194', 'Wabash Ave & Wacker Pl'),
    ('370', 'Calumet Ave & 21st St'),
    ('117', 'Wilton Ave & Belmont Ave'),
    ('60', 'Dayton St & North Ave'),
    ('383', 'Ashland Ave & Harrison St'),
    ('122', 'Ogden Ave & Congress Pkwy'),
    ('449', 'Clark St & Columbia Ave'),
    ('258', 'Logan Blvd & Elston Ave'),
    ('425', 'Harper Ave & 59th St'),
    ('510', 'Spaulding Ave & Division St'),
    ('336', 'Cottage Grove Ave & 47th St'),
    ('160', 'Campbell Ave & North Ave'),
    ('3', 'Shedd Aquarium'),
    ('20', 'Sheffield Ave & Kingsbury St'),
    ('452', 'Western Ave & Granville Ave'),
    ('470', 'Kedzie Ave & Foster Ave'),
    ('279', 'Halsted St & 35th St (*)'),
    ('262', 'Halsted St & 37th St'),
    ('402', 'Shields Ave & 31st St'),
    ('19', 'Loomis St & Taylor St (*)'),
    ('51', 'Clark St & Randolph St'),
    ('22', 'May St & Taylor St'),
    ('502', 'California Ave & Altgeld St'),
    ('222', 'Milwaukee Ave & Rockwell St'),
    ('62', 'McCormick Place'),
    ('240', 'Sheridan Rd & Irving Park Rd'),
    ('328', 'Ellis Ave & 58th St'),
    ('228', 'Damen Ave & Melrose Ave'),
    ('206', 'Halsted St & Archer Ave'),
    ('277', 'Ashland Ave & Grand Ave'),
    ('341', 'Adler Planetarium'),
    ('482', 'Campbell Ave & Montrose Ave'),
    ('115', 'Sheffield Ave & Wellington Ave'),
    ('180', 'Ritchie Ct & Banks St'),
    ('439', 'Kedzie Ave & 21st St'),
    ('281', 'Western Ave & 24th St'),
    ('121', 'Blackstone Ave & Hyde Park Blvd'),
    ('501', 'Richmond St & Diversey Ave'),
    ('280', 'Morgan St & 31st St'),
    ('434', 'Ogden Ave & Roosevelt Rd'),
    ('34', 'Cannon Dr & Fullerton Ave'),
    ('317', 'Wood St & Taylor St'),
    ('348', 'California Ave & 21st St'),
    ('459', 'Lakefront Trail & Bryn Mawr Ave'),
    ('6', 'Dusable Harbor'),
    ('197', 'Michigan Ave & Madison St'),
    ('113', 'Bissell St & Armitage Ave'),
    ('442', 'California Ave & 23rd Pl'),
    ('90', 'Millennium Park'),
    ('97', 'Museum Campus'),
    ('445', 'California Ave & 26th St'),
    ('244', 'Ravenswood Ave & Irving Park Rd'),
    ('250', 'Ashland Ave & Wellington Ave'),
    ('239', 'Western Ave & Leland Ave'),
    ('416', 'Dorchester Ave & 49th St'),
    ('472', 'Lincoln Ave & Winona St'),
    ('179', 'MLK Jr Dr & Oakwood Blvd'),
    ('436', 'Fairfield Ave & Roosevelt Rd'),
    ('410', 'Prairie Ave & 43rd St'),
    ('495', 'Keystone Ave & Montrose Ave'),
    ('257', 'Lincoln Ave & Waveland Ave'),
    ('505', 'Winchester Ave & Elston Ave'),
    ('388', 'Halsted St & 63rd St'),
    ('424', 'Museum of Science and Industry'),
    ('381', 'Western Ave & Monroe St'),
    ('509', 'Troy St & North Ave'),
    ('399', 'South Shore Dr & 74th St'),
    ('4', 'Burnham Harbor'),
    ('454', 'Broadway & Granville Ave'),
    ('432', 'Clark St & Lunt Ave'),
    ('249', 'Montrose Harbor'),
    ('294', 'Broadway & Berwyn Ave'),
    ('489', 'Drake Ave & Addison St'),
    ('136', 'Racine Ave & 13th St'),
    ('297', 'Paulina St & Montrose Ave'),
    ('491', 'Talman Ave & Addison St'),
    ('474', 'Christiana Ave & Lawrence Ave'),
    ('184', 'State St & 35th St'),
    ('203', 'Western Ave & 21st St'),
    ('421', 'MLK Jr Dr & 56th St (*)'),
    ('315', 'Elston Ave & Wabansia Ave'),
    ('453', 'Clark St & Schreiber Ave'),
    ('162', 'Damen Ave & Wellington Ave'),
    ('310', 'Damen Ave & Charleston St'),
    ('263', 'Rhodes Ave & 32nd St'),
    ('438', 'Central Park Ave & Ogden Ave'),
    ('447', 'Glenwood Ave & Morse Ave'),
    ('469', 'St. Louis Ave & Balmoral Ave'),
    ('451', 'Sheridan Rd & Loyola Ave'),
    ('253', 'Clifton Ave & Lawrence Ave'),
    ('437', 'Washtenaw Ave & 15th St (*)'),
    ('185', 'Stave St & Armitage Ave'),
    ('103', 'Clinton St & Polk St (*)'),
    ('124', 'Damen Ave & Cullerton St'),
    ('42', 'Wabash Ave & Cermak Rd'),
    ('499', 'Kosciuszko Park'),
    ('487', 'California Ave & Byron St'),
    ('477', 'Manor Ave & Leland Ave'),
    ('207', 'Emerald Ave & 28th St'),
    ('497', 'Kimball Ave & Belmont Ave'),
    ('490', 'Troy St & Elston Ave'),
    ('95', 'Stony Island Ave & 64th St'),
    ('237', 'MLK Jr Dr & 29th St'),
    ('354', 'Sheridan Rd & Greenleaf Ave'),
    ('484', 'Monticello Ave & Irving Park Rd'),
    ('215', 'Damen Ave & Madison St'),
    ('267', 'Lake Park Ave & 47th St'),
    ('415', 'Calumet Ave & 51st St'),
    ('427', 'Cottage Grove Ave & 63rd St'),
    ('373', 'Kedzie Ave & Chicago Ave'),
    ('367', 'Racine Ave & 35th St'),
    ('368', 'Ashland Ave & Archer Ave'),
    ('412', 'Princeton Ave & 47th St'),
    ('271', 'Cottage Grove Ave & 43rd St'),
    ('435', 'Kedzie Ave & Roosevelt Rd'),
    ('216', 'California Ave & Division St'),
    ('480', 'Kedzie Ave & Montrose Ave'),
    ('150', 'Fort Dearborn Dr & 31st St'),
    ('503', 'Drake Ave & Fullerton Ave'),
    ('506', 'Spaulding Ave & Armitage Ave'),
    ('481', 'California Ave & Montrose Ave'),
    ('351', 'Cottage Grove Ave & 51st St'),
    ('422', 'DuSable Museum'),
    ('433', 'Kedzie Ave & Harrison St'),
    ('352', 'Jeffery Blvd & 67th St'),
    ('375', 'Sacramento Blvd & Franklin Blvd'),
    ('102', 'Stony Island Ave & 67th St'),
    ('2', 'Michigan Ave & Balbo Ave'),
    ('193', 'State St & 29th St'),
    ('467', 'Western Ave & Lunt Ave'),
    ('428', 'Dorchester Ave & 63rd St'),
    ('218', 'Wells St & 19th St'),
    ('372', 'Humboldt Dr & Luis Munoz Marin Dr'),
    ('485', 'Sawyer Ave & Irving Park Rd'),
    ('429', 'Cottage Grove Ave & 67th St'),
    ('378', 'California Ave & Lake St'),
    ('450', 'Warren Park West'),
    ('466', 'Ridge Blvd & Touhy Ave'),
    ('353', 'Clark St & Touhy Ave'),
    ('208', 'Ashland Ave & 21st St'),
    ('409', 'Shields Ave & 43rd St'),
    ('406', 'Lake Park Ave & 35th St'),
    ('335', 'Calumet Ave & 35th St'),
    ('390', 'Wentworth Ave & 63rd St'),
    ('456', '2112 W Peterson Ave'),
    ('483', 'Keeler Ave & Irving Park Rd'),
    ('369', 'Wood St & 35th St'),
    ('448', 'Warren Park East'),
    ('446', 'Western Ave & 28th St'),
    ('167', 'Damen Ave & Coulter St'),
    ('356', 'Stony Island Ave & 71st St'),
    ('508', 'Central Park Ave & North Ave'),
    ('400', 'Cottage Grove Ave & 71st St'),
    ('355', 'South Shore Dr & 67th St'),
    ('396', 'Yates Blvd & 75th St'),
    ('408', 'Union Ave & 42nd St'),
    ('455', 'Maplewood Ave & Peterson Ave'),
    ('12', 'South Shore Dr & 71st St'),
    ('441', 'Kedzie Ave & 24th St'),
    ('393', 'Calumet Ave & 71st St'),
    ('11', 'Jeffery Blvd & 71st St'),
    ('430', 'MLK Jr Dr & 63rd St'),
    ('101', '63rd St Beach'),
    ('307', 'Southport Ave & Clybourn Ave'),
    ('431', 'Eberhart Ave & 61st St'),
    ('392', 'Perry Ave & 69th St'),
    ('443', 'Millard Ave & 26th St'),
    ('391', 'Halsted St & 69th St'),
    ('488', 'Pulaski Rd & Eddy St'),
    ('190', 'Southport Ave & Wrightwood Ave'),
    ('270', 'Stony Island Ave & 75th St'),
    ('407', 'State St & Pershing Rd'),
    ('444', 'Albany Ave & 26th St'),
    ('395', 'Jeffery Blvd & 76th St'),
    ('397', 'Saginaw Ave & Exchange Ave'),
    ('398', 'Rainbow Beach'),
    ('440', 'Lawndale Ave & 23rd St'),
    ('384', 'Halsted St & 51st St'),
    ('20', 'Sheffield Ave & Kingsbury St'),
    ('332', 'Halsted St & Diversey Pkwy'),
    ('114', 'Sheffield Ave & Addison St'),
    ('81', 'Daley Center Plaza'),
    ('386', 'Halsted St & 56th St'),
    ('518', 'Conservatory Dr & Lake St'),
    ('537', 'Kenton Ave & Madison St'),
    ('532', 'Austin Blvd & Lake St'),
    ('540', 'Laramie Ave & Madison St'),
    ('533', 'Central Park Blvd & 5th Ave'),
    ('536', 'Kostner Ave & Lake St'),
    ('534', 'Pulaski Rd & Madison St'),
    ('530', 'Laramie Ave & Kinzie St'),
    ('545', 'Kostner Ave & Adams St'),
    ('541', 'Central Ave & Harrison St'),
    ('528', 'Pulaski Rd & Lake St'),
    ('544', 'Mason Ave & Madison St'),
    ('546', 'Damen Ave & Pershing Rd'),
    ('529', 'Cicero Ave & Lake St'),
    ('547', 'Ashland Ave & Pershing Rd'),
    ('535', 'Pulaski Rd & Congress Pkwy'),
    ('594', 'Western Blvd & 48th Pl'),
    ('551', 'Hoyne Ave & 47th St'),
    ('552', 'Ashland Ave & McDowell Ave'),
    ('548', 'Morgan St & Pershing Rd'),
    ('542', 'Central Ave & Madison St'),
    ('554', 'Damen Ave & 51st St'),
    ('572', 'State St & 76th St'),
    ('568', 'Normal Ave & 72nd St'),
    ('553', 'Elizabeth St & 47th St'),
    ('618', 'Lombard Ave & Garfield St'),
    ('616', 'Oak Park Ave & Harrison St'),
    ('561', 'Damen Ave & 61st St'),
    ('560', 'Marshfield Ave & 59th St'),
    ('539', 'Cicero Ave & Quincy St'),
    ('615', 'Lombard Ave & Madison St'),
    ('538', 'Cicero Ave & Flournoy St'),
    ('613', 'Wisconsin Ave & Madison St'),
    ('565', 'Ashland Ave & 66th St'),
    ('614', 'East Ave & Madison St'),
    ('617', 'East Ave & Garfield St'),
    ('597', 'Chicago Ave & Washington St'),
    ('600', 'Dodge Ave & Church St'),
    ('596', 'Benson Ave & Church St'),
    ('601', 'Central St Metra'),
    ('563', 'Ashland Ave & 63rd St'),
    ('610', 'Marion St & South Blvd'),
    ('611', 'Oak Park Ave & South Blvd'),
    ('609', 'Forest Ave & Lake St'),

   )

STATION_DICT = dict(STATION)

class Input(models.Model):

    station = models.CharField(max_length=50, choices=STATION)
    name  = models.CharField(max_length=50)
