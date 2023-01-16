function []=dz3(theid, e01, e11, e21, e31, e41, e02, e12, e22, e32, e42, e52, e03, e13, e23, e33, e43, e04, e14, e24, e34, e44, e05, e15, e25, e35)
    thefile = append("id", int2str(theid), ".txt");
    fid = fopen(thefile, 'w');
        
    clc
    %% task1
    disp("task1");
    
    un = [e01; e11; e21; e31; e41];
    un = rref(un);
    disp(rank(un));
    fwrite(fid, unicode2native(char(">Задача 1>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(int2str(rank(un))), 'UTF-8'), 'uint8');
    %% task2
    disp("task2");
    % e0 = [1 0 0];
    % e1 = [0 1 0];
    % e2 = [1 1 1];
    % e3 = [-1 -3 -2];
    % e4 = [-2 1 0];
    % e5 = [1 5 5];
    un = [e02; e12; e22; e32; e42; e52];
    un = rref(un)
    disp(rank(un));
    
    fwrite(fid, unicode2native(char(">>Задача 2>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(int2str(rank(un))), 'UTF-8'), 'uint8');
    %% task3
    disp("task3");
    % e0 = [1 -2 3 0 5];
    % e1 = [0 1 -2 -1 -1];
    % e2 = [-2 3 -3 2 -10];
    % e3 = [0 0 -1 -1 1];
    % e4 = [3 -4 4 -3 14];
    un = [e03; e13; e23; e33; e43];
    un = rref(un);
    disp(un);
    str = geolin(un);
    fwrite(fid, unicode2native(char(">>Задача 3>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task4
    disp("task4");
    un = [e04; e14; e24; e34; e44];
    un = rref(un);
    str = geolin(un);
    fwrite(fid, unicode2native(char(">>Задача 4>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task5
    disp("task5");
    un = [e05; e15; e25; e35];
    un = rref(un);
    un = delemptys(un);
    un = FSR(un);
    str = geolin(un);
    
    fwrite(fid, unicode2native(char(">>Задача 5>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    fclose(fid);