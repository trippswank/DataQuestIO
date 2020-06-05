## 1. Lists ##

row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]

total = ratings_1 + ratings_2 + ratings_3

average = total/3



## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]


rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]

total_rating = rating_1 + rating_2 + rating_3

average_rating = total_rating/3


## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
pandora_rating_data = [row_5[0], row_5[3], row_5[-1]]


avg_rating = (fb_rating_data[-1] + insta_rating_data[-1] + pandora_rating_data[-1]) / 3


## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

first_4_fb = row_1[0:4]

last_3_fb = row_1[2:5]

pandora_3_4 = row_5[2:4]

## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]


app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = ((app_data_set[0][-1]) + (app_data_set[1][-1]) + (app_data_set[2][-1]) + (app_data_set[3][-1]) + (app_data_set[4][-1])) / 5







## 7. Opening and Reading a File ##

opened_file = open('AppleStore.csv')

read_file = opened_file.read()
read_file[:300]
print(read_file[:300])

opened_file.close()

## 8. From Strings to Lists ##

new_line_split = read_file.split("\n")

row_1_list = new_line_split[0].split(",")
row_2_list = new_line_split[1].split(",")
row_3_list = new_line_split[2].split(",")

first_three_lists = [row_1_list, row_2_list, row_3_list]



## 9. For Loops ##

#Use a for loop to modify first_three so that its elements are the first three rows (in order) split on the comma character.

header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]
first_three = [header, data_row_1, data_row_2]

index=0
for each_string in first_three:
    first_three[index] = each_string.split(",")
    print(first_three[index])
    index += 1
   
print(first_three)


## 10. Reading CSV files ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)

apps_data = list(read_file)

opened_file.close()

print(len(apps_data))

print(apps_data[:1])

print(apps_data[2][3])


