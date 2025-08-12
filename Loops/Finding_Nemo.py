fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break


print("  visual break for a diff loop ")


#using a while loop

fish_list_counter = 0

while True:
     print(fish_list[fish_list_counter])
     if fish_list[fish_list_counter] == "Nemo":
         break
     fish_list_counter += 1
     
     
