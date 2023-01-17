function []=dz2(theid, un1, e02, e12, e22, e32, un3, un4, e05, e15, e25, e06, e16, e26, e36)
    thefile = append("id", int2str(theid), ".txt");
    fid = fopen(thefile, 'w');
    
    clc
    %% task1
    disp("task1");
    % un=[1 -2 -1 -3 -3;
    %    -2 4 2 6 6;
    %    3 -6 -3 -9 -9;
    %    4 -8 -4 -12 -12;
    %    -4 8 4 12 12];
    un = rref(un1);
    un = delemptys(un);
    un = FSR(un);
    str = geolin(un);
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">Задача 1>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    clear un
    %% task2
    disp("task2");
    un = [e02; e12; e22; e32];
    un = rref(un);
    un = null(un).';
    un = round(un.*10000);
    disp(rank(un));
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">>Задача 2>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(int2str(rank(un))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    %% task3
    disp("task3");
    

    un = rref(un3);
    un = delemptys(un);
    un = FSR(un);
    str = geolin(un);
    fwrite(fid, unicode2native(char(">>Задача 3>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task4
    disp("task4");

    un = rref(un4);
    un = delemptys(un);
    un = FSR(un);
    str = geolin(un);
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">>Задача 4>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task5
    disp("task5");
    un = [e05; e15; e25];
    un = rref(un);
    if isequal(un,zeros(3))==0
        result = 1;
    else
        result = 0;
    end
    
    fwrite(fid, unicode2native(char(">>Задача 5>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(int2str(result)), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    
    %% task6
    disp("task6");
    % e0 = [-2 0 5 0];
    % e1 = [0 4 0 1];
    % e2 = [-2 4 5 1];
    % e3 = [0 3 6 0];
    un = [e06; e16; e26; e36];
    un = rref(un);
    un = null(un).';
    un = round(un.*10000);
    disp(rank(un));
    
    
    fwrite(fid, unicode2native(char(">>Задача 6>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(int2str(rank(un))), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char("`"), 'UTF-8'), 'uint8');
    fclose(fid);
