%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Uncomment these if they aren't already loaded%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% disp('Loading row index vectors. This will take a minute or two.')
% row_ind = load('row_ind.mat');
% disp('Done! Row Index vectors loaded')
% disp('Loading column index vectors. This will take a minute or two.')
% col_ind = load('col_ind.mat');
% disp('Done! Column Index vectors loaded')
% disp('Loading data vectors. This will take a minute or two.')
% data_Arr = load('data_Arr.mat');
% disp('Done! Data vectors loaded')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Making into a symmetric matrix and creating the corresponding sparse matrix%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp('Creating sparse matrices for the seven attributes. This may take a minute')
for k=1:7
    k
    sizeVec = size(max(row_ind{k}, col_ind{k}));
    N = sizeVec(1);
    row_indSym{k} = [row_ind{k} 1:N];
    col_indSym{k} = [col_ind{k} 1:N];
    data_ArrSym{k} = [data_Arr{k} zeros(1,N)];
    S{k} = sparse(row_indSym{k}, col_indSym{k}, data_ArrSym{k});
end