function str = geolin2(matrix)
    matrix = delemptys(matrix);
    dim = size(matrix);
    str = "[";
    for i=1:dim(1)
        for j=1:dim(2)
            if j~=dim(2)
                str = str + num2str(matrix(i, j)) + ", ";
            elseif i~=dim(1)
                str = str + num2str(matrix(i, j)) + "]"+ newline +"[";
            else
                str = str + num2str(matrix(i, j)) + "]";
            end
         end
    end
end 


