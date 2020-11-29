# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:
def converter_function(lists):
    i=0
    for item in lists:
        if 'M' in item:
            item = float(item[:-1])*1000000
            lists[i]=item            
        elif 'B' in item:
            item = float(item[:-1])*1000000000
            lists[i]=item
        i+=1
    return lists
new_damages = converter_function(damages)

# write your construct hurricane dictionary function here:
def dict_maker(nam,mos,yrs,msw,aaf,dam,dth):
    total = len(nam)
    i = 0
    hur_dict = {}
    while i < total:
        hur_dict[nam[i]] = {"Names":nam[i],'Months':mos[i],'Years':yrs[i],'Max Sustained Winds':msw[i],'Areas Affected':aaf[i],'Damage':dam[i],'Death':dth[i]}
        i+=1
    return(hur_dict)
hurricane_dict = dict_maker(names, months,years, max_sustained_winds,areas_affected,new_damages,deaths)
#print(hurricane_dict['Michael']['Death'])

# write your construct hurricane by year dictionary function here:
def dict_by_year(data,yrs):
    #total = len(data)
    yrs_dict = {}
    hur_data = []
    for value in data.values():
        hur_data.append(value)
    i=0
    for item in yrs:
        current_cane = [hur_data[i-1]]
        #print(current_cane)
        if item in yrs_dict:
            current_cane.append(hur_data[i])
            yrs_dict[item] = current_cane
        else:
            yrs_dict[item] = hur_data[i]
        i+=1
    return yrs_dict

year_dictionary = dict_by_year(hurricane_dict,years)
#print(year_dictionary[1932])


# write your count affected areas function here:
def area_count(aff):
    areas = []
    count = []
    area_dict = {}
    for item1 in areas_affected:
        for item2 in item1:
            areas.append(item2)
    i=0
    for ar in areas:
        if ar in area_dict:
            area_dict[ar] = area_dict[ar] +1
        else:
            area_dict[ar] = 1
        i+=1
    return area_dict

counting = area_count(areas_affected)
#print(counting['Mexico'])

# write your find most affected area function here:
def most_affected(areas):
    most_area = 12
    counts = 0
    for key in areas.keys():
        if areas[key] > counts:
            most_area = key
            counts = areas[key]
    return most_area, counts

most_affected_area = most_affected(counting)
#print(most_affected_area)

# write your greatest number of deaths function here:
def most_deaths_func(dictio):
    death_count = 0
    death_area = 0
    for key in dictio.keys():
        if dictio[key]['Death'] > death_count:
            death_count = dictio[key]['Death']
            death_area = key
        
    return death_area,death_count

most_death = most_deaths_func(hurricane_dict)
#print(most_death)

# write your catgeorize by mortality function here:

def hurr_scale_func(dictio):
    scale = [0,1,2,3,4]
    scale_dict = {}
    hur_scale_0 = []
    scale_0_death = []
    hur_scale_1 = []
    scale_1_death = []
    hur_scale_2 = []
    scale_2_death =[]
    hur_scale_3 = []
    scale_3_death=[]
    hur_scale_4 = []
    scale_4_death=[]
    for key in dictio.keys():
        death_count = dictio[key]['Death']
        #print(dictio[key])
        #print(death_count)
        if death_count == 0:
            hur_scale_0.append([dictio[key]])
            scale_0_death.append(death_count)
        elif death_count > 0 and death_count <= 100:
            hur_scale_1.append([dictio[key]])
            scale_1_death.append(death_count)
        elif death_count > 100 and death_count <= 500:
            hur_scale_2.append([dictio[key]])
            scale_2_death.append(death_count)
        elif death_count > 500 and death_count <= 1000:
            hur_scale_3.append([dictio[key]])
            scale_3_death.append(death_count)
        else :
            hur_scale_4.append([dictio[key]])
            scale_4_death.append(death_count) 
    #print(hur_scale_0,scale_0_death)
    all_scale = [hur_scale_0, hur_scale_1,hur_scale_2,hur_scale_3,hur_scale_4]
    i=0
    for item in scale:
        scale_dict[item] = all_scale[i]
        i+=1

    return scale_dict

dict_by_scale = hurr_scale_func(hurricane_dict)   

#print(dict_by_scale[1])

# write your greatest damage function here:
def most_damage_func(dictio):
    damage_cost = 0
    damaged_area = 0
    for key in dictio.keys():
        aspect = dictio[key]['Damage']
        if aspect == 'Damages not recorded':
            continue
        elif aspect > damage_cost:
            damage_cost = dictio[key]['Damage']
            damaged_area = key
        
    return damaged_area,damage_cost

most_damaged = most_damage_func(hurricane_dict)
print(most_damaged)





# write your catgeorize by damage function here:

def dam_scale_func(dictio):
    dam_scale = [0,1,2,3,4]
    dam_scale_dict = {}
    dam_scale_0 = []
    dam_scale_1 = []
    dam_scale_2 = []
    dam_scale_3 = []
    dam_scale_4 = []
    for key in dictio.keys():
        damage_count = dictio[key]['Death']
        if damage_count == 0:
            dam_scale_0.append([dictio[key]])
        elif damage_count > 0 and damage_count <= 100000000:
            dam_scale_1.append([dictio[key]])
        elif damage_count > 100000000 and damage_count <= 1000000000:
            dam_scale_2.append([dictio[key]])
        elif damage_count > 1000000000 and damage_count <= 10000000000:
            dam_scale_3.append([dictio[key]])
        else :
            dam_scale_4.append([dictio[key]])
    all_scale = [dam_scale_0, dam_scale_1,dam_scale_2,dam_scale_3,dam_scale_4]
    i=0
    for item in dam_scale:
        dam_scale_dict[item] = all_scale[i]
        i+=1
    return dam_scale_dict

dict_by_dam_scale = dam_scale_func(hurricane_dict)
print(dict_by_dam_scale)



