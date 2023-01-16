function f=changecolumns(matrix, changes)
    dimch = size(changes);
    for i=1:dimch(1)
        curr = matrix(:, changes(i, 1));
        matrix(:, changes(i, 1)) = matrix(:, changes(i, 2));
        matrix(:, changes(i, 2)) = curr;
    end
    f=matrix;
end