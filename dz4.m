function []=dz4(theid, un1, e02, e12, e22, e32, un3, un4, v5, e15, e25, e35, v6, e16, e26, e36)
    thefile = append("id", int2str(theid), ".txt");
    fid = fopen(thefile, 'w');
    
    clc
    %% task1
    disp("Задача 1");
    fwrite(fid, unicode2native(char(">Задача 1>"), 'UTF-8'), 'uint8');
    un = rref(un1);
    un = delemptys(un);
    b = un(:,end).';
    b(1,5) = 0; 
    un = un(:,1:end-1);
    un = FSR(un);
    result = zeros(5);
    for i=0:4
        curr = i.*un(1,:) + un(2,:);
        result(i+1,:) = curr + b;
    end

    fwrite(fid, unicode2native(char("```>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(result(1,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(result(2,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(result(3,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(result(4,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(result(5,:))), 'UTF-8'), 'uint8');
    %% task2
    disp("task2");
    un = [e02-e12+e22; e12-e22+e02; e22-e02+e12; e12-e32+e22];
    fwrite(fid, unicode2native(char(">```>Задача 2>```>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(un(1,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(un(2,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(un(3,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(geolin(un(4,:))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(">```"), 'UTF-8'), 'uint8');
    %% task3
    disp("task3");
    un = rref(un3);
    un = delemptys(un);
    str = geolin(un);
    fwrite(fid, unicode2native(char(">Задача 3>`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`>"), 'UTF-8'), 'uint8');
    %% task4
    disp("task4");
    un = rref(un4);
    un = delemptys(un);
    b = un(:,end).';
    b(1,5) = 0; 
    un = un(:,1:end-1);
    un = FSR(un);
    un = un + b;
    str = geolin(un);
    fwrite(fid, unicode2native(char(">Задача 4>`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task5
    disp("task5");
    clear un str
    v5 = v5.';
    e15 = e15.';
    e25 = e25.';
    e35 = e35.';

    un = [e15 e25 e35];
    str = geolin((inv(un)*v5).');
    % if str="["
    %     str = "[]"
    % end
    fwrite(fid, unicode2native(char("`>>Задача 5>`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task6
    disp("task6");
    v6 = v6.';
    e16 = e16.';
    e26 = e26.';
    e36 = e36.';
    un = [e16 e26 e36];
    %un = inv(un);
    %un = un*v6;
    str = geolin((inv(un)*v6).');
    
    fwrite(fid, unicode2native(char("`>>Задача 6>`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');

    fclose(fid);