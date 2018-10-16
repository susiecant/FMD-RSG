equipment_list = Alldata.equipment;
shares_water_list = Alldata.water;
shares_grazing_list = Alldata.grazing;
shares_milk_list = Alldata.milk;
shares_vet_list = Alldata.vet;
contact_animal_list = Alldata.contact_animal;
contact_human_list = Alldata.contact_people;
xcoord = Alldata.xcoord/100000;
ycoord = Alldata.ycoord/100000;
xsize = size(xcoord);
N = xsize(1);

cap = 10/100;
arr = {};
arr{1} = equipment_list;
arr{2} = shares_water_list;
arr{3} = shares_grazing_list;
arr{4} = shares_milk_list;
arr{5} = shares_vet_list;
arr{6} = contact_animal_list;
arr{7} = contact_human_list;

% A = attributes_matrix(shares_water_list, 10, N, xcoord, ycoord)

% function [row_ind, col_ind, data_arr] = attributes_matrix(arr, cap, n, xcoord, ycoord)
for i=1:7
    row_ind{i} = [];
    col_ind{i} = [];
    data_arr{i} = [];
end
parfor l=1:7
    row_ind1 = [];
    col_ind1 = [];
    data_arr1 = [];
    for i=1:N-1
        xcoordi = xcoord(i)*ones(i+1,1);
        xdistfromicoord = xcoordi-xcoord(1:i+1);
        ycoordi = ycoord(i)*ones(i+1,1);
        ydistfromicoord = ycoordi-ycoord(1:i+1);
        distVec = sqrt(xdistfromicoord(1:i+1).^2+ydistfromicoord(1:i+1).^2);
        farmIndex = find(distVec <= cap);
        for k=1:size(farmIndex)
            j = farmIndex(k);
            if i ~= j
                if arr{l}(i) + arr{l}(j) == 2
                    row_ind1(end+1) = i;
                    col_ind1(end+1) = j;
                    data_arr1(end+1) = 1;
                end
            end
        end
    end
    row_ind{l} = row_ind1;
    col_ind{l} = col_ind1;
    data_Arr{l} = data_arr1;
end
disp('Saving row_ind, col_in and data_Arr to your filesystem')
save('row_ind.mat', 'row_ind', '-v7.3');
save('col_ind.mat', 'col_ind', '-v7.3');
save('data_Arr.mat', 'data_Arr', '-v7.3');