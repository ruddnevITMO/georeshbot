function str = geolin(matrix, fid)
    matrix = delemptys(matrix);
    dim = size(matrix);
    str = "[";
    for i=1:dim(1)
        for j=1:dim(2)
            if j~=dim(2)
                str = str + num2str(matrix(i, j)) + ", ";
            elseif i~=dim(1)
                str = str + num2str(matrix(i, j)) + "; ";
            else
                str = str + num2str(matrix(i, j)) + "]";
            end
         end
    end
end 

