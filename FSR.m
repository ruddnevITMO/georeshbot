function f=FSR(matrix)
    dim = size(matrix);
    changes = [];
    for i=1:dim(1)
       if matrix(i, i)~=1
           currchange = i;
           for j=i+1:dim(2)
              if matrix(i, j)==1
                 currchange = [currchange j];
                 break;
              end
           end
           changes = [changes; currchange];
       end
    end
    matrix = changecolumns(matrix, changes);
    matrix((dim(1)+1):dim(2), (dim(1)+1):dim(2)) = eye(dim(2)-dim(1));
    for i=1:dim(2)
        for j=1:dim(2)
            if i~=j
                matrix(i,j)= (-1)*matrix(i,j);
            end
        end
    end
    result = zeros(dim(2)-dim(1), dim(2));
    for i=(dim(1)+1):dim(2)
        result(i-dim(1),:) = (matrix(:, i).');
    end
    result = changecolumns(result, changes);
    f = result;
end
