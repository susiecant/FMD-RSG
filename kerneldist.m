xcoord = Alldata.xcoord/100000;
ycoord = Alldata.ycoord/100000;
psi = 0.00657;
xsize = size(xcoord);
N = xsize(1);

cap = 10/100;

% A = attributes_matrix(shares_water_list, 10, N, xcoord, ycoord)

% function [row_ind, col_ind, data_arr] = attributes_matrix(arr, cap, n, xcoord, ycoord)

row_ind1 = [];
col_ind1 = [];
data_arr1 = [];
kerneldata_arr1 = [];
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
            row_ind1(end+1) = i;
            col_ind1(end+1) = j;
%             data_arr1(end+1) = distVec(j);
            kerneldata_arr1(end+1) =  (psi)/(psi^2 + distVec(j)^2);
        end
    end
end


disp('Saving row_ind, col_in and data_Arr to your filesystem')
save('row_ind1.mat', 'row_ind1', '-v7.3');
save('col_ind1.mat', 'col_ind1', '-v7.3');
% save('data_arr1.mat', 'data_arr1', '-v7.3');
save('kerneldata_arr1.mat', 'kerneldata_arr1', '-v7.3');

row = row_ind1;
col = col_ind1;
% data = data_arr1;
data = kerneldata_arr1;
save(strcat('kerneldist', '_rows.mat'), 'row')
save(strcat('kerneldist','_cols.mat'), 'col')
save(strcat('kerneldist', '_data.mat'), 'data')