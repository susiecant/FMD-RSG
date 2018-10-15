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
arr = shares_water_list;

% A = attributes_matrix(shares_water_list, 10, N, xcoord, ycoord)

% function [row_ind, col_ind, data_arr] = attributes_matrix(arr, cap, n, xcoord, ycoord)
    row_ind = zeros(50000000,1);
    col_ind = zeros(50000000,1);
    data_arr = zeros(50000000,1);
    parfor i=1:N
        xcoordi = xcoord(i)*ones(i+1,1);
        xdistfromicoord = xcoordi-xcoord(1:i+1);
        ycoordi = ycoord(i)*ones(i+1,1);
        ydistfromicoord = ycoordi-ycoord(1:i+1);
        distVec = sqrt(xdistfromicoord(1:i+1).^2+ydistfromicoord(1:i+1).^2);
        farmIndex = find(distVec <= cap);
        for k=1:size(farmIndex)
            j = farmIndex(k);
            if i ~= j
                if arr(i) + arr(j) == 2
                    ind = find(row_ind==0,1)
                    row_ind(ind) = i;
                    col_ind(ind) = j;
                    data_arr(ind) = 1;
                end
            end
        end
    end
% end