function f=delemptys(matrix)
    dim = size(matrix);
    if (dim(1)==0 || dim(2)==0)
        f = [];
        return
    end
    newmatrix = matrix(1,:);
    for i = 2:dim(1)
        if isequal(matrix(i,:),zeros(1,dim(2)))==0
            newmatrix = [newmatrix; matrix(i,:)];
        end
    end
    f = newmatrix;
end

