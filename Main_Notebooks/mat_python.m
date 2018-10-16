names = {'shares_equipment', 'shares_water', 'shares_grazing', 'shares_milk', 'shares_vet', 'contact_animal', 'contact_human'};
 for i=1:7
     row = row_ind{i};
     col = col_ind{i};
     data = data_Arr{i};
     save(strcat(names{i}, '_rows.mat'), 'row')
     save(strcat(names{i},'_cols.mat'), 'col')
     save(strcat(names{i}, '_data.mat'), 'data')
 end
 